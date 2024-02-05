from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput

################
# Aflevering 1
players1 = [
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
]
questions1 = {
    # Naar welk symbool was de Mol, als kandidaat, op zoek tijdens 'Dia del Top(it)o'?
    7: Question(
        {
            # Bel
            1: [Player.FONS_25],
            # Brood
            2: [Player.ROSARIO_25],
            # Cactus
            3: [Player.JUSTIN_25],
            # Hart
            4: [Player.RIAN_25],
            # Kroon
            5: [Player.ANNA_25],
            # Paraplu
            6: [Player.TOOSKE_25],
            # Piramide
            7: [Player.KEES_25],
            # Schaar
            8: [Player.JEROEN_25],
            # Vlag
            9: [Player.JIP_25],
            # Zeemeermin
            10: [Player.BABS_25],
        }
    ),
    # Voor welke aflevering heeft de Mol een vrijstelling gekregen?
    8: Question(
        {
            # Aflevering 1
            1: [Player.RIAN_25, Player.BABS_25, Player.KEES_25],
            # Aflevering 2
            2: [Player.JEROEN_25, Player.ROSARIO_25],
            # Aflevering 3
            3: [Player.TOOSKE_25],
            # De Mol heeft geen vrijstelling gekregen
            4: [Player.ANNA_25, Player.FONS_25, Player.JIP_25, Player.JUSTIN_25],
        }
    ),
    # Met wie had de Mol de eerste speeddate?
    9: Question(
        {
            1: [Player.ANNA_25],
            2: [Player.BABS_25],
            3: [Player.FONS_25],
            4: [Player.JEROEN_25],
            5: [Player.JIP_25],
            6: [Player.JUSTIN_25],
            7: [Player.KEES_25],
            8: [Player.RIAN_25],
            9: [Player.ROSARIO_25],
            10: [Player.TOOSKE_25],
        }
    ),
    # Welke taak had de Mol tijdens de Frida Kahlo opdracht?
    14: Question(
        {
            # Zelfportret naschilderen
            1: [
                Player.FONS_25,
                Player.JIP_25,
                Player.JEROEN_25,
                Player.ROSARIO_25,
                Player.JUSTIN_25,
            ],
            # Schilderijen verzamelen
            2: [Player.TOOSKE_25, Player.KEES_25, Player.ANNA_25],
            # Schilderijen beoordelen
            3: [Player.BABS_25, Player.RIAN_25],
        }
    ),
    # Wie is de Mol?
    20: Question(
        {
            1: [Player.ANNA_25],
            2: [Player.BABS_25],
            3: [Player.FONS_25],
            4: [Player.JEROEN_25],
            5: [Player.JIP_25],
            6: [Player.JUSTIN_25],
            7: [Player.KEES_25],
            8: [Player.RIAN_25],
            9: [Player.ROSARIO_25],
            10: [Player.TOOSKE_25],
        }
    ),
}
input1 = {
    Player.JEROEN_25: TestInput(
        {8: 4},
        accusations=[Player.FONS_25, Player.JUSTIN_25, Player.JIP_25, Player.BABS_25],
    ),
    Player.FONS_25: TestInput({7: 6}, accusations=[Player.TOOSKE_25, Player.JIP_25]),
    Player.RIAN_25: TestInput(accusations=[Player.FONS_25]),
    Player.JIP_25: TestInput(
        accusations=[Player.JUSTIN_25, Player.TOOSKE_25, Player.RIAN_25]
    ),
    Player.JUSTIN_25: TestInput(
        {9: 7}, accusations=[Player.JIP_25, Player.BABS_25, Player.JEROEN_25]
    ),
    Player.ANNA_25: TestInput({14: 1}),
    Player.ROSARIO_25: TestInput({20: 1}, accusations=[Player.JIP_25, Player.ANNA_25]),
}
result1 = Result(DropType.EXECUTION_DROP, [Player.BABS_25])
episode1 = Episode(players1, result1, input1, questions1)

