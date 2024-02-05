from Data.ExerciseData.Dataclasses.Season import Season
from Data.ExerciseData.Dataclasses.Exercise import Exercise
from Data.ExerciseData.Dataclasses.Earning import Earning
from Data.Player import Player

# Aflevering 1
# Opdracht 1 (Maximaal €1000): Gezamelijk verdiend
# Opdracht 2 (Maximaal €2000): Niks verdiend
alive1 = {
    Player.AIREN_16,
    Player.ANNEMIEKE_16,
    Player.CECILE_16,
    Player.ELLIE_16,
    Player.KLAAS_16,
    Player.MARJOLEIN_16,
    Player.REMY_16,
    Player.ROP_16,
    Player.TAEKE_16,
    Player.TIM_16,
}
exercise1_1 = Exercise(
    episode=1, alive=alive1, maximum=1000, powerful=set(), earned=[]
)
exercise1_2 = Exercise(
    episode=1, alive=alive1, maximum=2000, powerful=set(), earned=[]
)

# Aflevering 2
# Opdracht 1 (Maximaal €2000): Niks verdiend
# Opdracht 2 (Maximaal €2000): 1e goed, 2e goed, 3e fout, 4e fout, 5e fout, 6e fout, 7e fout, 8e goed, 9e goed (All)
# €100 (Major: Airen, Cecile, Tim) (Minor: Marjolein), €100 (Major: Airen, Cecile, Tim) (Minor: Marjolein),
# €100 (Major: Klaas, Rop, Taeke) (Minor: Marjolein), €100 (Minor: Rest)
# Opdracht 3 (Maximaal €0): Niks verdiend
alive2 = {
    Player.AIREN_16,
    Player.ANNEMIEKE_16,
    Player.CECILE_16,
    Player.ELLIE_16,
    Player.KLAAS_16,
    Player.MARJOLEIN_16,
    Player.REMY_16,
    Player.ROP_16,
    Player.TAEKE_16,
    Player.TIM_16,
}
exercise2_1 = Exercise(
    episode=2, alive=alive2, maximum=2000, powerful=set(), earned=[]
)
exercise2_2 = Exercise(
    episode=2,
    alive=alive2,
    maximum=2000,
    powerful=set(),
    earned=[
        Earning(
            money=200,
            major={Player.AIREN_16, Player.CECILE_16, Player.TIM_16},
            minor={Player.MARJOLEIN_16},
        ),
        Earning(
            money=100,
            major={Player.KLAAS_16, Player.ROP_16, Player.TAEKE_16},
            minor={Player.MARJOLEIN_16},
        ),
        Earning(
            money=100,
            minor={
                Player.AIREN_16,
                Player.ANNEMIEKE_16,
                Player.CECILE_16,
                Player.ELLIE_16,
                Player.KLAAS_16,
                Player.MARJOLEIN_16,
                Player.REMY_16,
                Player.ROP_16,
                Player.TAEKE_16,
                Player.TIM_16,
            },
        ),
    ],
)

# Aflevering 3
# Opdracht 1 (Maximaal €1750):
# €500 (Major: Annemieke) (Minor: Taeke), €250 (Major: Klaas, Tim)
# Opdracht 2 (Maximaal €3000):
# €200 (Major: Klaas), €1000 (Major: Taeke), €400 (Major: Ellie, Remy), €100 (Major: Cecille)
# Opdracht 3 (Maximaal €0):
# -€2345 (Minor: Annemieke, Cecile, Ellie, Klaas, Marjolein, Rop, Taeke, Tim)
alive3 = {
    Player.ANNEMIEKE_16,
    Player.CECILE_16,
    Player.ELLIE_16,
    Player.KLAAS_16,
    Player.MARJOLEIN_16,
    Player.REMY_16,
    Player.ROP_16,
    Player.TAEKE_16,
    Player.TIM_16,
}
exercise3_1 = Exercise(
    episode=3,
    alive=alive3,
    maximum=1750,
    powerful=set(),
    earned=[
        Earning(money=500, major={Player.ANNEMIEKE_16}, minor={Player.TAEKE_16}),
        Earning(money=250, major={Player.KLAAS_16, Player.TIM_16}),
    ],
)
exercise3_2 = Exercise(
    episode=3,
    alive=alive3,
    maximum=3000,
    powerful=set(),
    earned=[
        Earning(money=200, major={Player.KLAAS_16}),
        Earning(money=1000, major={Player.TAEKE_16}),
        Earning(money=400, major={Player.ELLIE_16, Player.REMY_16}),
        Earning(money=100, major={Player.CECILE_16}),
    ],
)
exercise3_3 = Exercise(
    episode=3,
    alive=alive3,
    maximum=None,
    powerful=set(),
    earned=[
        Earning(
            money=-2345,
            minor={
                Player.ANNEMIEKE_16,
                Player.CECILE_16,
                Player.ELLIE_16,
                Player.KLAAS_16,
                Player.MARJOLEIN_16,
                Player.ROP_16,
                Player.TAEKE_16,
                Player.TIM_16,
            },
        ),
    ],
)

