"""
Trainer.py: trains the moldel based on data in Data directory
"""

import Settings as s
from Data.LastEpisodes import get_last_episode
from Layers.Appearance.AppearanceLayer import AppearanceLayer
from Layers.ExamAccusations.ExamAccusationsLayer import ExamAccusationsLayer
from Layers.Power.PowerLayer import PowerLayer
from Layers.ExamDrop.ExamDropLayer import ExamDropLayer
from Layers.ExamPass.ExamPassLayer import ExamPassLayer
from Layers.Moldel import Moldel
from Layers.Money.MoneyLayer import MoneyLayer
from Layers.Special.MemoryLayer import MemoryLayer
from Layers.Special.PotentialMolLayer import PotentialMolLayer
from Layers.Wikipedia.WikipediaLayer import WikipediaLayer
from Validators.PieChartCreator import PieChartCreator
from Validators.Precomputer import Precomputer
from Validators.TotalLogLoss import TotalLogLoss
from Validators.ValidationMetrics import ValidationMetrics
from numpy.random.mtrand import RandomState
from progress.bar import Bar

distributions = dict()
random_generator = RandomState(s.RANDOM_SEED)

layers = {
    "appearance": AppearanceLayer(2/11, 11, 4, 2, 0.01),
    "exam-accusations": ExamAccusationsLayer(random_generator),
    "power": PowerLayer(random_generator),
    "exam-drop": ExamDropLayer(120, 4, random_generator),
    "exam-pass": ExamPassLayer(random_generator),
    "money": MoneyLayer(0.99, 4, 9, random_generator),
    "wikipedia": WikipediaLayer(-0.524, 0.782, 5, random_generator)
}
validators = {
    "appearance": Precomputer("Appearance Stacker"),
    "exam-accusations": Precomputer("Exam Accusations Stacker"),
    "power": Precomputer("Power Stacker"),
    "exam-drop": Precomputer("Exam Drop Stacker"),
    "exam-pass": Precomputer("Exam Pass Stacker"),
    "money": Precomputer("Money Stacker"),
    "wikipedia": Precomputer("Wikipedia Stacker")
}

for name, layer in layers.items():
    if s.TRAIN_LAYER == 'all' \
            or s.TRAIN_LAYER == name:

        total_tasks = sum([get_last_episode(season) + 1 for season in s.USE_SEASONS])
        progress_bar = Bar("Training " + name + " layer:", max=total_tasks)
        for season in s.USE_SEASONS:
            train_seasons = s.USE_SEASONS.difference({season})
            for episode in range(get_last_episode(season) + 1):
                distributions[(season, episode)] = layer.compute_distribution(season, episode, train_seasons)
                progress_bar.next()
        progress_bar.finish()
        validator = validators[name]
        # validator = PieChartCreator("Uniform (9-21)")
        # validator = ValidationMetrics(9, [10, 9, 8, 7, 6, 5, 4, 3, 2])
        # validator = TotalLogLoss()
        validator.validate(distributions)
