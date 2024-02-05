from Data.ExerciseData.Dataclasses.Season import Season
from Data.ExerciseData.Dataclasses.Exercise import Exercise
from Data.ExerciseData.Dataclasses.Earning import Earning
from Data.Player import Player

################
# Aflevering 1
players1 = {
    Player.ARNO_23,
    Player.EVERON_23,
    Player.FRESIA_23,
    Player.GLEN_23,
    Player.HILA_23,
    Player.KIM_LIAN_23,
    Player.LAETITIA_23,
    Player.SAHIL_23,
    Player.SUZANNE_23,
    Player.THOMAS_23,
    Player.WELMOED_23,
}
exercises1 = [
    # Opdracht 1: (Af)troeven
    Exercise(episode=1, alive=players1, maximum=1500, powerful=set(), earned=[]),
    # Opdracht 2: Avondklok
    Exercise(
        episode=1,
        alive=players1,
        maximum=1500,
        powerful=set(),
        earned=[
            Earning(
                money=1500,
                major={
                    Player.FRESIA_23,
                    Player.GLEN_23,
                    Player.THOMAS_23,
                    Player.ARNO_23,
                    Player.EVERON_23,
                    Player.HILA_23,
                    Player.KIM_LIAN_23,
                    Player.LAETITIA_23,
                    Player.SAHIL_23,
                    Player.SUZANNE_23,
                    Player.WELMOED_23,
                },
            ),
        ],
    ),
    # Opdracht 3: Ontmaskerd?
    Exercise(
        episode=1,
        alive=players1,
        maximum=5000,
        powerful=set(),
        earned=[
            Earning(money=-5000, major={Player.EVERON_23, Player.GLEN_23}),
        ],
    ),
]

################
# Aflevering 2
players2 = {
    Player.ARNO_23,
    Player.EVERON_23,
    Player.FRESIA_23,
    Player.GLEN_23,
    Player.HILA_23,
    Player.KIM_LIAN_23,
    Player.LAETITIA_23,
    Player.SAHIL_23,
    Player.THOMAS_23,
    Player.WELMOED_23,
}
exercises2 = [
    # Opdracht 1: Binnen en buiten bereik
    Exercise(
        episode=2,
        alive=players2,
        maximum=2500,
        powerful=set(),
        earned=[
            Earning(money=10, major={Player.FRESIA_23}),
            Earning(
                money=200,
                major={
                    Player.ARNO_23,
                    Player.EVERON_23,
                    Player.KIM_LIAN_23,
                    Player.THOMAS_23,
                    Player.LAETITIA_23,
                },
            ),
            Earning(
                money=100,
                major={
                    Player.HILA_23,
                    Player.GLEN_23,
                    Player.WELMOED_23,
                    Player.FRESIA_23,
                    Player.SAHIL_23,
                },
            ),
        ],
    ),
    # Opdracht 2: Prikactie (goud en laatste = 150, groen = 10, rood = -10)
    Exercise(
        episode=2,
        alive=players2,
        maximum=3000,
        powerful=set(),
        earned=[
            Earning(money=300, major={Player.ARNO_23}),
            Earning(money=320, major={Player.EVERON_23}),
            Earning(money=-10, major={Player.FRESIA_23}),
            Earning(money=-30, major={Player.GLEN_23}),
            Earning(money=10, major={Player.HILA_23}),
            Earning(money=50, major={Player.KIM_LIAN_23}),
            Earning(money=0, major={Player.LAETITIA_23}),
            Earning(money=10, major={Player.SAHIL_23}),
            Earning(money=-110, major={Player.THOMAS_23}),
            Earning(money=10, major={Player.WELMOED_23}),
        ],
    ),
    # Opdracht 3: Ver gelijken
    Exercise(
        episode=2,
        alive=players2,
        maximum=1800,
        powerful=set(),
        earned=[
            Earning(
                money=400,
                major={Player.HILA_23, Player.GLEN_23, Player.ARNO_23},
                minor={Player.THOMAS_23, Player.FRESIA_23},
            ),
            Earning(
                money=200,
                major={Player.SAHIL_23, Player.WELMOED_23},
                minor={Player.THOMAS_23, Player.FRESIA_23},
            ),
            Earning(
                money=200,
                major={Player.LAETITIA_23, Player.EVERON_23, Player.KIM_LIAN_23},
                minor={Player.THOMAS_23, Player.FRESIA_23},
            ),
        ],
    ),
]