# Aflevering 4
# Opdracht 1 (Maximaal €?):
# Rob (2 kokers) (Minor: Klaas), Ellie (2 kokers) (Minor: Klaas), Annemieke (1 koker), Marjolein (1 koker) (€1000 samen)
# Opdracht 2 (Maximaal €4010):
# -€500 (Major: Annemieke), €500 (Major: Marjolein)
# Opdracht 3 (Maximaal €1500):
# €1500 (Major: Ellie) (Minor: Taeke)
alive4 = {
    Player.ANNEMIEKE_16,
    Player.CECILE_16,
    Player.ELLIE_16,
    Player.KLAAS_16,
    Player.MARJOLEIN_16,
    Player.ROP_16,
    Player.TAEKE_16,
    Player.TIM_16,
}
exercise4_1 = Exercise(
    episode=4,
    alive=alive4,
    maximum=None,
    powerful=set(),
    earned=[
        Earning(money=1000 * 2 / 6, major={Player.ROP_16}, minor={Player.KLAAS_16}),
        Earning(money=1000 * 2 / 6, major={Player.ELLIE_16}, minor={Player.KLAAS_16}),
        Earning(money=1000 * 1 / 6, major={Player.ANNEMIEKE_16}),
        Earning(money=1000 * 1 / 6, major={Player.MARJOLEIN_16}),
    ],
)
exercise4_2 = Exercise(
    episode=4,
    alive=alive4,
    maximum=4010,
    powerful=set(),
    earned=[
        Earning(money=-500, major={Player.ANNEMIEKE_16}),
        Earning(money=500, major={Player.MARJOLEIN_16}),
    ],
)
exercise4_3 = Exercise(
    episode=4,
    alive=alive4,
    maximum=1500,
    powerful=set(),
    earned=[Earning(money=1500, major={Player.ELLIE_16}, minor={Player.TAEKE_16})],
)

# Aflevering 5
# Opdracht 1 (Maximaal €2400):
# €200 (Major: Rop) (Minor: Klaas, Taeke), €200 (Major: Annemieke) (Minor: Taeke, Tim),
# €200 (Major: Klaas) (Minor: Taeke, Tim)
# Opdracht 2 (Maximaal €1000): Gezamelijk verdiend
# Opdracht 3 (Maximaal €1000): Niks verdiend
alive5 = {
    Player.ANNEMIEKE_16,
    Player.CECILE_16,
    Player.KLAAS_16,
    Player.MARJOLEIN_16,
    Player.ROP_16,
    Player.TAEKE_16,
    Player.TIM_16,
}
exercise5_1 = Exercise(
    episode=5,
    alive=alive5,
    maximum=2400,
    powerful=set(),
    earned=[
        Earning(
            money=200, major={Player.ROP_16}, minor={Player.KLAAS_16, Player.TAEKE_16}
        ),
        Earning(
            money=200,
            major={Player.ANNEMIEKE_16},
            minor={Player.TAEKE_16, Player.TIM_16},
        ),
        Earning(
            money=200, major={Player.KLAAS_16}, minor={Player.TAEKE_16, Player.TIM_16}
        ),
    ],
)
exercise5_2 = Exercise(
    episode=5, alive=alive5, maximum=1000, powerful=set(), earned=[]
)
exercise5_3 = Exercise(
    episode=5, alive=alive5, maximum=1000, powerful=set(), earned=[]
)

# Aflevering 6
# Opdracht 1 (Maximaal €1500): Niks verdiend
# Opdracht 2 (Maximaal €1000):
# Annemieke (Bandera, Ermana, Jessezeist),
# €100 (Major: Annemieke) (Minor: Klaas, Rop, Taeke), €100 (Major: Annemieke) (Minor: Klaas, Rop, Taeke),
# €100 (Major: Annemieke), €100 (Major: Rop) (Minor: Annemieke, Cecile, Tim)
# Opdracht 3 (Maximaal €2000): Niks verdiend
alive6 = {
    Player.ANNEMIEKE_16,
    Player.CECILE_16,
    Player.KLAAS_16,
    Player.ROP_16,
    Player.TAEKE_16,
    Player.TIM_16,
}
exercise6_1 = Exercise(
    episode=6, alive=alive6, maximum=1500, powerful=set(), earned=[]
)
exercise6_2 = Exercise(
    episode=6,
    alive=alive6,
    maximum=1000,
    powerful=set(),
    earned=[
        Earning(
            money=200,
            major={Player.ANNEMIEKE_16},
            minor={Player.KLAAS_16, Player.ROP_16, Player.TAEKE_16},
        ),
        Earning(money=100, major={Player.ANNEMIEKE_16}),
        Earning(
            money=100,
            major={Player.ROP_16},
            minor={Player.ANNEMIEKE_16, Player.CECILE_16, Player.TIM_16},
        ),
    ],
)
exercise6_3 = Exercise(
    episode=6, alive=alive6, maximum=2000, powerful=set(), earned=[]
)

