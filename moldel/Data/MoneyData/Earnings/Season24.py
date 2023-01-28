from Data.MoneyData.Dataclasses.Season import Season
from Data.MoneyData.Dataclasses.Exercise import Exercise
from Data.MoneyData.Dataclasses.Earning import Earning
from Data.Player import Player

################
# Aflevering 1
players1 = {Player.ANKE_24, Player.ANNICK_24, Player.DANIEL_24, Player.FROUKJE_24, Player.JURRE_24,
            Player.NABIL_24, Player.RANOMI_24, Player.SANDER_24, Player.SARAH_24, Player.SOY_24}
exercises1 = [
    # Opdracht 1: Gulden middenweg
    Exercise(episode=1, alive=players1, maximum=4000, earned=[
        Earning(money=500, major={Player.SARAH_24, Player.SANDER_24, Player.JURRE_24, Player.ANKE_24}),
    ]),
    # Opdracht 2: Toonaangevend
    Exercise(episode=1, alive=players1, maximum=4000, earned=[
        Earning(money=1500, major={Player.SARAH_24}, minor={Player.NABIL_24,
                Player.ANNICK_24, Player.DANIEL_24, Player.RANOMI_24, Player.FROUKJE_24}),
        Earning(money=1000, major={Player.SOY_24}, minor={Player.NABIL_24,
                Player.ANNICK_24, Player.DANIEL_24, Player.RANOMI_24, Player.FROUKJE_24}),
        Earning(money=250, major={Player.ANKE_24}, minor={Player.NABIL_24,
                Player.ANNICK_24, Player.DANIEL_24, Player.RANOMI_24, Player.FROUKJE_24}),
    ]),
]

################
# Aflevering 2
players2 = {Player.ANKE_24, Player.ANNICK_24, Player.DANIEL_24, Player.FROUKJE_24, Player.JURRE_24,
            Player.NABIL_24, Player.RANOMI_24, Player.SANDER_24, Player.SOY_24}
exercises2 = [
    # Opdracht 1: Stalen Zenuwen
    Exercise(episode=2, alive=players2, maximum=3000, earned=[
        Earning(money=1300, minor={Player.ANKE_24, Player.ANNICK_24, Player.DANIEL_24, Player.FROUKJE_24,
                Player.JURRE_24, Player.NABIL_24, Player.RANOMI_24, Player.SANDER_24, Player.SOY_24}),
    ]),
    # Opdracht 2: Propvol
    Exercise(episode=2, alive=players2, maximum=3000, earned=[
        Earning(money=250, major={Player.DANIEL_24}, minor={Player.JURRE_24,
                Player.NABIL_24, Player.ANNICK_24, Player.RANOMI_24, Player.SANDER_24}),
    ]),
]

################
# Aflevering 3
players3 = {Player.ANKE_24, Player.ANNICK_24, Player.DANIEL_24, Player.JURRE_24,
            Player.NABIL_24, Player.RANOMI_24, Player.SANDER_24, Player.SOY_24}
exercises3 = [
    # Opdracht 1: Om leiding
    Exercise(episode=3, alive=players3, maximum=2500, earned=[
        Earning(money=2500, major={Player.ANKE_24, Player.ANNICK_24, Player.DANIEL_24, Player.JURRE_24,
                                   Player.NABIL_24, Player.RANOMI_24, Player.SANDER_24, Player.SOY_24}),
    ]),
    # Opdracht 2: Per definitie
    Exercise(episode=3, alive=players3, maximum=2000, earned=[
        Earning(money=300, major={Player.JURRE_24, Player.ANNICK_24}),
        Earning(money=150, major={Player.SOY_24, Player.RANOMI_24}),
        Earning(money=100, major={Player.DANIEL_24, Player.SANDER_24}),
        Earning(money=200, major={Player.ANKE_24, Player.NABIL_24}),
    ]),
    # Opdracht 3: Schip ingaan
    Exercise(episode=3, alive=players3, maximum=2000, earned=[])
]

################
# Aflevering 4
players4 = {Player.ANKE_24, Player.ANNICK_24, Player.DANIEL_24, Player.JURRE_24,
            Player.NABIL_24, Player.RANOMI_24, Player.SOY_24}
exercises4 = [
    # Opdracht 1: Padvinden
    Exercise(episode=4, alive=players4, maximum=2000, earned=[
        Earning(money=300, major={Player.RANOMI_24}),
    ]),
    # Opdracht 2: (eend)zame hoogte
    Exercise(episode=4, alive=players4, maximum=3000, earned=[])
]

season24 = Season(
    exercises1
    + exercises2
    + exercises3
    + exercises4
)
