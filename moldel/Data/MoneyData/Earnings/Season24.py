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
        Earning(money=250, major={Player.DANIEL_24}, minor={Player.FROUKJE_24, Player.JURRE_24,
                Player.NABIL_24, Player.ANNICK_24, Player.RANOMI_24, Player.SANDER_24}),
    ]),
]

season24 = Season(
    exercises1
    + exercises2
)