# Aflevering 7
# Opdracht 1 (Maximaal €1500):
# €300 (Major: Tim) (Minor: Annemieke)
# Opdracht 2 (Maximaal €1000):
# -€250 (Major: Annemieke), -€750 (Major: Taeke)
# Opdracht 3 (Maximaal €?): Gezamelijk verdiend
alive7 = {
    Player.ANNEMIEKE_16,
    Player.KLAAS_16,
    Player.ROP_16,
    Player.TAEKE_16,
    Player.TIM_16,
}
exercise7_1 = Exercise(
    episode=7,
    alive=alive7,
    maximum=1500,
    powerful=set(),
    earned=[
        Earning(money=300, major={Player.TIM_16}, minor={Player.ANNEMIEKE_16}),
    ],
)
exercise7_2 = Exercise(
    episode=7,
    alive=alive7,
    maximum=1000,
    powerful=set(),
    earned=[
        Earning(money=-250, major={Player.ANNEMIEKE_16}),
        Earning(money=-750, major={Player.TAEKE_16}),
    ],
)

# Aflevering 8
# Opdracht 1 (Maximaal €2000):
# €2000 (Major: Taeke, Tim) (Minor: Annemieke, Klaas)
# Opdracht 2 (Maximaal €4500):
# 9 klokken (Tellen -€1000 eraf)
# €18 (Major: Annemieke), €407 (Major: Taeke), €184 (Major: Annemieke), €460 (Major: Taeke),
# -€13 (Major: Taeke, Tim) (Minor: Annemieke, Klaas), €490 (Major: Taeke), €532 (Major: Taeke),
# €568 (Major: Taeke), €49 (Major: Taeke)
# Opdracht 3 (Maximaal €1250):
# €1000 (Major: Annemieke) (Minor: Klaas, Taeke, Tim)
alive8 = {Player.ANNEMIEKE_16, Player.KLAAS_16, Player.TAEKE_16, Player.TIM_16}
exercise8_1 = Exercise(
    episode=8,
    alive=alive8,
    maximum=2000,
    powerful=set(),
    earned=[
        Earning(
            money=2000,
            major={Player.TAEKE_16, Player.TIM_16},
            minor={Player.ANNEMIEKE_16, Player.KLAAS_16},
        ),
    ],
)
exercise8_2 = Exercise(
    episode=8,
    alive=alive8,
    maximum=4500,
    powerful=set(),
    earned=[
        Earning(money=202, major={Player.ANNEMIEKE_16}),
        Earning(money=2506, major={Player.TAEKE_16}),
        Earning(
            money=-13,
            major={Player.TAEKE_16, Player.TIM_16},
            minor={Player.ANNEMIEKE_16, Player.KLAAS_16},
        ),
    ],
)
exercise8_3 = Exercise(
    episode=8,
    alive=alive8,
    maximum=1250,
    powerful=set(),
    earned=[
        Earning(
            money=1000,
            major={Player.ANNEMIEKE_16},
            minor={Player.KLAAS_16, Player.TAEKE_16, Player.TIM_16},
        )
    ],
)

# Aflevering 9
# Opdracht 1 (Maximaal €1500): Gezamelijk verdiend
# Opdracht 2 (Maximaal €?): Gezamelijk verdiend
alive9 = {Player.ANNEMIEKE_16, Player.KLAAS_16, Player.TIM_16}
exercise9_1 = Exercise(
    episode=9, alive=alive9, maximum=1500, powerful=set(), earned=[]
)

season16 = Season(
    [
        exercise1_1,
        exercise1_2,
        exercise2_1,
        exercise2_2,
        exercise3_1,
        exercise3_2,
        exercise3_3,
        exercise4_1,
        exercise4_2,
        exercise4_3,
        exercise5_1,
        exercise5_2,
        exercise5_3,
        exercise6_1,
        exercise6_2,
        exercise6_3,
        exercise7_1,
        exercise7_2,
        exercise8_1,
        exercise8_2,
        exercise8_3,
        exercise9_1,
    ]
)
