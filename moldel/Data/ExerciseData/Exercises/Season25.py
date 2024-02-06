from Data.ExerciseData.Dataclasses.Season import Season
from Data.ExerciseData.Dataclasses.Exercise import Exercise
from Data.ExerciseData.Dataclasses.Earning import Earning
from Data.Player import Player

################
# Aflevering 1
players1 = {
    Player.ANNA_25,
    Player.BABS_25,
    Player.FONS_25,
    Player.JEROEN_25,
    Player.JIP_25,
    Player.JUSTIN_25,
    Player.KEES_25,
    Player.RIAN_25,
    Player.ROSARIO_25,
    Player.TOOSKE_25,
}
exercises1 = [
    # Opdracht 1: Speeddate
    Exercise(
        episode=1,
        alive=players1,
        maximum=6000,
        powerful=set(),
        earned=[
            Earning(
                money=6000,
                major={
                    Player.ANNA_25,
                    Player.BABS_25,
                    Player.FONS_25,
                    Player.JEROEN_25,
                    Player.JIP_25,
                    Player.JUSTIN_25,
                    Player.KEES_25,
                    Player.RIAN_25,
                    Player.ROSARIO_25,
                    Player.TOOSKE_25,
                },
            ),
        ],
    ),
    # Opdracht 2: Afschilderen
    Exercise(
        episode=1,
        alive=players1,
        maximum=2500,
        powerful=[
            Player.ANNA_25,
            Player.BABS_25,
            Player.KEES_25,
            Player.RIAN_25,
            Player.TOOSKE_25,
        ],
        earned=[
            Earning(
                money=500,
                major={Player.RIAN_25, Player.BABS_25},
                minor={
                    Player.ANNA_25,
                    Player.FONS_25,
                    Player.KEES_25,
                    Player.TOOSKE_25,
                },
            ),
        ],
    ),
]

################
# Aflevering 2
players2 = {
    Player.ANNA_25,
    Player.FONS_25,
    Player.JEROEN_25,
    Player.JIP_25,
    Player.JUSTIN_25,
    Player.KEES_25,
    Player.RIAN_25,
    Player.ROSARIO_25,
    Player.TOOSKE_25,
}
exercises2 = [
    # Opdracht 1: Molympische Spelen
    Exercise(
        episode=2,
        alive=players2,
        maximum=1968,
        powerful=[
    Player.ANNA_25,
    Player.FONS_25,
    Player.JEROEN_25,
    Player.KEES_25,
    Player.ROSARIO_25,
    Player.TOOSKE_25,
    ],
        earned=[],
    ),
    # Opdracht 2: Uitzitten
    Exercise(
        episode=2,
        alive=players2,
        maximum=4000,
        powerful=[
    Player.JEROEN_25,
    Player.KEES_25,
    Player.RIAN_25,
    Player.TOOSKE_25,
        ],
        earned=[
            Earning(money=750, major={Player.FONS_25}),
            Earning(money=750, major={Player.ANNA_25}),
            Earning(money=250, major={Player.ROSARIO_25}),
            Earning(money=250, major={Player.JUSTIN_25}),
            Earning(money=-750, major={Player.JIP_25}),
        ],
    ),
]

