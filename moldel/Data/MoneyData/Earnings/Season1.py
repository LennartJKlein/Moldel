from Data.MoneyData.Dataclasses.Season import Season
from Data.MoneyData.Dataclasses.Exercise import Exercise
from Data.MoneyData.Dataclasses.Earning import Earning
from Data.Player import Player

################
# Aflevering 1
players1 = {Player.ARNOUD_1, Player.DEBORAH_1, Player.FOKE_1, Player.JOHN_1, Player.PETRA_1, Player.ROBIN_1,
            Player.SANDY_1, Player.WARNER_1, Player.WILLY_1, Player.WILMIE_1}
exercises1 = [
    # Opdracht 1: Duiken naar woorden
    Exercise(episode=1, alive=players1, maximum=7500, earned=[
        Earning(money=7500, major={Player.DEBORAH_1, Player.PETRA_1, Player.JOHN_1, Player.FOKE_1, Player.WILLY_1}),
    ]),
    # Opdracht 2: 25km rijden
    Exercise(episode=1, alive=players1, maximum=7500, earned=[
        Earning(money=7500, major={Player.ROBIN_1, Player.WILMIE_1, Player.SANDY_1, Player.WARNER_1, Player.ARNOUD_1}),
    ]),
    # Opdracht 3: Didgeridoo
    Exercise(episode=1, alive=players1, maximum=25000, earned=[]),
]

################
# Aflevering 2
players2 = {Player.ARNOUD_1, Player.DEBORAH_1, Player.FOKE_1, Player.JOHN_1,
            Player.PETRA_1, Player.ROBIN_1, Player.WARNER_1, Player.WILLY_1, Player.WILMIE_1}
exercises2 = [
    # Opdracht 1: NL pubfeest
    Exercise(episode=2, alive=players2, maximum=0, earned=[
        # arnoud, john, foke - maken een feestje
        Earning(money=0, major={Player.ARNOUD_1, Player.JOHN_1, Player.FOKE_1})
    ]),
    # Opdracht 2: Quiz met gevaarkijke dieren
    Exercise(episode=2, alive=players2, maximum=5000, earned=[
        Earning(money=500, major={Player.WILLY_1}), # krokodil
        Earning(money=500, major={Player.WILLY_1}), # krokodil
        Earning(money=500, major={Player.PETRA_1}, minor={Player.WILLY_1}), # abel tasman
        Earning(money=500, major={Player.PETRA_1}, minor={Player.WILLY_1}), # camberra
        Earning(money=500, major={Player.PETRA_1}, minor={Player.WILLY_1}), # thomas cook
        Earning(money=500, major={Player.WARNER_1}), # haaien
        Earning(money=500, major={Player.WARNER_1}), # haaien
        Earning(money=500, major={Player.WARNER_1}), # haaien
        Earning(money=500, major={Player.DEBORAH_1}, minor={Player.WARNER_1}), # noorden
        Earning(money=500, major={Player.WARNER_1}), # haaien
    ]),
    # Opdracht 3: 
    Exercise(episode=2, alive=players2, maximum=0, earned=[]),
]

season1 = Season(
    exercises1 + exercises2 + exercises3 + exercises4 + exercises5 + exercises6 + exercises7
)
