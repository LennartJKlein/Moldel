"""
__main__.py: main entry of the moldel to run any command
"""

import sys
import Settings as s
LAYERS = ["all", "appearance", "exam-accusations", "exam-drop", "exam-pass", "money", "wikipedia"]

if len(sys.argv) < 2 \
        or not (sys.argv[1] == 'train' or sys.argv[1] == 'predict' or sys.argv[1] == 'performance'):
    print("python moldel <command>")
    print("")
    print("Available commands:")
    print("train       :  train the moldel with the data from the Data folder")
    print("predict     :  predict the Mol for a specific season and episode")
    print("performance :  show how the moldel performs at finding the Mol in a season")
    print("")
    exit()
if len(sys.argv) > 1:
    # TRAIN FEATURE
    if sys.argv[1] == 'train':
        if len(sys.argv) > 2:
            if not sys.argv[2] in LAYERS:
                print("python moldel train <layer>")
                print("")
                print("Available options:")
                print("python moldel train <layer>   :   " + " | ".join(LAYERS))
                print("")
                exit()
            else:
                s.TRAIN_LAYER = sys.argv[2]
        import Trainer

    # PREDICT FEATURE
    elif sys.argv[1] == 'predict':
        if len(sys.argv) > 2:
            if not sys.argv[2].isdigit() \
                or not sys.argv[3].isdigit() \
                    or not int(sys.argv[2]) > 0 \
                    or not int(sys.argv[3]) >= 0:
                print("python moldel predict <season> <episode>")
                print("")
                print("Available options:")
                print("<season>    :   number of the season to predict")
                print("<episode>   :   number of the episode to predict")
                print("--file      :   save the result as a file")
                print("--reel      :   save the result as a Instagram reel image")
                print("")
                exit()
            else:
                s.PREDICT_SEASON = int(sys.argv[2])
                s.PREDICT_EPISODE = int(sys.argv[3])
            if len(sys.argv) > 4:
                s.SAVE_AS_FILE = sys.argv[4] == "--file"
                s.SAVE_AS_REEL = sys.argv[4] == "--reel"
            if len(sys.argv) > 5:
                s.SAVE_AS_FILE = sys.argv[5] == "--file"
                s.SAVE_AS_REEL = sys.argv[5] == "--reel"
        import Predictor

    # PERFORMANCE FEATURE
    elif sys.argv[1] == 'performance':
        if len(sys.argv) > 2:
            if not sys.argv[2].isdigit() \
                    or not int(sys.argv[2]) > 0:
                print("python moldel performance <season>")
                print("")
                print("Available options:")
                print("<season>    :   number of the season to check")
                print("")
                exit()
            else:
                s.PREDICT_SEASON = int(sys.argv[2])
        s.WHOLE_SEASON = True
        import Predictor

    else:
        exit()
