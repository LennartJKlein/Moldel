from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput, DelayedAnswer

################
# Aflevering 1
players1 = [Player.ANKE_24, Player.ANNICK_24, Player.DANIEL_24, Player.FROUKJE_24, Player.JURRE_24,
            Player.NABIL_24, Player.RANOMI_24, Player.SANDER_24, Player.SARAH_24, Player.SOY_24]
questions1 = {
    # De Mol is een...
    1: Question({
        # Man
        1: [Player.DANIEL_24, Player.JURRE_24, Player.NABIL_24, Player.SANDER_24, Player.SOY_24],
        # Vrouw
        2: [Player.ANKE_24, Player.ANNICK_24, Player.FROUKJE_24, Player.RANOMI_24, Player.SARAH_24]
    }),
    # Met wie zat de Mol opgesloten in een kist?
    10: Question({
        # Anke
        1: [Player.SANDER_24],
        # Annick
        2: [Player.SOY_24],
        # Daniel
        3: [Player.FROUKJE_24],
        # Froukje
        4: [Player.DANIEL_24],
        # Jurre
        5: [Player.SARAH_24],
        # Nabil
        6: [Player.RANOMI_24],
        # Ranomi
        7: [Player.NABIL_24],
        # Sander
        8: [Player.ANKE_24],
        # Sarah
        9: [Player.JURRE_24],
        # Soy
        10: [Player.ANNICK_24],
    }),
    # In welke kleur kist was de Mol opgesloten?
    11: Question({
        # Blauw
        1: [Player.NABIL_24, Player.RANOMI_24],
        # Geel
        2: [Player.SANDER_24, Player.ANKE_24],
        # Groen
        3: [Player.JURRE_24, Player.SARAH_24],
        # Rood
        4: [Player.FROUKJE_24, Player.DANIEL_24],
        # Zwart
        5: [Player.SOY_24, Player.ANNICK_24]
    }),
    # Wat was de rol van de Mol tijdens de opdracht met het koor?
    17: Question({
        # Optreden
        1: [Player.SOY_24, Player.SANDER_24, Player.ANKE_24, Player.SARAH_24],
        # Deelopdrachten voltooien
        2: [Player.NABIL_24,
            Player.ANNICK_24, Player.DANIEL_24, Player.RANOMI_24, Player.FROUKJE_24]
    }),
    # Welk bedrag werd de Mol toebedeeld tijdens de opdracht met het koor?
    18: Question({
        # 250
        1: [Player.ANKE_24],
        # 500
        2: [Player.SANDER_24],
        # 750
        3: [Player.JURRE_24],
        # 1000
        4: [Player.SOY_24],
        # 1500
        5: [Player.SARAH_24],
        # De Mol deed deelopdrachten
        6: [Player.NABIL_24,
            Player.ANNICK_24, Player.DANIEL_24, Player.RANOMI_24, Player.FROUKJE_24]
    }),
}
input1 = {
    Player.NABIL_24: TestInput(
        accusations=[Player.RANOMI_24, Player.SANDER_24, Player.FROUKJE_24, Player.ANKE_24]
    ),
    Player.DANIEL_24: TestInput({18: 6}),
    Player.FROUKJE_24: TestInput({10: 4}, accusations=[Player.ANNICK_24, Player.DANIEL_24]),
    Player.SARAH_24: TestInput({11: 4}, accusations=[Player.FROUKJE_24, Player.RANOMI_24, Player.DANIEL_24, Player.SANDER_24]),
    Player.SANDER_24: TestInput(accusations=[Player.SOY_24, Player.FROUKJE_24, Player.SARAH_24, Player.ANNICK_24]),
    Player.ANKE_24: TestInput({1: 2}, accusations=[Player.ANNICK_24, Player.FROUKJE_24,
                                                   Player.NABIL_24, Player.SANDER_24, Player.SARAH_24, Player.SOY_24]),
    Player.JURRE_24: TestInput(accusations=[Player.ANKE_24, Player.DANIEL_24,
                                            Player.NABIL_24, Player.RANOMI_24, Player.SANDER_24, Player.SARAH_24, Player.SOY_24]),

    Player.ANNICK_24: TestInput({17: 1}, accusations=[Player.FROUKJE_24, Player.RANOMI_24, Player.SARAH_24, Player.SANDER_24]),

}
result1 = Result(DropType.EXECUTION_DROP, [Player.SARAH_24])
episode1 = Episode(players1, result1, input1, questions1)

################
# Summary
season24 = Season(
    players1,
    {
        1: episode1
    }
)
