from Data.MoneyData.Dataclasses.Season import Season
from Data.MoneyData.Dataclasses.Exercise import Exercise
from Data.MoneyData.Dataclasses.Earning import Earning
from Data.Player import Player

################
# Aflevering 1
players1 = {Player.ARNO_23, Player.EVERON_23, Player.FRESIA_23, Player.GLEN_23, Player.HILA_23, Player.KIM_LIAN_23, Player.LAETITIA_23, Player.SAHIL_23, Player.SUZANNE_23, Player.THOMAS_23, Player.WELMOED_23}
exercises1 = [
    # Opdracht 1: (Af)troeven
    Exercise(episode = 1, alive = players1, maximum = 1500, earned = []),
    # Opdracht 2: Avondklok
    Exercise(episode = 1, alive = players1, maximum = 1500, earned = [
        Earning(money = 1500, major = {Player.FRESIA_23, Player.GLEN_23, Player.THOMAS_23, Player.ARNO_23, Player.EVERON_23, Player.HILA_23, Player.KIM_LIAN_23, Player.LAETITIA_23, Player.SAHIL_23, Player.SUZANNE_23, Player.WELMOED_23}),
    ]),
    # Opdracht 3: Ontmaskerd?
    Exercise(episode = 1, alive = players1, maximum = 5000, earned = [
        # Wordt pas bekend gemaakt in slotaflevering
    ])
]

################
# Aflevering 2
players2 = {Player.ARNO_23, Player.EVERON_23, Player.FRESIA_23, Player.GLEN_23, Player.HILA_23, Player.KIM_LIAN_23, Player.LAETITIA_23, Player.SAHIL_23, Player.THOMAS_23, Player.WELMOED_23}
exercises2 = [
    # Opdracht 1: Binnen en buiten bereik
    Exercise(episode = 2, alive = players2, maximum = 2500, earned = [
        Earning(money = 10, major = {Player.FRESIA_23}),
        Earning(money = 200, major = {Player.ARNO_23, Player.EVERON_23, Player.KIM_LIAN_23, Player.THOMAS_23, Player.LAETITIA_23}),
        Earning(money = 100, major = {Player.HILA_23, Player.GLEN_23, Player.WELMOED_23, Player.FRESIA_23, Player.SAHIL_23})
    ]),
    # Opdracht 2: Prikactie (goud en laatste = 150, groen = 10, rood = -10)
    Exercise(episode = 2, alive = players2, maximum = 3000, earned = [
        Earning(money = 300, major = {Player.ARNO_23}),
        Earning(money = 320, major = {Player.EVERON_23}),
        Earning(money = -10, major = {Player.FRESIA_23}),
        Earning(money = -30, major = {Player.GLEN_23}),
        Earning(money = 10, major = {Player.HILA_23}),
        Earning(money = 50, major = {Player.KIM_LIAN_23}),
        Earning(money = 0, major = {Player.LAETITIA_23}),
        Earning(money = 10, major = {Player.SAHIL_23}),
        Earning(money = -110, major = {Player.THOMAS_23}),
        Earning(money = 10, major = {Player.WELMOED_23}),
    ]),
    # Opdracht 3: Ver gelijken
    Exercise(episode = 2, alive = players2, maximum = 1800, earned = [
        Earning(money = 400, major = {Player.HILA_23, Player.GLEN_23, Player.ARNO_23}, minor = {Player.THOMAS_23, Player.FRESIA_23}),
        Earning(money = 200, major = {Player.SAHIL_23, Player.WELMOED_23}, minor = {Player.THOMAS_23, Player.FRESIA_23}),
        Earning(money = 200, major = {Player.LAETITIA_23, Player.EVERON_23, Player.KIM_LIAN_23}, minor = {Player.THOMAS_23, Player.FRESIA_23})
    ])
]

################
# Aflevering 3
players3 = {Player.ARNO_23, Player.EVERON_23, Player.FRESIA_23, Player.HILA_23, Player.KIM_LIAN_23, Player.LAETITIA_23, Player.SAHIL_23, Player.THOMAS_23, Player.WELMOED_23}
exercises3 = [
    # Opdracht 1: Net of net niet
    Exercise(episode = 3, alive = players3, maximum = 7500, earned = [
        Earning(money = 250, major = {Player.EVERON_23}),
        Earning(money = -250, major = {Player.ARNO_23})
    ]),
    # Opdracht 2: Waar rook is, is vuur
    Exercise(episode = 3, alive = players3, maximum = 2000, earned = [
        Earning(money = 210, major = {Player.THOMAS_23}),
        Earning(money = 220, major = {Player.LAETITIA_23}),
        Earning(money = 200, major = {Player.SAHIL_23}),
        Earning(money = -100, major = {Player.SAHIL_23}),
        Earning(money = 210, major = {Player.ARNO_23})
    ]),
    # Opdracht 3: Vakbondje
    Exercise(episode = 3, alive = players3, maximum = 6000, earned = [
        Earning(money = 1500, major = {Player.WELMOED_23}, minor = {Player.KIM_LIAN_23}),
        Earning(money = -1500, major = {Player.HILA_23})
    ])
]

season23 = Season(
    exercises1 + exercises2 + exercises3
)