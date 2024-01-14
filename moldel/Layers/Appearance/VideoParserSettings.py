# This is the configuration file for the VideoParser class. When you want to run the VideoParser for a certain episode
# then you need to change these values appropriately.
from Data.Player import Player

# The season and episode number which are used to save the Appearance results of the videos and to load them
# during training of the Appearance layer.
SEASON_NUMBER = 25
EPISODE_NUMBER = 2

# The location to the video file of the episode on which you want to run the VideoParser. Only mp4 and mkv files have
# been tested with the VideoParser, other video formats might not work. Make sure that only the episode is included in
# video. MolTalk and commercial breaks should not be contained in the video.
EPISODE_VIDEO_LOCATION = "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/AppearanceData/S25E02.mp4"

# A set of all players that were alive during this episode, including the person that dropped off during this
# episode. But excluding players that dropped off during earlier episodes and did not return during this episode.
ALIVE_PLAYERS = {
    Player.ANNA_25,
    Player.FONS_25,
    Player.JEROEN_25,
    Player.JIP_25,
    Player.JUSTIN_25,
    Player.KEES_25,
    Player.RIAN_25,
    Player.ROSARIO_25,
    Player.TOOSKE_25
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
    Player.ANNA_25: "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/Faces/25-ANNA.jpg",
    Player.BABS_25: "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/Faces/25-BABS.jpg",
    Player.FONS_25: "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/Faces/25-FONS.jpg",
    Player.JEROEN_25: "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/Faces/25-JEROEN.jpg",
    Player.JIP_25: "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/Faces/25-JIP.jpg",
    Player.JUSTIN_25: "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/Faces/25-JUSTIN.jpg",
    Player.KEES_25: "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/Faces/25-KEES.jpg",
    Player.RIAN_25: "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/Faces/25-RIAN.jpg",
    Player.ROSARIO_25: "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/Faces/25-ROSARIO.jpg",
    Player.TOOSKE_25: "/Users/LKLEIN/Ontwikkelomgeving/Moldel/moldel/Data/Faces/25-TOOSKE.jpg"
}

# How many frames get skipped before analysing a frame (setting this value higher will make the script run faster,
# but makes the results less accurate). The general rule is to use 1 frame every 0.5 seconds. Therefore for video files
# with 25 frames per second it is recommended to use a FRAME_SKIP of 10 (which means a frame get analysed every 0.4
# second). For video files with 30 frames per second it is recommended to use a FRAME_SKIP of 15.
FRAME_SKIP = 10

# The folder in which all parsed results of the videos will be stored.
SAVE_FOLDER = "moldel/Data/AppearanceData/"
