from Data.ExerciseData.Dataclasses.Season import Season
from Data.ExerciseData.Dataclasses.Exercise import Exercise
from Data.ExerciseData.Dataclasses.Earning import Earning
from Data.Player import Player

# Aflevering 1
# Opdracht 1 (Maximaal €2000): Niks verdiend
# Opdracht 2 (Maximaal €2000): Niks verdiend
alive1 = {
    Player.AJOUAD_15,
    Player.CAROLINA_15,
    Player.CHRIS_15,
    Player.EVELIEN_15,
    Player.MARGRIET_15,
    Player.MARLIJN_15,
    Player.MARTINE_15,
    Player.PIETER_15,
    Player.RIK_15,
    Player.VIKTOR_15,
}
exercise1_1 = Exercise(
    episode=1, alive=alive1, maximum=2000, powerful=set(), earned=[]
)
exercise1_2 = Exercise(
    episode=1, alive=alive1, maximum=2000, powerful=set(), earned=[]
)

# Aflevering 2
# Opdracht 1 (Maximaal €2000):
# -€100 (Major: Chris), -€100 (Major: Marlijn), -€100 (Major: Viktor), -€100 (Major: Margriet), -€100 (Major: Marlijn),
# -€100 (Major: Evelien), -€100 (Major: Carolina), -€100 (Major: Chris), €900 (Minor: Allen)
# Opdracht 2 (Maximaal €1500):
# €500 (Major: Ajouad, Evelien) (Minor: Carolina), €500 (Major: Margriet, Rik) (Minor: Marlijn),
# €500 (Major: Chris, Viktor) (Minor: Martine)
# Opdracht 3 (Maximaal €1500): Gezamelijk verdiend
# Daarnaast: -€200 ingeleverd door Margriet (en deels Martine)
alive2 = {
    Player.AJOUAD_15,
    Player.CAROLINA_15,
    Player.CHRIS_15,
    Player.EVELIEN_15,
    Player.MARGRIET_15,
    Player.MARLIJN_15,
    Player.MARTINE_15,
    Player.RIK_15,
    Player.VIKTOR_15,
}
exercise2_1 = Exercise(
    episode=2,
    alive=alive2,
    maximum=2000,
    powerful=set(),
    earned=[
        Earning(
            money=900,
            minor={
                Player.AJOUAD_15,
                Player.CAROLINA_15,
                Player.CHRIS_15,
                Player.EVELIEN_15,
                Player.MARGRIET_15,
                Player.MARLIJN_15,
                Player.MARTINE_15,
                Player.RIK_15,
                Player.VIKTOR_15,
            },
        ),
        Earning(money=-200, major={Player.CHRIS_15}),
        Earning(money=-200, major={Player.MARLIJN_15}),
        Earning(money=-100, major={Player.VIKTOR_15}),
        Earning(money=-100, major={Player.MARGRIET_15}),
        Earning(money=-100, major={Player.EVELIEN_15}),
        Earning(money=-100, major={Player.CAROLINA_15}),
    ],
)
exercise2_2 = Exercise(
    episode=2,
    alive=alive2,
    maximum=1500,
    powerful=set(),
    earned=[
        Earning(
            money=500,
            major={Player.AJOUAD_15, Player.EVELIEN_15},
            minor={Player.CAROLINA_15},
        ),
        Earning(
            money=500,
            major={Player.MARGRIET_15, Player.RIK_15},
            minor={Player.MARLIJN_15},
        ),
        Earning(
            money=500,
            major={Player.CHRIS_15, Player.VIKTOR_15},
            minor={Player.MARTINE_15},
        ),
    ],
)
exercise2_3 = Exercise(
    episode=2, alive=alive2, maximum=1500, powerful=set(), earned=[]
)
exercise2_4 = Exercise(
    episode=2,
    alive=alive2,
    maximum=None,
    powerful=set(),
    earned=[
        Earning(money=-200, major={Player.MARGRIET_15}, minor={Player.MARTINE_15}),
    ],
)

