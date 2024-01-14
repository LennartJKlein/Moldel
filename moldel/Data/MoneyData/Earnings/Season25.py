from Data.MoneyData.Dataclasses.Season import Season
from Data.MoneyData.Dataclasses.Exercise import Exercise
from Data.MoneyData.Dataclasses.Earning import Earning
from Data.Player import Player

################
# Aflevering 1
players1 = {
    Player.ANNA_25,
    Player.BABS_25,
    Player.FONS_25,
    Player.JEROEN_25,
    Player.JIP_25,
    Player.JUSTIN_25,
    Player.KEES_25,
    Player.RIAN_25,
    Player.ROSARIO_25,
    Player.TOOSKE_25,
}
exercises1 = [
    # Opdracht 1: Speeddate
    Exercise(
        episode=1,
        alive=players1,
        maximum=6000,
        earned=[
            Earning(
                money=6000,
                major={
                    Player.ANNA_25,
                    Player.BABS_25,
                    Player.FONS_25,
                    Player.JEROEN_25,
                    Player.JIP_25,
                    Player.JUSTIN_25,
                    Player.KEES_25,
                    Player.RIAN_25,
                    Player.ROSARIO_25,
                    Player.TOOSKE_25,
                },
            ),
        ],
    ),
    # Opdracht 2: Afschilderen
    Exercise(
        episode=1,
        alive=players1,
        maximum=2500,
        earned=[
            Earning(
                money=500,
                major={Player.RIAN_25, Player.BABS_25},
                minor={
                    Player.ANNA_25,
                    Player.FONS_25,
                    Player.KEES_25,
                    Player.TOOSKE_25,
                },
            ),
        ],
    ),
]

################
# Aflevering 2
players2 = {
    Player.ANNA_25,
    Player.BABS_25,
    Player.FONS_25,
    Player.JEROEN_25,
    Player.JIP_25,
    Player.JUSTIN_25,
    Player.KEES_25,
    Player.RIAN_25,
    Player.ROSARIO_25,
    Player.TOOSKE_25,
}
exercises2 = [
    # Opdracht 1: Molympische Spelen
    Exercise(
        episode=2,
        alive=players2,
        maximum=1968,
        earned=[],
    ),
    # Opdracht 2: Uitzitten
    Exercise(
        episode=2,
        alive=players2,
        maximum=4000,
        earned=[
            Earning(money=750, major={Player.FONS_25}),
            Earning(money=750, major={Player.ANNA_25}),
            Earning(money=250, major={Player.ROSARIO_25}),
            Earning(money=250, major={Player.JUSTIN_25}),
            Earning(money=-750, major={Player.JIP_25})
        ],
    )
]

season25 = Season(
    exercises1
    + exercises2
    # + exercises3
    # + exercises4
    # + exercises5
    # + exercises6
    # + exercises7
    # + exercises8
    # + exercises9
)
