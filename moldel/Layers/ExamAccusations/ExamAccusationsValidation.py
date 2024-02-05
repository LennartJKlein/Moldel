from Data.ExamData.Exams.All import EXAM_DATA
from Data.PlayerData import get_is_mol, get_mol_in_season
from sklearn.linear_model import LogisticRegression
import numpy as np

TRAIN_SEASONS = {
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
}
train_input = []
train_output = []
for season in TRAIN_SEASONS:
    season = EXAM_DATA[season]
    for episode in season.episodes.values():

        all_accusations = episode.total_accusations()
        dropouts = episode.result.players
        for player in episode.players:
            accusations_made = all_accusations.get(player)
            times_accused = 0
            accused_dropout = 0
            accused_by_dropout = 0
            accused_like_others = 0
            for p, accusations in all_accusations.items():
                if p != player:
                    times_accused += sum(
                        accusedPlayer == player for accusedPlayer in accusations
                    )
                    if accusations_made is not None:
                        accused_like_others += sum(
                            accusedPlayer in accusations_made
                            for accusedPlayer in accusations
                        )
                if p == player:
                    accused_dropout += sum(
                        accusedPlayer in dropouts for accusedPlayer in accusations
                    )
                if p in dropouts:
                    accused_by_dropout += sum(
                        accusedPlayer == player for accusedPlayer in accusations
                    )
            train_input.append(
                [
                    times_accused,
                    accused_dropout,
                    accused_by_dropout,
                    accused_like_others,
                ]
            )
            train_output.append(1.0 if get_is_mol(player) else 0.0)

train_input = np.array(train_input)
train_output = np.array(train_output)

estimator = LogisticRegression()
estimator.fit(train_input, train_output)

for season_id in TRAIN_SEASONS:
    season = EXAM_DATA[season_id]
    for episode in season.episodes.values():

        drop_probabilities = dict()
        all_accusations = episode.total_accusations()
        dropouts = episode.result.players
        mol_likelihoods = dict()
        for player in episode.players:
            accusations_made = all_accusations.get(player)
            times_accused = 0
            accused_dropout = 0
            accused_by_dropout = 0
            accused_like_others = 0
            for p, accusations in all_accusations.items():
                if p != player:
                    times_accused += sum(
                        accusedPlayer == player for accusedPlayer in accusations
                    )
                    if accusations_made is not None:
                        accused_like_others += sum(
                            accusedPlayer in accusations_made
                            for accusedPlayer in accusations
                        )
                if p == player:
                    accused_dropout += sum(
                        accusedPlayer in dropouts for accusedPlayer in accusations
                    )
                if p in dropouts:
                    accused_by_dropout += sum(
                        accusedPlayer == player for accusedPlayer in accusations
                    )
            features = [
                times_accused,
                accused_dropout,
                accused_by_dropout,
                accused_like_others,
            ]
            mol_likelihoods[player] = estimator.predict_proba(np.array([features]))[0][
                1
            ]
        probability_sum = sum(mol_likelihoods.values())
        drop_probabilities = {
            player: likelihood / probability_sum
            for player, likelihood in mol_likelihoods.items()
        }

        print(
            "Probability comparison s"
            + str(season_id)
            + "e"
            + str(episode.id)
            + ": "
            + str(round(drop_probabilities[get_mol_in_season(season_id)], 2)),
            str(round(1 / len(drop_probabilities), 2)),
        )