# Aflevering 3
# Opdracht 1 (Maximaal €3000):
# €100 (Major: Viktor)
# Opdracht 2 (Maximaal €?): Niks verdiend
alive3 = {
    Player.AJOUAD_15,
    Player.CAROLINA_15,
    Player.CHRIS_15,
    Player.MARGRIET_15,
    Player.MARLIJN_15,
    Player.MARTINE_15,
    Player.RIK_15,
    Player.VIKTOR_15,
}
exercise3_1 = Exercise(
    episode=3,
    alive=alive3,
    maximum=3000,
    powerful=set(),
    earned=[Earning(money=100, major={Player.VIKTOR_15})],
)

# Aflevering 4
# Opdracht 1 (Maximaal €1750):
# €250 (Major: Marlijn) (Minor: Viktor), €250 (Major: Chris) (Minor: Ajouad, Martine),
# €250 (Major: Martine) (Minor: Chris, Margriet, Rik)
# Opdracht 2 (Maximaal €?):
# €500 (Major: Marlijn), €250 (Major: Chris)
# Opdracht 3 (Maximaal €2000): Niks verdiend
alive4 = {
    Player.AJOUAD_15,
    Player.CAROLINA_15,
    Player.CHRIS_15,
    Player.MARGRIET_15,
    Player.MARLIJN_15,
    Player.MARTINE_15,
    Player.RIK_15,
    Player.VIKTOR_15,
}
exercise4_1 = Exercise(
    episode=4,
    alive=alive4,
    maximum=1750,
    powerful=set(),
    earned=[
        Earning(money=250, major={Player.MARLIJN_15}, minor={Player.VIKTOR_15}),
        Earning(
            money=250,
            major={
                Player.CHRIS_15,
            },
            minor={Player.AJOUAD_15, Player.MARTINE_15},
        ),
        Earning(
            money=250,
            major={Player.MARTINE_15},
            minor={Player.CHRIS_15, Player.MARGRIET_15, Player.RIK_15},
        ),
    ],
)
exercise4_2 = Exercise(
    episode=4,
    alive=alive4,
    maximum=None,
    powerful=set(),
    earned=[
        Earning(money=500, major={Player.MARLIJN_15}),
        Earning(money=250, major={Player.CHRIS_15}),
    ],
)
exercise4_3 = Exercise(
    episode=4, alive=alive4, maximum=2000, powerful=set(), earned=[]
)

# Aflevering 5
# Opdracht 1 (Maximaal €?): Niks verdiend
# Opdracht 2 (Maximaal €?): Niks verdiend
# Opdracht 3 (Maximaal €2000):
# Carolina + Viktor (2x in Geldrop), Martine + Marlijn (1x in Geldrop)
# €1000 (Major: Carolina, Viktor) (Minor: Chris), €500 (Major: Marlijn, Martine) (Minor: Chris)
alive5 = {
    Player.CAROLINA_15,
    Player.CHRIS_15,
    Player.MARGRIET_15,
    Player.MARLIJN_15,
    Player.MARTINE_15,
    Player.RIK_15,
    Player.VIKTOR_15,
}
exercise5_3 = Exercise(
    episode=5,
    alive=alive5,
    maximum=2000,
    powerful=set(),
    earned=[
        Earning(
            money=1000,
            major={Player.CAROLINA_15, Player.VIKTOR_15},
            minor={Player.CHRIS_15},
        ),
        Earning(
            money=500,
            major={Player.MARLIJN_15, Player.MARTINE_15},
            minor={Player.CHRIS_15},
        ),
    ],
)

# Aflevering 6
# Opdracht 1 (Maximaal €1987): Niks verdiend
# Opdracht 2 (Maximaal €?):
# Opgraven:
# Chris & Carolina (2x), Rik & Marlijn (1x), Martine (1x), Rik (1x), Martine (1x), Carolina & Martine (1x),
# Margriet & Martine (1x), Niet gezien (3x)
# Ingeleverd:
# Martine (2x), Margriet (1x), Rik (1x), Carolina (5x), Chris (2x)
# €1250 gezamelijk verdiend
# Daarnaast: -€750 ingeleverd door Marlijn & Rik
alive6 = {
    Player.CAROLINA_15,
    Player.CHRIS_15,
    Player.MARGRIET_15,
    Player.MARLIJN_15,
    Player.MARTINE_15,
    Player.RIK_15,
}
exercise6_1 = Exercise(
    episode=6, alive=alive6, maximum=1987, powerful=set(), earned=[]
)
exercise6_2 = Exercise(
    episode=6,
    alive=alive6,
    maximum=None,
    powerful=set(),
    earned=[
        Earning(money=1250 * 2 / 11, minor={Player.MARTINE_15}),
        Earning(money=1250 * 1 / 11, minor={Player.MARGRIET_15}),
        Earning(money=1250 * 1 / 11, minor={Player.RIK_15}),
        Earning(money=1250 * 5 / 11, minor={Player.CAROLINA_15}),
        Earning(money=1250 * 2 / 11, minor={Player.CHRIS_15}),
    ],
)
exercise6_3 = Exercise(
    episode=6,
    alive=alive6,
    maximum=None,
    powerful=set(),
    earned=[
        Earning(money=-750, major={Player.MARLIJN_15, Player.RIK_15}),
    ],
)

