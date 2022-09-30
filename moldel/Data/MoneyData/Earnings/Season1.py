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
    Exercise(episode=1, alive=players1, maximum=25000, earned=[])
]

################
# Aflevering 2
players2 = {Player.ARNOUD_1, Player.DEBORAH_1, Player.FOKE_1, Player.JOHN_1,
            Player.PETRA_1, Player.ROBIN_1, Player.WARNER_1, Player.WILLY_1, Player.WILMIE_1}
exercises2 = [
    # Opdracht 1: NL pubfeest (arnoud, john, foke)
    Exercise(episode=2, alive=players2, maximum=5000, earned=[]),
    # Opdracht 2: Quiz met gevaarlijke dieren
    Exercise(episode=2, alive=players2, maximum=5000, earned=[
        Earning(money=500, major={Player.WILLY_1}),  # antwoord 1
        Earning(money=500, major={Player.WILLY_1}),  # antwoord 2
        Earning(money=500, major={Player.PETRA_1}, minor={Player.WILLY_1}),  # antwoord 3
        Earning(money=500, major={Player.PETRA_1}, minor={Player.WILLY_1}),  # antwoord 4
        Earning(money=500, major={Player.PETRA_1}, minor={Player.WILLY_1}),  # antwoord 5
        Earning(money=500, major={Player.WARNER_1}),  # antwoord 1
        Earning(money=500, major={Player.WARNER_1}),  # antwoord 2
        Earning(money=500, major={Player.WARNER_1}),  # antwoord 3
        Earning(money=500, major={Player.DEBORAH_1}, minor={Player.WARNER_1}),  # antwoord 4
        Earning(money=500, major={Player.WARNER_1}),  # antwoord 5
    ]),
    # Opdracht 3: Raften
    Exercise(episode=2, alive=players2, maximum=5000, earned=[])
]

################
# Aflevering 3
players3 = {Player.ARNOUD_1, Player.DEBORAH_1, Player.FOKE_1, Player.JOHN_1,
            Player.PETRA_1, Player.ROBIN_1, Player.WARNER_1, Player.WILMIE_1}
exercises3 = [
    # Opdracht 1: Onbewoond eiland
    Exercise(episode=3, alive=players3, maximum=10000, earned=[]),
    # Opdracht 2: Vleesproeverij
    Exercise(episode=3, alive=players3, maximum=5000, earned=[]),
    # Opdracht 3: Bungeejumpen
    Exercise(episode=3, alive=players3, maximum=15000, earned=[
        Earning(money=15000, major={Player.ARNOUD_1, Player.DEBORAH_1, Player.FOKE_1,
                Player.JOHN_1, Player.PETRA_1, Player.ROBIN_1, Player.WARNER_1, Player.WILMIE_1}),
    ])
]

################
# Aflevering 4
players4 = {Player.ARNOUD_1, Player.DEBORAH_1, Player.FOKE_1,
            Player.PETRA_1, Player.ROBIN_1, Player.WARNER_1, Player.WILMIE_1}
exercises4 = [
    # Opdracht 1: Doolhof
    Exercise(episode=4, alive=players4, maximum=7500, earned=[
        Earning(money=7500, major={Player.ARNOUD_1, Player.WILMIE_1}),
    ]),
    # Opdracht 2: Whale watching
    Exercise(episode=4, alive=players4, maximum=5000, earned=[]),
    # Opdracht 3: Kampioenen
    Exercise(episode=4, alive=players4, maximum=5000, earned=[])
]

################
# Aflevering 5
players5 = {Player.ARNOUD_1, Player.DEBORAH_1, Player.FOKE_1, Player.PETRA_1, Player.ROBIN_1, Player.WILMIE_1}
exercises5 = [
    # Opdracht 1: Vlagtikkertje
    Exercise(episode=5, alive=players5, maximum=10000, earned=[
        Earning(money=10000, major={Player.ROBIN_1, Player.PETRA_1})
    ]),
    # Opdracht 2: Individuele opdrachten
    Exercise(episode=5, alive=players5, maximum=10000, earned=[
        Earning(money=10000, major={Player.ARNOUD_1, Player.FOKE_1, Player.PETRA_1, Player.ROBIN_1, Player.WILMIE_1}),
    ])
]

################
# Aflevering 6
players6 = {Player.ARNOUD_1, Player.DEBORAH_1, Player.PETRA_1, Player.ROBIN_1, Player.WILMIE_1}
exercises6 = [
    # Opdracht 1: Truckers en liften
    Exercise(episode=6, alive=players6, maximum=5000, earned=[]),
    # Opdracht 2: Ronde van Byron Bay
    Exercise(episode=6, alive=players6, maximum=5000, earned=[
        Earning(money=5000, major={Player.ARNOUD_1, Player.DEBORAH_1, Player.ROBIN_1, Player.WILMIE_1}),
    ]),
    # Opdracht 3: Vermommde hippies
    Exercise(episode=6, alive=players6, maximum=5000, earned=[])
]

################
# Aflevering 7
players7 = {Player.DEBORAH_1, Player.PETRA_1, Player.ROBIN_1, Player.WILMIE_1}
exercises7 = [
    # Opdracht 1: Surfen
    Exercise(episode=7, alive=players7, maximum=5000, earned=[]),
    # Opdracht 2: Circus
    Exercise(episode=7, alive=players7, maximum=5000, earned=[]),
    # Opdracht 3: Nimbin koor
    Exercise(episode=7, alive=players7, maximum=5000, earned=[
        Earning(money=5000, major={Player.DEBORAH_1, Player.WILMIE_1}),
    ]),
    # Opdracht 4: Armbanden
    Exercise(episode=7, alive=players7, maximum=5000, earned=[
        Earning(money=-5000, major={Player.PETRA_1, Player.ROBIN_1}),
    ])
]

################
# Aflevering 8
players8 = {Player.DEBORAH_1, Player.PETRA_1, Player.ROBIN_1}
exercises8 = [
    # Opdracht 1:
    Exercise(episode=8, alive=players8, maximum=0, earned=[]),
    # Opdracht 2: Objecten en eindbestemming
    Exercise(episode=8, alive=players8, maximum=15000, earned=[
        Earning(money=5000, major={Player.PETRA_1}),
        Earning(money=5000, major={Player.DEBORAH_1}),
        Earning(money=5000, major={Player.ROBIN_1})
    ]),
    # Opdracht 3:
    Exercise(episode=8, alive=players8, maximum=0, earned=[])
]

season1 = Season(
    exercises1 + exercises2 + exercises3 + exercises4 + exercises5 + exercises6 + exercises7 + exercises8
)
