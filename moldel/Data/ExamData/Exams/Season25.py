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
    8: Question(
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
# Summary
season25 = Season(
    players1,
    {
        1: episode1,
    },
)
