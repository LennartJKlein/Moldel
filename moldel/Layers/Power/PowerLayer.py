from numpy.random import RandomState

from Data.ExerciseData.Dataclasses.Exercise import Exercise
from Data.ExamData.Dataclasses.Episode import Episode
from Data.ExerciseData.Exercises.All import EXERCISES_DATA
from Data.Player import Player
from Data.PlayerData import get_players_in_season
from Layers.Layer import Layer
from Layers.Special.EqualLayer import EqualLayer
from Layers.Special.NormalizeLayer import NormalizeLayer
from Layers.Special.PotentialMolLayer import PotentialMolLayer
from sklearn.linear_model import LogisticRegression
from typing import Dict, List, Set, Tuple
import itertools as it
import numpy as np
import math


class InnerPowerLayer(Layer):
    def __init__(self, random_generator: RandomState):
        self.__random_generator = random_generator

    def compute_distribution(
        self, predict_season: int, latest_episode: int, train_seasons: Set[int]
    ) -> Dict[Player, float]:
        available_seasons = EXERCISES_DATA.keys()
        train_seasons = train_seasons.intersection(available_seasons)
        if predict_season not in available_seasons:
            return EqualLayer().compute_distribution(
                predict_season, latest_episode, train_seasons
            )

        estimator = self.__train(train_seasons)
        alive_players = EXERCISES_DATA[predict_season].get_alive(latest_episode)
        result = {
            player: 1.0 if player in alive_players else 0.0
            for player in get_players_in_season(predict_season)
        }
        for exercise in EXERCISES_DATA[predict_season].get_exercises(latest_episode):
            prediction = self.__predict_for_exercise(
                exercise, previous_exercise, alive_players, estimator
            )
            for player, likelihood in prediction.items():
                result[player] *= likelihood
        return result

    def __train(self, train_seasons: Set[int]) -> LogisticRegression:
        """Train the estimator, which estimates the probability that someone has the powerful positions in every exercise.

        Arguments:
            train_seasons (Set[int]): All seasons used as training data.

        Returns:
            The estimator used to estimate the likelihood that someone has the powerful positions in every exercise.
        """
        train_input, train_output = self.__get_train_data(train_seasons)
        estimator = LogisticRegression(
            solver="lbfgs", penalty=None, random_state=self.__random_generator
        )
        estimator.fit(train_input, train_output)
        return estimator

    @classmethod
    def __predict_for_exercise(
        self,
        exercise: Exercise,
        previous_exercise: Exercise,
        alive_players: Set[Player],
        estimator: LogisticRegression,
    ) -> Dict[Player, float]:
        """Determine the probability that the exercises happen for each mol, based on the powerful positions during the exercises.

        Arguments:
            exercise (Exercise): The episode for which we estimate the probability that he/she is in the powerful position.
            alive_players (Set[Player]): The players that could still be the mol.
            estimator (LogisticRegression): The estimator used to estimate the likelihood.

        Returns:
            A dictionary with as key a player that could be the Mol and as value the probability that he/she is in the powerful position.
        """
        power_likelihoods = self.__get_power_likelihoods(
            exercise, previous_exercise, estimator
        )
        mol_likelihoods = dict()
        powerful = exercise.powerful
        power_likelihood = np.prod([power_likelihoods[p] for p in powerful])
        for mol in alive_players:
            possible_powerful = set(exercise.alive).difference({mol})
            power_sum = 0.0
            for players in it.combinations(possible_powerful, len(powerful)):
                power_sum += np.prod([power_likelihoods[p] for p in players])
            mol_likelihoods[mol] = power_likelihood / power_sum
        return mol_likelihoods

    @classmethod
    def __get_train_data(self, train_seasons: Set[int]) -> Tuple[np.array, np.array]:
        """Get the train data used to estimate the likelihood of being powerful.

        Arguments:
            train_seasons (Set[int]):  All seasons used as training data.

        Returns:

        """
        train_input = []
        train_output = []
        for train_season in train_seasons:
            train_season = EXERCISES_DATA[train_season]
            previous_exercise = Exercise()
            for exercise in EXERCISES_DATA[train_season].get_exercises(math.inf):
                for player in exercise.alive:
                    train_input.append(
                        self.__get_input(player, previous_exercise.powerful)
                    )
                    train_output.append(1.0 if player in exercise.powerful else 0.0)
                previous_exercise = exercise
        return np.array(train_input), np.array(train_output)

    @classmethod
    def __get_power_likelihoods(
        self,
        exercise: Exercise,
        previous_exercise: Exercise,
        estimator: LogisticRegression,
    ) -> Dict[Player, float]:
        """Get the powerful likelihoods for all players in an episode, based on being powerful in the past.

        Arguments:
            exercise (Exercise): The episode for which we determine the powerful likelihoods.
            estimator (LogisticRegression): The estimator used to estimate the likelihood that someone is powerful based
                on the past.

        Returns:
            A dictionary with as key a player that was alive in this episode and as value the likelihood of being powerful (float).
        """
        past_power = previous_exercise.powerful
        power_likelihoods = dict()
        for player in exercise.alive:
            features = self.__get_input(player, past_power)
            power_likelihoods[player] = estimator.predict_proba(np.array([features]))[
                0
            ][1]
        probability_sum = sum(power_likelihoods.values())
        return {
            player: likelihood / probability_sum
            for player, likelihood in power_likelihoods.items()
        }

    @staticmethod
    def __get_input(player: Player, past_power: Set[Player]) -> List[float]:
        """Get the input encoding for a player based on the previous power

        Arguments:
            player (Player): The input encoding for a player.
            previous_power (Dict[Player, int]): If player was in power previous exercise

        Returns:
            The feature encoding for that player.
        """
        return [sum(1.0 for p in past_power if p != player)]


class PowerLayer(PotentialMolLayer):
    """The Exam Pass Layer predicts whether a player is the Mol based on how many jokers and exemptions players used
    during the test."""

    def __init__(self, random_generator: RandomState):
        """Constructor of the Exam Pass Layer.

        Arguments:
            random_generator (RandomState): The random generator used to generate random values.
        """
        super().__init__(NormalizeLayer(InnerPowerLayer(random_generator)))