# Aflevering 7
# Opdracht 1 (Maximaal €1000): Niks verdiend
# Opdracht 2 (Maximaal €2000): Onduidelijk wie wat verdiend heeft
# Daarnaast: -€750 ingeleverd door Rik
alive7 = {
    Player.CHRIS_15,
    Player.MARGRIET_15,
    Player.MARLIJN_15,
    Player.MARTINE_15,
    Player.RIK_15,
}
exercise7_1 = Exercise(
    episode=7, alive=alive7, maximum=1000, powerful=set(), earned=[]
)
exercise7_2 = Exercise(
    episode=7, alive=alive7, maximum=2000, powerful=set(), earned=[]
)
exercise7_3 = Exercise(
    episode=7,
    alive=alive7,
    maximum=None,
    powerful=set(),
    earned=[
        Earning(money=-750, major={Player.RIK_15}),
    ],
)

# Aflevering 8
# Opdracht 1 (Maximaal €1851): Niks verdiend
# Opdracht 2 (Maximaal €1500):
# €1500 (Major: Martine) (Minor: Chris, Margriet, Rik)
# Opdracht 3 (Maximaal €2500):
# €500 (Major: Margriet), €250 (Major: Chris)
alive8 = {
    Player.CHRIS_15,
    Player.MARGRIET_15,
    Player.MARLIJN_15,
    Player.MARTINE_15,
    Player.RIK_15,
}
exercise8_1 = Exercise(
    episode=8, alive=alive8, maximum=1851, powerful=set(), earned=[]
)
exercise8_2 = Exercise(
    episode=8,
    alive=alive8,
    maximum=1500,
    powerful=set(),
    earned=[
        Earning(
            money=1500,
            major={Player.MARTINE_15},
            minor={Player.CHRIS_15, Player.MARGRIET_15, Player.RIK_15},
        ),
    ],
)
exercise8_3 = Exercise(
    episode=8,
    alive=alive8,
    maximum=2500,
    powerful=set(),
    earned=[
        Earning(money=500, major={Player.MARGRIET_15}),
        Earning(money=250, major={Player.CHRIS_15}),
    ],
)

# Aflevering 9
# Opdracht 1 (Maximaal €1000):
# €500 (Major: Marlijn)
# Opdracht 2 (Maximaal €1500): Niks verdiend
alive9f = {Player.CHRIS_15, Player.MARGRIET_15, Player.MARLIJN_15, Player.RIK_15}
alive9s = {Player.MARGRIET_15, Player.MARLIJN_15, Player.RIK_15}
exercise9_1 = Exercise(
    episode=9,
    alive=alive9f,
    maximum=1000,
    powerful=set(),
    earned=[Earning(money=500, major={Player.MARLIJN_15})],
)
exercise9_2 = Exercise(
    episode=9, alive=alive9s, maximum=1500, powerful=set(), earned=[]
)

season15 = Season(
    [
        exercise1_1,
        exercise1_2,
        exercise2_1,
        exercise2_2,
        exercise2_3,
        exercise2_4,
        exercise3_1,
        exercise4_1,
        exercise4_2,
        exercise4_3,
        exercise5_3,
        exercise6_1,
        exercise6_2,
        exercise6_3,
        exercise7_1,
        exercise7_2,
        exercise7_3,
        exercise8_1,
        exercise8_2,
        exercise8_3,
        exercise9_1,
        exercise9_2,
    ]
)