################
# Aflevering 3
players3 = {
    Player.ANNA_25,
    Player.FONS_25,
    Player.JEROEN_25,
    Player.JUSTIN_25,
    Player.KEES_25,
    Player.RIAN_25,
    Player.ROSARIO_25,
    Player.TOOSKE_25,
}
exercises3 = [
    # Opdracht 1: De violen stemmen
    Exercise(
        episode=3,
        alive=players3,
        maximum=2000,
        powerful=set(),
        earned=[
            Earning(
                money=-200,
                minor={
                    Player.ANNA_25,
                    Player.FONS_25,
                    Player.JEROEN_25,
                    Player.JUSTIN_25,
                    Player.KEES_25,
                    Player.RIAN_25,
                    Player.ROSARIO_25,
                    Player.TOOSKE_25,
                },
            ),
            Earning(
                money=400,
                major={
                    Player.JEROEN_25,
                    Player.KEES_25,
                },
            ),
            Earning(
                money=-200,
                major={
                    Player.KEES_25,
                    Player.JEROEN_25,
                },
                minor={Player.RIAN_25, Player.JUSTIN_25},
            ),
            Earning(
                money=400,
                major={
                    Player.RIAN_25,
                    Player.ROSARIO_25,
                    Player.TOOSKE_25,
                    Player.JEROEN_25,
                    Player.JUSTIN_25,
                },
                minor={Player.FONS_25},
            ),
            Earning(
                money=-200,
                major={
                    Player.ANNA_25,
                    Player.JEROEN_25,
                    Player.TOOSKE_25,
                    Player.ROSARIO_25,
                    Player.KEES_25,
                },
                minor={
                    Player.FONS_25,
                    Player.RIAN_25,
                },
            ),
            Earning(
                money=-200,
                major={
                    Player.ANNA_25,
                    Player.TOOSKE_25,
                    Player.JEROEN_25,
                    Player.ROSARIO_25,
                },
                minor={
                    Player.FONS_25,
                    Player.KEES_25,
                    Player.RIAN_25,
                },
            ),
            Earning(
                money=-200,
                major={
                    Player.JEROEN_25,
                    Player.ANNA_25,
                    Player.KEES_25,
                    Player.ROSARIO_25,
                    Player.TOOSKE_25,
                },
            ),
            Earning(
                money=400,
                major={
                    Player.ANNA_25,
                    Player.JEROEN_25,
                    Player.FONS_25,
                },
                minor={Player.TOOSKE_25},
            ),
            Earning(
                money=-200,
                major={
                    Player.ANNA_25,
                    Player.JEROEN_25,
                },
                minor={
                    Player.KEES_25,
                    Player.RIAN_25,
                },
            ),
            Earning(
                money=400,
                major={
                    Player.TOOSKE_25,
                    Player.JEROEN_25,
                },
                minor={Player.KEES_25},
            ),
        ],
    ),
    # Opdracht 2: Stand en land aflopen
    Exercise(
        episode=3,
        alive=players3,
        maximum=2000,
        powerful=[
          Player.JEROEN_25,
          Player.KEES_25,
          Player.ROSARIO_25,
          Player.RIAN_25,
        ],
        earned=[
            Earning(
                money=150,
                major={Player.ROSARIO_25, Player.ANNA_25},
            ),
            Earning(
                money=150,
                major={Player.JEROEN_25, Player.ROSARIO_25},
            ),
            Earning(
                money=150,
                major={Player.KEES_25, Player.RIAN_25},
            ),
            Earning(
                money=150,
                major={Player.KEES_25, Player.JUSTIN_25},
            ),
        ],
    ),
    # Opdracht 3: Er mee worstelen
    Exercise(
        episode=3,
        alive=players3,
        maximum=2025,
        powerful=[
                    Player.ANNA_25,
                    Player.BABS_25,
                    Player.JEROEN_25,
                    Player.KEES_25,
                    Player.RIAN_25,
                    Player.ROSARIO_25,
                    Player.TOOSKE_25
        ],
        earned=[
            Earning(
                money=75,
                major={Player.FONS_25, Player.JUSTIN_25},
                minor={
                    Player.ANNA_25,
                    Player.BABS_25,
                    Player.JEROEN_25,
                    Player.KEES_25,
                    Player.RIAN_25,
                    Player.ROSARIO_25,
                    Player.TOOSKE_25,
                },
            ),
        ],
    ),
]