################
# Aflevering 3
players3 = {
    Player.ARNO_23,
    Player.EVERON_23,
    Player.FRESIA_23,
    Player.HILA_23,
    Player.KIM_LIAN_23,
    Player.LAETITIA_23,
    Player.SAHIL_23,
    Player.THOMAS_23,
    Player.WELMOED_23,
}
exercises3 = [
    # Opdracht 1: Net of net niet
    Exercise(
        episode=3,
        alive=players3,
        maximum=7500,
        powerful=set(),
        earned=[
            Earning(money=250, major={Player.EVERON_23}),
            Earning(money=-250, major={Player.ARNO_23}),
        ],
    ),
    # Opdracht 2: Waar rook is, is vuur
    Exercise(
        episode=3,
        alive=players3,
        maximum=2000,
        powerful=set(),
        earned=[
            Earning(money=210, major={Player.THOMAS_23}),
            Earning(money=220, major={Player.LAETITIA_23}),
            Earning(money=200, major={Player.SAHIL_23}),
            Earning(money=-100, major={Player.SAHIL_23}),
            Earning(money=210, major={Player.ARNO_23}),
        ],
    ),
    # Opdracht 3: Vakbondje
    Exercise(
        episode=3,
        alive=players3,
        maximum=6000,
        powerful=set(),
        earned=[
            Earning(money=1500, major={Player.WELMOED_23}, minor={Player.KIM_LIAN_23}),
            Earning(money=-1500, major={Player.HILA_23}),
        ],
    ),
]

################
# Aflevering 4
players4 = {
    Player.ARNO_23,
    Player.EVERON_23,
    Player.FRESIA_23,
    Player.HILA_23,
    Player.KIM_LIAN_23,
    Player.LAETITIA_23,
    Player.SAHIL_23,
    Player.THOMAS_23,
}
exercises4 = [
    # Opdracht 1: Luid sprekers
    Exercise(
        episode=4,
        alive=players4,
        maximum=2000,
        powerful=set(),
        earned=[
            Earning(money=150, major={Player.KIM_LIAN_23}, minor={Player.SAHIL_23})
        ],
    ),
    # Opdracht 2: Hoog spel spelen
    Exercise(
        episode=4,
        alive=players4,
        maximum=2000,
        powerful=set(),
        earned=[
            Earning(money=250, major={Player.KIM_LIAN_23}, minor={Player.HILA_23}),
            Earning(money=250, major={Player.THOMAS_23}, minor={Player.LAETITIA_23}),
            Earning(money=250, major={Player.HILA_23}),
            Earning(money=-250, major={Player.KIM_LIAN_23}),
        ],
    ),
    # Opdracht 3: (Kamers met zoek de verschillen)
    Exercise(
        episode=4,
        alive=players4,
        maximum=2000,
        powerful=set(),
        earned=[
            Earning(money=100, major={Player.KIM_LIAN_23}, minor={Player.LAETITIA_23}),
            Earning(money=100, major={Player.LAETITIA_23}),
            Earning(money=100, major={Player.KIM_LIAN_23}),
            Earning(money=100, major={Player.FRESIA_23}),
            Earning(money=400, major={Player.EVERON_23}),
            Earning(money=200, major={Player.HILA_23}),
            Earning(money=100, major={Player.THOMAS_23}),
        ],
    ),
]

################
# Aflevering 5
players5 = {
    Player.EVERON_23,
    Player.FRESIA_23,
    Player.HILA_23,
    Player.KIM_LIAN_23,
    Player.LAETITIA_23,
    Player.SAHIL_23,
    Player.THOMAS_23,
}
exercises5 = [
    # Opdracht 1: Uit de lucht gegrepen
    Exercise(
        episode=5,
        alive=players5,
        maximum=2000,
        powerful=set(),
        earned=[
            Earning(
                money=750,
                major={Player.LAETITIA_23, Player.THOMAS_23},
                minor={Player.FRESIA_23},
            )
        ],
    ),
    # Opdracht 2: Zwanenmeer
    Exercise(
        episode=5,
        alive=players5,
        maximum=3000,
        powerful=set(),
        earned=[
            Earning(
                money=725,
                major={
                    Player.KIM_LIAN_23,
                    Player.SAHIL_23,
                    Player.LAETITIA_23,
                    Player.EVERON_23,
                    Player.HILA_23,
                    Player.FRESIA_23,
                },
            ),
            Earning(money=75, major={Player.THOMAS_23}),
        ],
    ),
    # Opdracht 3: Tijdsbeeld
    Exercise(
        episode=5,
        alive=players5,
        maximum=2000,
        powerful=set(),
        earned=[
            Earning(
                money=2000,
                major={
                    Player.EVERON_23,
                    Player.FRESIA_23,
                    Player.HILA_23,
                    Player.KIM_LIAN_23,
                    Player.LAETITIA_23,
                    Player.SAHIL_23,
                    Player.THOMAS_23,
                },
            )
        ],
    ),
]

