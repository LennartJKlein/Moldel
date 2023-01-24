"""
Predictor.py: predicts the likelyhood of the Mol in a given season and episode
"""

import Settings as s
from Layers.Moldel import Moldel
from numpy.random import RandomState
from Printers.BarChartPrinter import BarChartPrinter
from Printers.InstagramPrinter import InstagramPrinter
from Printers.MolPrinter import MolPrinter
from Data.LastEpisodes import get_last_episode
from progress.bar import Bar

# Remove season to predict from training data
s.USE_SEASONS.discard(s.PREDICT_SEASON)

# Build and run the moldel
random_generator = RandomState(s.RANDOM_SEED)
moldel = Moldel(random_generator)
total_tasks = get_last_episode(s.PREDICT_SEASON) + 1 if s.WHOLE_SEASON else 1
progress_bar = Bar("Predicting episode ", max=total_tasks)
for episode in range(total_tasks):
    s.PREDICT_EPISODE = episode if s.WHOLE_SEASON else s.PREDICT_EPISODE
    distribution = moldel.compute_distribution(s.PREDICT_SEASON, s.PREDICT_EPISODE, s.USE_SEASONS)

    # Print result in popup, as a file or as reel
    if s.WHOLE_SEASON:
        filename = f"s{s.PREDICT_SEASON}e{s.PREDICT_EPISODE}"
        printer = MolPrinter(s.PREDICT_SEASON, s.PREDICT_EPISODE, filename)
        printer.print(distribution)
    elif s.SAVE_AS_FILE:
        filename = f"s{s.PREDICT_SEASON}e{s.PREDICT_EPISODE}"
        printer = BarChartPrinter(s.PREDICT_SEASON, s.PREDICT_EPISODE, filename)
        printer.print(distribution)
    elif s.SAVE_AS_REEL:
        filename = f"s{s.PREDICT_SEASON}e{s.PREDICT_EPISODE}-reel"
        printer = InstagramPrinter(s.PREDICT_SEASON, s.PREDICT_EPISODE, filename)
        printer.print(distribution)
    else:
        printer = BarChartPrinter(s.PREDICT_SEASON, s.PREDICT_EPISODE, None)
        printer.print(distribution)

    # Next operation
    progress_bar.next()