################
# Aflevering 4
players4 = {
    Player.ANNA_25,
    Player.FONS_25,
    Player.JEROEN_25,
    Player.KEES_25,
    Player.RIAN_25,
    Player.ROSARIO_25,
    Player.TOOSKE_25,
}
exercises4 = [
    # Opdracht 1: Kijken kijken wel kopen
    Exercise(
        episode=4,
        alive=players4,
        maximum=3000,
        powerful=[
            Player.FONS_25,
            Player.KEES_25,
            Player.ROSARIO_25,
            Player.TOOSKE_25,
        ],
        earned=[
            Earning(
                money=100,
                major={Player.FONS_25, Player.KEES_25, Player.TOOSKE_25},
                minor={Player.JEROEN_25, Player.ANNA_25, Player.RIAN_25},
            ),
            Earning(
                money=100,
                major={Player.FONS_25, Player.KEES_25, Player.ROSARIO_25},
                minor={Player.JEROEN_25, Player.ANNA_25, Player.RIAN_25},
            ),
            Earning(
                money=100,
                major={
                    Player.FONS_25,
                },
                minor={Player.JEROEN_25, Player.ANNA_25, Player.RIAN_25},
            ),
            Earning(
                money=100,
                major={
                    Player.FONS_25,
                    Player.KEES_25,
                },
                minor={Player.JEROEN_25, Player.ANNA_25, Player.RIAN_25},
            ),
            Earning(
                money=100,
                major={Player.ROSARIO_25, Player.TOOSKE_25},
                minor={Player.JEROEN_25, Player.ANNA_25, Player.RIAN_25},
            ),
            Earning(
                money=100,
                major={
                    Player.FONS_25,
                    Player.KEES_25,
                },
                minor={Player.JEROEN_25, Player.ANNA_25, Player.RIAN_25},
            ),
            Earning(
                money=100,
                major={Player.FONS_25, Player.TOOSKE_25},
                minor={Player.JEROEN_25, Player.ANNA_25, Player.RIAN_25},
            ),
        ],
    ),
    # Opdracht 2: Op het spel zetten
    Exercise(
        episode=4,
        alive=players4,
        maximum=3500,
        powerful=set(),
        earned=[
            Earning(
                money=-100,
                minor={
                    Player.ANNA_25,
                    Player.KEES_25,
                    Player.FONS_25,
                    Player.ROSARIO_25,
                },
            ),
            Earning(
                money=-400,
                minor={
                    Player.JEROEN_25,
                    Player.RIAN_25,
                    Player.TOOSKE_25,
                },
            ),
        ],
    ),
]

################
# Aflevering 5
players5 = {
    Player.ANNA_25,
    Player.BABS_25,
    Player.FONS_25,
    Player.JEROEN_25,
    Player.KEES_25,
    Player.RIAN_25,
    Player.ROSARIO_25,
    Player.TOOSKE_25,
}
exercises5 = [
    # Opdracht 1: Op elkaar rekenen
    Exercise(
        episode=5,
        alive=players5,
        maximum=2008,
        powerful=[
            Player.ANNA_25,
            Player.BABS_25,
            Player.KEES_25,
            Player.RIAN_25,
            Player.ROSARIO_25,
            Player.TOOSKE_25,
        ],
        earned=[],
    ),
    # Opdracht 2: Het gebaande pad
    Exercise(
        episode=5,
        alive=players5,
        maximum=38640,
        powerful=[],
        earned=[
            Earning(
                money=-250,
                major={
                    Player.FONS_25,
                },
            ),
            Earning(
                money=-250,
                major={
                    Player.ANNA_25,
                },
            ),
            Earning(
                money=-250,
                major={
                    Player.JEROEN_25,
                },
            ),
            Earning(
                money=-1000,
                minor={
                    Player.ANNA_25,
                    Player.BABS_25,
                    Player.FONS_25,
                    Player.JEROEN_25,
                    Player.RIAN_25,
                    Player.ROSARIO_25,
                    Player.TOOSKE_25,
                },
            ),
        ],
    ),
    # Opdracht 3: Afwegen
    Exercise(
        episode=5,
        alive=players5,
        maximum=2000,
        powerful=[],
        earned=[
            Earning(
                money=-3000,
                major={
                    Player.ROSARIO_25,
                },
            ),
            Earning(
                money=250,
                major={
                    Player.BABS_25,
                },
            ),
            Earning(
                money=-500,
                major={
                    Player.ANNA_25,
                },
            ),
        ],
    ),
]

season25 = Season(
    exercises1
    + exercises2
    + exercises3
    + exercises4
    + exercises5
    # + exercises6
    # + exercises7
    # + exercises8
    # + exercises9
)
