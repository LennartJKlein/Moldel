import sys
import Settings as s
from Layers.Moldel import Moldel
from numpy.random import RandomState
from Printers.PieChartPrinter import PieChartPrinter
from Printers.TextSortedPrinter import TextSortedPrinter

# python moldel train wikipedia
# python moldel train examdrop 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22
# python moldel predict 23 4

# Validate and use command line arguments
# if len(sys.argv) < 1:
#     print("Usage: python moldel [COMMAND]")
#     print("Available commands:")
#     print("train    : use the data of one or more layers to train the moldel")
#     print("predict  : predict the Mol for a specific season and episode")
#     exit()
if len(sys.argv) > 1:
    if not sys.argv[1].isdigit() \
    or not sys.argv[2].isdigit() \
    or not int(sys.argv[1]) > 0 \
    or not int(sys.argv[2]) >= 0:
        print("Usage: python moldel [SEASON] [LATEST EPISODE] [--file]")
        print("Options and arguments:")
        print("train    :")
        print("predict  :")
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