################
# Aflevering 2
players2 = [
    Player.ANNA_25,
    Player.FONS_25,
    Player.JEROEN_25,
    Player.JIP_25,
    Player.JUSTIN_25,
    Player.KEES_25,
    Player.RIAN_25,
    Player.ROSARIO_25,
    Player.TOOSKE_25,
]
questions2 = {
    # Is de Mol een man of een vrouw?
    1: Question(
        {  # Man
            1: [
                Player.JEROEN_25,
                Player.JUSTIN_25,
                Player.KEES_25,
                Player.ROSARIO_25,
                Player.FONS_25,
            ],
            # Vrouw
            2: [Player.ANNA_25, Player.JIP_25, Player.RIAN_25, Player.TOOSKE_25],
        }
    ),
    # Wat was de positie van de Mol bij aanvang van de opdracht in het stadion?
    4: Question(
        {
            # Atletiekbaan
            1: [
                Player.JEROEN_25,
                Player.TOOSKE_25,
                Player.ROSARIO_25,
                Player.KEES_25,
                Player.FONS_25,
            ],
            # Middenstip
            2: [Player.ANNA_25],
            # Tribune
            3: [Player.JIP_25, Player.JUSTIN_25, Player.RIAN_25],
        }
    ),
    # Heeft de Mol het Molympisch vuur onstoken?
    6: Question(
        {
            # Ja
            1: [Player.JUSTIN_25],
            # Nee
            2: [
                Player.JIP_25,
                Player.ANNA_25,
                Player.RIAN_25,
                Player.JEROEN_25,
                Player.TOOSKE_25,
                Player.ROSARIO_25,
                Player.KEES_25,
                Player.FONS_25,
            ],
        }
    ),
}
input2 = {
    Player.JUSTIN_25: TestInput(
        accusations=[Player.ANNA_25, Player.JIP_25, Player.TOOSKE_25, Player.FONS_25]
    ),
    Player.FONS_25: TestInput(
        {1: 2}, accusations=[Player.TOOSKE_25, Player.JIP_25, Player.ANNA_25]
    ),
    Player.RIAN_25: TestInput(accusations=[Player.KEES_25]),
    Player.KEES_25: TestInput({4: 3}, accusations=[Player.RIAN_25]),
    Player.ROSARIO_25: TestInput(accusations=[Player.JIP_25, Player.TOOSKE_25]),
    Player.JIP_25: TestInput({6: 1}, accusations=[Player.JUSTIN_25]),
}
result2 = Result(DropType.EXECUTION_DROP, [Player.JIP_25])
episode2 = Episode(players2, result2, input2, questions2)

################
# Aflevering 3
players3 = [
    Player.ANNA_25,
    Player.FONS_25,
    Player.JEROEN_25,
    Player.JUSTIN_25,
    Player.KEES_25,
    Player.RIAN_25,
    Player.ROSARIO_25,
    Player.TOOSKE_25,
]
questions3 = {
    # Is de Mol een man of een vrouw?
    1: Question(
        {  # Man
            1: [
                Player.JEROEN_25,
                Player.JUSTIN_25,
                Player.KEES_25,
                Player.ROSARIO_25,
                Player.FONS_25,
            ],
            # Vrouw
            2: [Player.ANNA_25, Player.RIAN_25, Player.TOOSKE_25],
        }
    ),
    # Heeft de Mol de antwoorden genoteerd tijdens de opdracht met de mariachi's?
    4: Question(
        {  # Ja
            1: [Player.JEROEN_25],
            # Nee
            2: [
                Player.ANNA_25,
                Player.FONS_25,
                Player.JUSTIN_25,
                Player.KEES_25,
                Player.RIAN_25,
                Player.ROSARIO_25,
                Player.TOOSKE_25,
            ],
        }
    ),
    # Danste de Mol staand de Macarena?
    6: Question(
        {  # Ja
            1: [Player.TOOSKE_25],
            # Nee
            2: [
                Player.ANNA_25,
                Player.FONS_25,
                Player.JEROEN_25,
                Player.JUSTIN_25,
                Player.KEES_25,
                Player.RIAN_25,
                Player.ROSARIO_25,
            ],
        }
    ),
    # Was de Mol aanwezig op het einde van de opdracht met de wereldsteden?
    13: Question(
        {  # Ja
            1: [
                Player.FONS_25,
                Player.JEROEN_25,
                Player.JUSTIN_25,
                Player.KEES_25,
                Player.RIAN_25,
                Player.ROSARIO_25,
            ],
            # Nee
            2: [Player.ANNA_25, Player.TOOSKE_25],
        }
    ),
}
input3 = {
    Player.RIAN_25: TestInput({13: 1}, accusations=[Player.KEES_25, Player.TOOSKE_25]),
    Player.ANNA_25: TestInput(
        {6: 1}, accusations=[Player.FONS_25, Player.TOOSKE_25, Player.JEROEN_25]
    ),
    Player.FONS_25: TestInput(
        {1: 2}, accusations=[Player.ANNA_25, Player.RIAN_25, Player.TOOSKE_25]
    ),
    Player.TOOSKE_25: TestInput(
        accusations=[Player.KEES_25, Player.RIAN_25, Player.JEROEN_25]
    ),
    Player.JEROEN_25: TestInput(accusations=[Player.TOOSKE_25, Player.FONS_25]),
    Player.JUSTIN_25: TestInput({4: 2}),
}
result3 = Result(DropType.EXECUTION_DROP, [Player.JUSTIN_25])
episode3 = Episode(players3, result3, input3, questions3)

