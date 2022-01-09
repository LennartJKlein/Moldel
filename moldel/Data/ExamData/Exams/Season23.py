from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput, DelayedAnswer

################
# Aflevering 1
players1 = [Player.ARNO_23, Player.EVERON_23, Player.FRESIA_23, Player.GLEN_23, Player.HILA_23, Player.KIM_LIAN_23, Player.LAETITIA_23, Player.SAHIL_23, Player.SUZANNE_23, Player.THOMAS_23, Player.WELMOED_23]
questions1 = {
    # De Mol is een...
    1: Question({
        # Man
        1: [Player.ARNO_23, Player.EVERON_23, Player.GLEN_23, Player.SAHIL_23, Player.THOMAS_23],
        # Vrouw
        2: [Player.FRESIA_23, Player.HILA_23, Player.KIM_LIAN_23, Player.LAETITIA_23, Player.SUZANNE_23, Player.WELMOED_23]
    }),
    # In welke groep zat de Mol tijdens de opdracht '(Af)troeven'?
    5: Question({
        # Troeven
        1: [Player.ARNO_23, Player.HILA_23, Player.LAETITIA_23, Player.THOMAS_23, Player.SUZANNE_23, Player.WELMOED_23],
        # Aftroeven
        2: [Player.EVERON_23, Player.FRESIA_23, Player.GLEN_23, Player.KIM_LIAN_23, Player.SAHIL_23]
    }),
    # Houdt de Mol van kamperen?
    13: Question({
        # Ja
        1: [Player.EVERON_23, Player.FRESIA_23, Player.GLEN_23, Player.SAHIL_23, Player.THOMAS_23, Player.KIM_LIAN_23, Player.LAETITIA_23, Player.SUZANNE_23, Player.WELMOED_23],
        # Nee
        2: [Player.ARNO_23, Player.HILA_23]
    }),
    # Heeft de Mol een klok stilgezet tijdens de opdracht 'Avondklok'?
    17: Question({
        # Ja
        1: [Player.FRESIA_23, Player.GLEN_23, Player.THOMAS_23],
        # Nee
        2: [Player.ARNO_23, Player.EVERON_23, Player.HILA_23, Player.KIM_LIAN_23, Player.LAETITIA_23, Player.SAHIL_23, Player.SUZANNE_23, Player.WELMOED_23]
    })
}
input1 = {
    Player.THOMAS_23: TestInput({1: 1}),
    Player.SUZANNE_23: TestInput({5: 1}),
    Player.WELMOED_23: TestInput({13: 1}),
    Player.THOMAS_23: TestInput({17: 2}),
    Player.WELMOED_23: TestInput(jokers = 1),
    Player.LAETITIA_23: TestInput(jokers = 1)
}
result1 = Result(DropType.EXECUTION_DROP, [Player.SUZANNE_23])
episode1 = Episode(
    players1,
    result1,
    input1,
    questions1
)

################
# Aflevering 2
players2 = [Player.ARNO_23, Player.EVERON_23, Player.FRESIA_23, Player.GLEN_23, Player.HILA_23, Player.KIM_LIAN_23, Player.LAETITIA_23, Player.SAHIL_23, Player.THOMAS_23, Player.WELMOED_23]
questions2 = {
    # Wat is het sterrenbeeld van de Mol?
    3: Question({
        # Kreeft
        1: [Player.ARNO_23],
        # Leeuw
        2: [Player.HILA_23],
        # Maagd
        3: [Player.WELMOED_23],
        # Ram
        4: [Player.FRESIA_23],
        # Schorpioen
        5: [Player.SAHIL_23],
        # Steenbok
        6: [Player.GLEN_23],
        # Tweeling
        7: [Player.EVERON_23, Player.LAETITIA_23],
        # Vissen
        8: [Player.THOMAS_23],
        # Weegschaal
        9: [Player.KIM_LIAN_23]
    }),
    # In welke ronde betrad de Mol het parcours tijdens de opdracht 'Prikactie'?
    11: Question({
        # Eerste
        1: [Player.GLEN_23, Player.KIM_LIAN_23],
        # Tweede
        2: [Player.FRESIA_23, Player.WELMOED_23],
        # Derde
        3: [Player.THOMAS_23, Player.HILA_23],
        # Vierde
        4: [Player.LAETITIA_23, Player.SAHIL_23],
        # Vijfde
        5: [Player.ARNO_23, Player.EVERON_23]
    }),
    # Stond de Mol op een van de ingeleverde reconstructies van de Marubi-foto's?
    17: Question({
        # Ja
        1: [Player.HILA_23, Player.SAHIL_23, Player.LAETITIA_23, Player.KIM_LIAN_23],
        # Nee
        2: [Player.THOMAS_23. Player.FRESIA_23, Player.EVERON_23, Player.WELMOED_23]
    })
}
input2 = {
    Player.WELMOED_23: TestInput({3: 9}),
    Player.FRESIA_23: TestInput({11: 4}),
    Player.GLEN_23: TestInput({17: 1}),
    Player.WELMOED_23: TestInput(jokers = 1)
}
result2 = Result(DropType.EXECUTION_DROP, [Player.GLEN_23])
episode2 = Episode(
    players2,
    result2,
    input2,
    questions2
)

################
# Summary
season23 = Season(
    players1,
    {
        1: episode1,
        2: episode2
    }
)