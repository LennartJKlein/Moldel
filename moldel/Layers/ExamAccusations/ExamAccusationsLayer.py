from numpy.random import RandomState

from Data.ExamData.Dataclasses.DropType import DropType
from Data.ExamData.Dataclasses.Episode import Episode
from Data.ExamData.Exams.All import EXAM_DATA
from Data.Player import Player
from Data.PlayerData import get_is_mol, get_players_in_season
from Layers.Layer import Layer
from Layers.Special.EqualLayer import EqualLayer
from Layers.Special.NormalizeLayer import NormalizeLayer
from Layers.Special.PotentialMolLayer import PotentialMolLayer
from sklearn.linear_model import LogisticRegression
from typing import Dict, List, Set, Tuple
import itertools as it
import numpy as np
import sys

class InnerExamAccusationsLayer(Layer):
    def __init__(self, random_generator: RandomState):
        self.__random_generator = random_generator

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        available_seasons = EXAM_DATA.keys()
        train_seasons = train_seasons.intersection(available_seasons)
        if predict_season not in available_seasons:
            return EqualLayer().compute_distribution(predict_season, latest_episode, train_seasons)

        estimator = self.__train(train_seasons)
        alive_players = EXAM_DATA[predict_season].get_alive_players(latest_episode)
        result = {player: 1.0 if player in alive_players else 0.0 for player in get_players_in_season(predict_season)}
        for episode in EXAM_DATA[predict_season].episodes.values():
            if episode.id > latest_episode or episode.result.drop != DropType.EXECUTION_DROP:
                continue
            prediction = self.__predict_for_episode(episode, alive_players, estimator)
            for player, likelihood in prediction.items():
                result[player] *= likelihood
        return result

    def __train(self, train_seasons: Set[int]) -> LogisticRegression:
        """ Train the estimator, which estimates the probability that someone is the Mol, based on spoken accusations.

        Arguments:
            train_seasons (Set[int]): All seasons used as training data.

        Returns:
            The estimator used to estimate the likelihood that someone is the Mol based on spoken accusations.
        """
        train_input, train_output = self.__get_train_data(train_seasons)
        estimator = LogisticRegression(solver = "lbfgs", penalty = "none", random_state = self.__random_generator)
        estimator.fit(train_input, train_output)
        return estimator

    @classmethod
    def __predict_for_episode(self, episode: Episode, alive_players: Set[Player], estimator: LogisticRegression) -> Dict[Player, float]:
        """ Determine the probability that a player is the Mol based on the dropouts and spoken
        accusations during an episode.

        Arguments:
            episode (Episode): The episode for which we estimate the probability that its execution result happens.
            alive_players (Set[Player]): The players that could still be the mol.
            estimator (LogisticRegression): The estimator used to estimate the likelihood that someone is the Mol based
                on the spoken accusations.

        Returns:
            A dictionary with as key a player that could be the Mol and as value the probability that it is the Mol.
        """
        # mol_likelihoods = self.__get_mol_likelihoods(episode, estimator)
        # predictions = dict()
        # dropouts = episode.result.players
        # drop_likelihood = np.prod([mol_likelihoods[p] for p in dropouts])
        # for mol in alive_players:
        #     possible_dropouts = set(episode.players).difference({mol})
        #     drop_sum = 0.0
        #     for players in it.combinations(possible_dropouts, len(dropouts)):
        #         drop_sum += np.prod([mol_likelihoods[p] for p in players])
        #     predictions[mol] = drop_likelihood / drop_sum
        # return predictions
        mol_likelihoods = self.__get_mol_likelihoods(episode, estimator)
        predictions = dict()
        for p in alive_players:
            predictions[p] = mol_likelihoods[p]
        return predictions

    @classmethod
    def __get_train_data(self, train_seasons: Set[int]) -> Tuple[np.array, np.array]:
        """ Get the train data used to estimate the likelihood of being the Mol based on spoken accusations.

        Arguments:
            train_seasons (Set[int]):  All seasons used as training data.

        Returns:
            All train input, which is an encoding of the accusations every player made, and all train output, which
            is whether that player was the Mol.
        """
        train_input = []
        train_output = []
        for season in train_seasons:
            season = EXAM_DATA[season]
            for episode in season.episodes.values():
                all_accusations = episode.total_accusations()
                dropouts = episode.result.players
                for player in episode.players:
                    train_input.append(self.__get_input(player, all_accusations, dropouts))
                    train_output.append(1.0 if get_is_mol(player) else 0.0)
        return np.array(train_input), np.array(train_output)

    @classmethod
    def __get_mol_likelihoods(self, episode: Episode, estimator: LogisticRegression) -> Dict[Player, float]:
        """ Get the mol likelihoods for all players in an episode, based on only the spoken accusations.

        Arguments:
            episode (Episode): The episode for which we determine the Mol likelihoods.
            estimator (LogisticRegression): The estimator used to estimate the likelihood that someone is the Mol based
                on spoken accusations.

        Returns:
            A dictionary with as key a player that was alive in this episode and as value the likelihood of being the Mol.
        """
        all_accusations = episode.total_accusations()
        dropouts = episode.result.players
        mol_likelihoods = dict()
        for player in episode.players:
            features = self.__get_input(player, all_accusations, dropouts)
            mol_likelihoods[player] = estimator.predict_proba(np.array([features]))[0][1]
        probability_sum = sum(mol_likelihoods.values())
        return {player: likelihood / probability_sum for player, likelihood in mol_likelihoods.items()}

    @staticmethod
    def __get_input(player: Player, all_accusations: Dict[Player, List[Player]], dropouts: List[Player]) -> List[float]:
        """ Get the input encoding for a player based on spoken accusations.

        Arguments:
            player (Player): The input encoding for a player.
            all_accusations (Dict[Player, List[Player]]): All spoken accusations of each player in an episode.
            dropouts (List[Player]): Dropouts of this episode.

        Returns:
            The feature encoding for that player.
        """
        accusations_made = all_accusations.get(player)
        times_accused = 0
        accused_dropout = 0
        accused_by_dropout = 0
        accused_like_others = 0
        for p, accusations in all_accusations.items():
            if p != player:
                times_accused += sum(accusedPlayer == player for accusedPlayer in accusations)
                if accusations_made is not None:
                    accused_like_others += sum(accusedPlayer in accusations_made for accusedPlayer in accusations)
            if p == player:
                accused_dropout += sum(accusedPlayer in dropouts for accusedPlayer in accusations)
            if p in dropouts:
                accused_by_dropout += sum(accusedPlayer == player for accusedPlayer in accusations)

        return [times_accused, accused_dropout, accused_by_dropout, accused_like_others]

class ExamAccusationsLayer(PotentialMolLayer):
    """ The Exam Accusations Layer predicts whether a player is the Mol based on spoken accusations. """

    def __init__(self, random_generator: RandomState):
        """ Constructor of the Exam Accusations Layer.

        Arguments:
            random_generator (RandomState): The random generator used to generate random values.
        """
        super().__init__(NormalizeLayer(InnerExamAccusationsLayer(random_generator)))