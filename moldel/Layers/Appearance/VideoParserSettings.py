# This is the configuration file for the VideoParser class. When you want to run the VideoParser for a certain episode
# then you need to change these values appropriately.
from Data.Player import Player

# The season and episode number which are used to save the Appearance results of the videos and to load them
# during training of the Appearance layer.
SEASON_NUMBER = 23
EPISODE_NUMBER = 4

# The location to the video file of the episode on which you want to run the VideoParser. Only mp4 and mkv files have
# been tested with the VideoParser, other video formats might not work. Make sure that only the episode is included in
# video. MolTalk and commercial breaks should not be contained in the video.
EPISODE_VIDEO_LOCATION = "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/AppearanceData/S2022E04.mp4"

# A set of all players that were alive during this episode, including the person that dropped off during this
# episode. But excluding players that dropped off during earlier episodes and did not return during this episode.
ALIVE_PLAYERS = {
  Player.ARNO_23,
  Player.EVERON_23,
  Player.FRESIA_23,
  Player.HILA_23,
  Player.KIM_LIAN_23,
  Player.LAETITIA_23,
  Player.SAHIL_23,
  Player.THOMAS_23
}

# The locations of the pictures for each player. Make sure that the quality of this pictures is good enough. This means
# that for each player the chin, eyes, mouth and nose are clearly visible. Also the edges of the face should be clear in
# the picture (if there is too much shadow over the face in the picture then it might have problems detecting the
# players). The player should look right into the camera (not to the left or the right). Moreover make sure that the
# picture only contains the head of the player (including the body of the player is unnecessary and having multiple
# faces in 1 picture might confuse the algorithm). Recommended is to pick a close-up of the player during the first
# episode or a moment when the player has a solo talk moment with a black background where he gives his opinion about
# something that happened. Never use a picture from the intro (because these are often low quality and players might
# look different during the intro then during the episode). If you cannot find a good quality picture then you can
# search for one on Google or check the second episode. When getting the results make sure that every player, except the
# players that dropped off, have been detected at least 75 times during every episode or has been detected at least 100
# times during episode 2, 3 or 4. If this is not the case then you should pick a higher quality picture of the player.
# If this new picture still does not give higher detection values then you should pick the best picture and stick to the
# low detection values of the player.
FACE_IMAGE_LOCATIONS = {
  Player.ARNO_23: "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/AppearanceData/Faces/23-arno.jpg",
  Player.EVERON_23: "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/AppearanceData/Faces/23-everon.jpg",
  Player.FRESIA_23: "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/AppearanceData/Faces/23-fresia.jpg",
  Player.GLEN_23: "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/AppearanceData/Faces/23-glen.jpg",
  Player.HILA_23: "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/AppearanceData/Faces/23-hila.jpg",
  Player.KIM_LIAN_23: "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/AppearanceData/Faces/23-kim-lian.jpg",
  Player.LAETITIA_23: "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/AppearanceData/Faces/23-laetitia.jpg",
  Player.SAHIL_23: "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/AppearanceData/Faces/23-sahil.jpg",
  Player.SUZANNE_23: "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/AppearanceData/Faces/23-suzanne.jpg",
  Player.THOMAS_23: "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/AppearanceData/Faces/23-thomas.jpg",
  Player.WELMOED_23: "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/AppearanceData/Faces/23-welmoed.jpg"
}

# How many frames get skipped before analysing a frame (setting this value higher will make the script run faster,
# but makes the results less accurate). The general rule is to use 1 frame every 0.5 seconds. Therefore for video files
# with 25 frames per second it is recommended to use a FRAME_SKIP of 10 (which means a frame get analysed every 0.4
# second). For video files with 30 frames per second it is recommended to use a FRAME_SKIP of 15.
FRAME_SKIP = 10

# The folder in which all parsed results of the videos will be stored.
SAVE_FOLDER = "moldel/Data/AppearanceData/"