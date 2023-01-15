"""
Predictor.py: predicts the likelyhood of the Mol in a given season and episode
"""

import Settings as s
from Layers.Moldel import Moldel
from numpy.random import RandomState
from Printers.PieChartPrinter import PieChartPrinter
from Printers.BarChartPrinter import BarChartPrinter

# Remove season to predict from training data
s.USE_SEASONS.discard(s.PREDICT_SEASON)

# Build and run the moldel
random_generator = RandomState(s.RANDOM_SEED)
moldel = Moldel(random_generator)
distribution = moldel.compute_distribution(s.PREDICT_SEASON, s.PREDICT_EPISODE, s.USE_SEASONS)

# Print result in popup or as a file
if s.SAVE_AS_FILE:
    filename = f"s{s.PREDICT_SEASON}e{s.PREDICT_EPISODE}"
else:
    filename = None
# printer = PieChartPrinter(s.PREDICT_SEASON, s.PREDICT_EPISODE, filename)
printer = BarChartPrinter(s.PREDICT_SEASON, s.PREDICT_EPISODE, filename)
printer.print(distribution)
