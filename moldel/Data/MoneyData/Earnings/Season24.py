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
        # Glansgans: 0 euro
        # Suurstofdieffies: 50 euro
        Earning(money=50, major={Player.JURRE_24, Player.ANNICK_24}),
        # Blerkas: 2 x 50 euro
        Earning(money=100, major={Player.JURRE_24, Player.ANNICK_24, Player.SOY_24, Player.RANOMI_24}),
        # Windpompsherry: ? euro
        Earning(money=50),
        # Skeletklets: 3 x 50 euro
        Earning(money=100, major={Player.DANIEL_24, Player.SANDER_24, Player.SOY_24, Player.RANOMI_24}),
        Earning(money=50),
        # Gelytydigheidsafrigter: 50 euro
        Earning(money=50, major={Player.JURRE_24, Player.ANNICK_24}),
        # Inklimgordel: 50 euro
        Earning(money=50, major={Player.ANKE_24, Player.NABIL_24}),
        # Patpredikant: ? euro
        Earning(money=200),
        # Begrafenispote: 2 x 50 euro
        Earning(money=100, major={Player.JURRE_24, Player.ANNICK_24, Player.ANKE_24, Player.NABIL_24}),
        # Molafspraak: 0 euro
    ]),
    # Opdracht 3: Schip ingaan
    Exercise(episode=3, alive=players3, maximum=2000, earned=[])
]

season24 = Season(
    exercises1
    + exercises2
    + exercises3
)