################
# Aflevering 6
players6 = {
    Player.EVERON_23,
    Player.FRESIA_23,
    Player.KIM_LIAN_23,
    Player.LAETITIA_23,
    Player.SAHIL_23,
    Player.THOMAS_23,
}
exercises6 = [
    # Opdracht 1: In het verschiet
    Exercise(
        episode=6,
        alive=players6,
        maximum=3500,
        powerful=set(),
        earned=[
            Earning(
                money=1400,
                major={Player.KIM_LIAN_23, Player.THOMAS_23, Player.SAHIL_23},
                minor={Player.EVERON_23, Player.FRESIA_23, Player.LAETITIA_23},
            )
        ],
    ),
    # Opdracht 2: Reddingsactie
    Exercise(
        episode=6,
        alive=players6,
        maximum=1740,
        powerful=set(),
        earned=[
            Earning(
                money=1310,
                major={
                    Player.KIM_LIAN_23,
                    Player.THOMAS_23,
                    Player.SAHIL_23,
                    Player.FRESIA_23,
                    Player.LAETITIA_23,
                },
                minor={Player.EVERON_23},
            )
        ],
    ),
]

################
# Aflevering 7
players7 = {
    Player.EVERON_23,
    Player.FRESIA_23,
    Player.KIM_LIAN_23,
    Player.LAETITIA_23,
    Player.THOMAS_23,
}
exercises7 = [
    # Opdracht 1: Vakmanscha(a)p
    Exercise(
        episode=7,
        alive=players7,
        maximum=2000,
        powerful=set(),
        earned=[
            Earning(
                money=-815,
                major={
                    Player.EVERON_23,
                    Player.KIM_LIAN_23,
                    Player.THOMAS_23,
                    Player.FRESIA_23,
                    Player.LAETITIA_23,
                },
            )
        ],
    ),
    # Opdracht 2: De boot missen?
    Exercise(
        episode=7,
        alive=players7,
        maximum=1500,
        powerful=set(),
        earned=[
            Earning(money=100, major={Player.FRESIA_23}),
            Earning(money=300, major={Player.KIM_LIAN_23}),
            Earning(money=200, major={Player.LAETITIA_23}),
            Earning(money=250, major={Player.THOMAS_23}),
        ],
    ),
]

################
# Aflevering 8
players8 = {Player.EVERON_23, Player.FRESIA_23, Player.KIM_LIAN_23, Player.THOMAS_23}
exercises8 = [
    # Opdracht 1: Carpet Diem
    Exercise(
        episode=8,
        alive=players8,
        maximum=2500,
        powerful=set(),
        earned=[
            Earning(
                money=445,
                major={
                    Player.EVERON_23,
                    Player.KIM_LIAN_23,
                    Player.THOMAS_23,
                    Player.FRESIA_23,
                },
            )
        ],
    ),
    # Opdracht 2: Heftig
    Exercise(episode=8, alive=players8, maximum=1500, powerful=set(), earned=[]),
    # Opdracht 3: Zand erover
    Exercise(
        episode=8,
        alive=players8,
        maximum=2000,
        powerful=set(),
        earned=[
            Earning(
                money=500,
                major={Player.EVERON_23, Player.KIM_LIAN_23, Player.FRESIA_23},
                minor={Player.THOMAS_23},
            )
        ],
    ),
]

################
# Aflevering 9
players9 = {Player.EVERON_23, Player.FRESIA_23, Player.KIM_LIAN_23}
exercises9 = [
    # Opdracht 1: Alarmerend
    Exercise(
        episode=9,
        alive=players9,
        maximum=2000,
        powerful=set(),
        earned=[
            Earning(money=405, major={Player.EVERON_23}),
            Earning(money=565, major={Player.KIM_LIAN_23}),
        ],
    ),
    # Opdracht 2: Afrekenen
    Exercise(
        episode=9,
        alive=players9,
        maximum=2000,
        powerful=set(),
        earned=[
            Earning(money=50, major={Player.KIM_LIAN_23}),
            Earning(money=75, major={Player.EVERON_23}),
            Earning(money=50, major={Player.EVERON_23}, minor={Player.KIM_LIAN_23}),
            Earning(money=150, major={Player.FRESIA_23}),
        ],
    ),
    # Opdracht 3: Binnenskamers
    Exercise(
        episode=9,
        alive=players9,
        maximum=2000,
        powerful=set(),
        earned=[
            Earning(
                money=-1000,
                major={Player.EVERON_23, Player.KIM_LIAN_23, Player.FRESIA_23},
            )
        ],
    ),
]

season23 = Season(
    exercises1
    + exercises2
    + exercises3
    + exercises4
    + exercises5
    + exercises6
    + exercises7
    + exercises8
    + exercises9
)
