import sys
import Settings as s
from Layers.Moldel import Moldel
from numpy.random import RandomState
from Printers.PieChartPrinter import PieChartPrinter
from Printers.TextSortedPrinter import TextSortedPrinter

if len(sys.argv) > 1:
    if not sys.argv[1].isdigit() \
    or not sys.argv[2].isdigit() \
    or not int(sys.argv[1]) > 0 \
    or not int(sys.argv[2]) > 0:
        print("Usage: python moldel [SEASON] [LATEST EPISODE]")
        exit()
    else:
        s.PREDICT_SEASON = int(sys.argv[1])
        s.LATEST_EPISODE = int(sys.argv[2])

s.TRAIN_SEASONS.discard(s.PREDICT_SEASON)

random_generator = RandomState(s.RANDOM_SEED)
moldel = Moldel(random_generator)
distribution = moldel.compute_distribution(s.PREDICT_SEASON, s.LATEST_EPISODE, s.TRAIN_SEASONS)
# printer = TextSortedPrinter(0, 2220)
printer = PieChartPrinter()
printer.print(distribution)