################
# Aflevering 4
players4 = [
    Player.ANNA_25,
    Player.FONS_25,
    Player.JEROEN_25,
    Player.KEES_25,
    Player.RIAN_25,
    Player.ROSARIO_25,
    Player.TOOSKE_25,
]
episode4 = Episode(
    players4, Result(DropType.NO_DROP_NOR_SCREENS, players4), dict(), dict()
)

################
# Aflevering 5
players5 = [
    Player.ANNA_25,
    Player.BABS_25,
    Player.FONS_25,
    Player.JEROEN_25,
    Player.KEES_25,
    Player.RIAN_25,
    Player.ROSARIO_25,
    Player.TOOSKE_25,
]
questions5 = {
    # Heeft de Mol in het huis gestaan waar Dennis Weening aanwezig was?
    7: Question(
        {
            # Ja
            1: [
                Player.BABS_25,
                Player.FONS_25,
            ],
            # Nee
            2: [
                Player.ANNA_25,
                Player.JEROEN_25,
                Player.KEES_25,
                Player.RIAN_25,
                Player.ROSARIO_25,
                Player.TOOSKE_25,
            ],
        }
    ),
    # Wat zat er in de envelop van de Mol aan het einde van de opdracht met de enveloppen?
    10: Question(
        {
            # Min 3000 euro
            1: [Player.ROSARIO_25],
            # Min 500 euro
            2: [Player.ANNA_25],
            # Niets
            3: [Player.JEROEN_25, Player.FONS_25, Player.KEES_25, Player.RIAN_25],
            # 3 jokers
            4: [Player.TOOSKE_25],
            # 250 euro
            5: [Player.BABS_25],
        }
    ),
    # Met wie vormde de Mol een duo tijdens de opdracht met de paardentaxi's?
    14: Question(
        {
            1: [Player.RIAN_25],
            2: [Player.ROSARIO_25],
            3: [Player.JEROEN_25],
            4: [Player.FONS_25],
            5: [Player.TOOSKE_25],
            6: [Player.ANNA_25],
            7: [Player.BABS_25],
            8: [Player.KEES_25],
        }
    ),
    # Wie is de Mol?
    20: Question(
        {
            1: [Player.ANNA_25],
            2: [Player.BABS_25],
            3: [Player.FONS_25],
            4: [Player.JEROEN_25],
            5: [Player.KEES_25],
            6: [Player.RIAN_25],
            7: [Player.ROSARIO_25],
            8: [Player.TOOSKE_25],
        }
    ),
}
input5 = {
    Player.TOOSKE_25: TestInput(
        jokers=3,
        accusations=[
            Player.ROSARIO_25,
            Player.FONS_25,
            Player.RIAN_25,
            Player.JEROEN_25,
        ],
    ),
    Player.ANNA_25: TestInput(
        {20: 3}, accusations=[Player.FONS_25, Player.TOOSKE_25, Player.ROSARIO_25]
    ),
    Player.BABS_25: TestInput({14: 3}),
    Player.ROSARIO_25: TestInput(jokers=1),
    Player.FONS_25: TestInput(
        {7: 2}, jokers=1, accusations=[Player.ANNA_25, Player.RIAN_25, Player.TOOSKE_25]
    ),
    Player.RIAN_25: TestInput(accusations=[Player.ROSARIO_25, Player.KEES_25]),
    Player.KEES_25: TestInput({10: 5}, jokers=1),
}
result5 = Result(DropType.EXECUTION_DROP, [Player.JEROEN_25])
episode5 = Episode(players5, result5, input5, questions5)

################
# Summary
season25 = Season(
    players1,
    {
        1: episode1,
        2: episode2,
        3: episode3,
        4: episode4,
        5: episode5,
    },
)
