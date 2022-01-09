import sys
import Settings as s
from Layers.Moldel import Moldel
from numpy.random import RandomState
from Printers.PieChartPrinter import PieChartPrinter
from Printers.TextSortedPrinter import TextSortedPrinter

# Validate and use command line arguments
if len(sys.argv) > 1:
    if not sys.argv[1].isdigit() \
    or not sys.argv[2].isdigit() \
    or not int(sys.argv[1]) > 0 \
    or not int(sys.argv[2]) > 0:
        print("Usage: python moldel [SEASON] [LATEST EPISODE] [--file]")
        exit()
    else:
        s.PREDICT_SEASON = int(sys.argv[1])
        s.LATEST_EPISODE = int(sys.argv[2])
if len(sys.argv) > 3:
    s.SAVE_AS_FILE = sys.argv[3] == '--file'

# Remove season to predict from training data
s.TRAIN_SEASONS.discard(s.PREDICT_SEASON)

# Build and run the moldel
random_generator = RandomState(s.RANDOM_SEED)
moldel = Moldel(random_generator)
distribution = moldel.compute_distribution(s.PREDICT_SEASON, s.LATEST_EPISODE, s.TRAIN_SEASONS)

# Print result in popup or as a file
if s.SAVE_AS_FILE:
    filename = f"s{s.PREDICT_SEASON}e{s.LATEST_EPISODE}"
else:
    filename = None
printer = PieChartPrinter(s.PREDICT_SEASON, s.LATEST_EPISODE, filename)
printer.print(distribution)