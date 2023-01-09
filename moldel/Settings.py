"""
Settings.py: settings that are used when running the moldel
"""

RANDOM_SEED = 949019755
USE_SEASONS = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}
TRAIN_FOLDER = "moldel/Predictions/"
TRAIN_LAYER = "all"  # can be overwritten via command line <layer>
PREDICT_SEASON = 24  # can be overwritten via command line <season>
PREDICT_EPISODE = 1  # can be overwritten via command line <episode>
SAVE_AS_FILE = False  # can be overwritten via command line --file
