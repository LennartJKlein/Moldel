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
    # (250, 500, 1000, 2000, 4000)
    # anke-sander sara-jurre soy-annick sander-anke nabil-ranomi daniel-froukje
    # licht aan: sara-jurre soy-annick sander-anke nabil-ranomi daniel-froukje
    # ontsnapt: sara-jurre sander-anke daniel-froukje
    # aangekomen: sara-jurre sander-anke
    Exercise(episode=1, alive=players1, maximum=4000, earned=[
        Earning(money=500, major={Player.SARAH_24, Player.SANDER_24, Player.JURRE_24, Player.ANKE_24}),
    ]),
    # Opdracht 2: Toonaangevend
    # muzikaal oor: froukje, ranomi, daniel, nabil, annick
    # opgaan in muziek: sander, sara, jurre, anke, soy
    # 1500 op Sara
    # 1000 op jurre
    # 100 anke
    Exercise(episode=1, alive=players1, maximum=4000, earned=[
        Earning(money=1500, major={Player.SARAH_24}, minor={Player.NABIL_24,
                Player.ANNICK_24, Player.DANIEL_24, Player.RANOMI_24, Player.FROUKJE_24}),
        Earning(money=1000, major={Player.SOY_24}, minor={Player.NABIL_24,
                Player.ANNICK_24, Player.DANIEL_24, Player.RANOMI_24, Player.FROUKJE_24}),
        Earning(money=250, major={Player.ANKE_24}, minor={Player.NABIL_24,
                Player.ANNICK_24, Player.DANIEL_24, Player.RANOMI_24, Player.FROUKJE_24}),
    ]),
]

season24 = Season(
    exercises1
)
