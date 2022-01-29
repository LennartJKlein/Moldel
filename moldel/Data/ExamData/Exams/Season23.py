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
    Player.ARNO_23: TestInput(
        {17: 2},
        accusations = [Player.LAETITIA_23, Player.SAHIL_23, Player.THOMAS_23, Player.WELMOED_23]
    ),
    Player.EVERON_23: TestInput(accusations = [Player.HILA_23, Player.SAHIL_23]),
    Player.FRESIA_23: TestInput(accusations = [Player.SAHIL_23, Player.GLEN_23]),
    Player.GLEN_23: TestInput(accusations = [Player.LAETITIA_23, Player.THOMAS_23, Player.WELMOED_23]),
    Player.HILA_23: TestInput(accusations = [Player.EVERON_23, Player.KIM_LIAN_23, Player.THOMAS_23]),
    Player.KIM_LIAN_23: TestInput(accusations = [Player.EVERON_23]),
    Player.LAETITIA_23: TestInput(jokers = 1),
    Player.SAHIL_23: TestInput(accusations = [Player.WELMOED_23]),
    Player.SUZANNE_23: TestInput(
        {5: 1},
        accusations = [Player.HILA_23]
    ),
    Player.THOMAS_23: TestInput({1: 1}),
    Player.WELMOED_23: TestInput(
        {13: 1},
        jokers = 1,
        accusations = [Player.HILA_23, Player.KIM_LIAN_23, Player.SAHIL_23, Player.THOMAS_23]
    )
}
result1 = Result(DropType.EXECUTION_DROP, [Player.SUZANNE_23])
episode1 = Episode(players1, result1, input1, questions1)

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
        2: [Player.THOMAS_23, Player.FRESIA_23, Player.EVERON_23, Player.WELMOED_23]
    })
}
input2 = {
    Player.EVERON_23: TestInput(accusations = [Player.KIM_LIAN_23, Player.SAHIL_23, Player.THOMAS_23]),
    Player.FRESIA_23: TestInput(
        {11: 4},
        accusations = [Player.SAHIL_23]
    ),
    Player.GLEN_23: TestInput(
        {17: 1},
        accusations = [Player.SAHIL_23, Player.THOMAS_23]
    ),
    Player.LAETITIA_23: TestInput(accusations = [Player.KIM_LIAN_23, Player.SAHIL_23, Player.THOMAS_23, Player.WELMOED_23]),
    Player.THOMAS_23: TestInput(accusations = [Player.ARNO_23, Player.GLEN_23, Player.HILA_23, Player.KIM_LIAN_23, Player.SAHIL_23]),
    Player.WELMOED_23: TestInput(
        {3: 9},
        jokers = 1,
        accusations = [Player.KIM_LIAN_23, Player.SAHIL_23, Player.THOMAS_23]
    )
}
result2 = Result(DropType.EXECUTION_DROP, [Player.GLEN_23])
episode2 = Episode(players2, result2, input2, questions2)

################
# Aflevering 3
players3 = [Player.ARNO_23, Player.EVERON_23, Player.FRESIA_23, Player.HILA_23, Player.KIM_LIAN_23, Player.LAETITIA_23, Player.SAHIL_23, Player.THOMAS_23, Player.WELMOED_23]
questions3 = {
    # Is de Mol in het water geweest tijdens de opdracht 'Net of net niet'?
    5: Question({
        # Ja
        1: [Player.ARNO_23, Player.FRESIA_23, Player.HILA_23, Player.KIM_LIAN_23, Player.SAHIL_23, Player.THOMAS_23, Player.WELMOED_23],
        # Nee
        2: [Player.EVERON_23, Player.LAETITIA_23]
    }),
    # Werd de Mol afgeschoten tijdens de opdracht 'Waar rook is, is vuur'?
    11: Question({
        # Ja
        1: [Player.EVERON_23, Player.FRESIA_23, Player.HILA_23, Player.KIM_LIAN_23, Player.WELMOED_23],
        # Nee
        2: [Player.ARNO_23, Player.LAETITIA_23, Player.SAHIL_23, Player.THOMAS_23]
    }),
    # Heeft de Mol een kistje geopend tijdens de opdracht 'Waar rook is, is vuur'?
    12: Question({
        # Ja
        1: [Player.EVERON_23, Player.FRESIA_23, Player.HILA_23, Player.KIM_LIAN_23, Player.WELMOED_23],
        # Nee
        2: [Player.ARNO_23, Player.LAETITIA_23, Player.SAHIL_23, Player.THOMAS_23]
    }),
    # Wie is de Mol?
    20: Question({
        # Arno
        1: [Player.ARNO_23],
        # Everon
        2: [Player.EVERON_23],
        # Fresia
        3: [Player.FRESIA_23],
        # Hila
        4: [Player.HILA_23],
        # Kim-Lian
        5: [Player.KIM_LIAN_23],
        # Laetitia
        6: [Player.LAETITIA_23],
        # Sahil
        7: [Player.SAHIL_23],
        # Thomas
        8: [Player.THOMAS_23],
        # Welmoed
        9: [Player.WELMOED_23]
    })
}
input3 = {
    Player.ARNO_23: TestInput(
        # vrijstelling ongedaan gemaakt
        accusations = [Player.WELMOED_23]
    ),
    Player.EVERON_23: TestInput(accusations = [Player.THOMAS_23]),
    Player.FRESIA_23: TestInput(
        {20: 7},
        accusations = [Player.SAHIL_23]
    ),
    Player.HILA_23: TestInput(
        # zwarte vrijstelling
        accusations = [Player.FRESIA_23, Player.THOMAS_23]
    ),
    Player.KIM_LIAN_23: TestInput(
        {20: 2},
        accusations = [Player.EVERON_23]
    ),
    Player.LAETITIA_23: TestInput(accusations = [Player.KIM_LIAN_23, Player.SAHIL_23]),
    Player.SAHIL_23: TestInput(
        {12: 1},
        accusations = [Player.KIM_LIAN_23, Player.THOMAS_23]
    ),
    Player.THOMAS_23: TestInput(
        {5: 1},
        accusations = [Player.ARNO_23, Player.KIM_LIAN_23, Player.SAHIL_23]
    ),
    Player.WELMOED_23: TestInput(
        {11: 1},
        accusations = [Player.HILA_23, Player.KIM_LIAN_23, Player.SAHIL_23, Player.THOMAS_23]
    )
}
result3 = Result(DropType.EXECUTION_DROP, [Player.WELMOED_23])
episode3 = Episode(players3, result3, input3, questions3)

################
# Aflevering 4
players4 = [Player.ARNO_23, Player.EVERON_23, Player.FRESIA_23, Player.HILA_23, Player.KIM_LIAN_23, Player.LAETITIA_23, Player.SAHIL_23, Player.THOMAS_23]
questions4 = {
    # De Mol is een...
    1: Question({
        # Man
        1: [Player.ARNO_23, Player.EVERON_23, Player.SAHIL_23, Player.THOMAS_23],
        # Vrouw
        2: [Player.FRESIA_23, Player.HILA_23, Player.KIM_LIAN_23, Player.LAETITIA_23, Player.SUZANNE_23]
    }),
    # Met wie vormde de Mol een duo tijdens de opdracht 'Luid sprekers'?
    4: Question({
        # Arno
        1: [Player.ARNO_23],
        # Everon
        2: [Player.EVERON_23],
        # Fresia
        3: [Player.FRESIA_23],
        # Hila
        4: [Player.HILA_23],
        # Kim-Lian
        5: [Player.KIM_LIAN_23],
        # Laetitia
        6: [Player.LAETITIA_23],
        # Sahil
        7: [Player.SAHIL_23],
        # Thomas
        8: [Player.THOMAS_23]
    }),
    # Wat deed de Mol in het kistje 'ondersteboven' tijdens de opdracht 'Hoog spel spelen'?
    11: Question({
        # Twee jokers
        1: [Player.ARNO_23, Player.EVERON_23, Player.FRESIA_23, Player.LAETITIA_23],
        # 250 euro
        2: [Player.HILA_23, Player.KIM_LIAN_23, Player.THOMAS_23],
        # Niets
        3: [Player.SAHIL_23]
    }),
    # Wie is de Mol?
    20: Question({
        # Arno
        1: [Player.ARNO_23],
        # Everon
        2: [Player.EVERON_23],
        # Fresia
        3: [Player.FRESIA_23],
        # Hila
        4: [Player.HILA_23],
        # Kim-Lian
        5: [Player.KIM_LIAN_23],
        # Laetitia
        6: [Player.LAETITIA_23],
        # Sahil
        7: [Player.SAHIL_23],
        # Thomas
        8: [Player.THOMAS_23]
    })
}
input4 = {
    Player.ARNO_23: TestInput(
        {11: 1}
    ),
    Player.EVERON_23: TestInput(
        jokers = 1,
        accusations = [Player.KIM_LIAN_23, Player.THOMAS_23]
    ),
    Player.HILA_23: TestInput(
        accusations = [Player.FRESIA_23, Player.SAHIL_23]
    ),
    Player.KIM_LIAN_23: TestInput(
        accusations = [Player.EVERON_23, Player.SAHIL_23]
    ),
    Player.LAETITIA_23: TestInput(
        {1: 1}
    ),
    Player.FRESIA_23: TestInput(
        {4: 3},
        jokers = 1
    ),
    Player.SAHIL_23: TestInput(
        {20: 8},
        accusations = [Player.ARNO_23, Player.KIM_LIAN_23, Player.THOMAS_23]
    ),
    Player.THOMAS_23: TestInput(
        jokers = 2,
        accusations = [Player.ARNO_23, Player.KIM_LIAN_23, Player.SAHIL_23]
    ),
}
result4 = Result(DropType.EXECUTION_DROP, [Player.ARNO_23])
episode4 = Episode(players4, result4, input4, questions4)

################
# Aflevering 5
players5 = [Player.EVERON_23, Player.FRESIA_23, Player.HILA_23, Player.KIM_LIAN_23, Player.LAETITIA_23, Player.SAHIL_23, Player.THOMAS_23]
questions5 = {
    # Waar was de Mol bij aanvang van de opdracht 'Uit de lucht gegrepen'?
    2: Question({
        # Vastgebonden op het strandje
        1: [Player.EVERON_23, Player.HILA_23, Player.KIM_LIAN_23, Player.LAETITIA_23, Player.THOMAS_23],
        # In een vliegtuigje
        2: [Player.FRESIA_23, Player.SAHIL_23]
    }),
    # Heeft de Mol de Moltelefoon?
    6: Question({
        # Ja
        1: [Player.SAHIL_23],
        # Nee
        2: [Player.EVERON_23, Player.FRESIA_23, Player.HILA_23, Player.KIM_LIAN_23, Player.LAETITIA_23, Player.THOMAS_23]
    }),
    # Hoeveel zwanen zater er achter fietssup van de Mol aan het einde van de opdracht 'Zwanenmeer'?
    10: Question({
        # Vier
        1: [Player.KIM_LIAN_23, Player.SAHIL_23],
        # Vijf
        2: [Player.KIM_LIAN_23, Player.SAHIL_23],
        # Zes
        3: [Player.KIM_LIAN_23, Player.SAHIL_23]
    }),
    # Is de Mol de huidige penningmeester?
    19: Question({
        # Ja
        1: [Player.HILA_23],
        # Nee
        2: [Player.EVERON_23, Player.FRESIA_23, Player.KIM_LIAN_23, Player.LAETITIA_23, Player.SAHIL_23, Player.THOMAS_23]
    }),
    # Wie is de Mol?
    20: Question({
        # Everon
        1: [Player.EVERON_23],
        # Fresia
        2: [Player.FRESIA_23],
        # Hila
        3: [Player.HILA_23],
        # Kim-Lian
        4: [Player.KIM_LIAN_23],
        # Laetitia
        5: [Player.LAETITIA_23],
        # Sahil
        6: [Player.SAHIL_23],
        # Thomas
        7: [Player.THOMAS_23]
    })
}
input5 = {
    Player.THOMAS_23: TestInput(
        {10: 1}
    ),
    Player.FRESIA_23: TestInput(
        {2: 1},
        jokers = 1,
        accusations = [Player.EVERON_23]
    ),
    Player.EVERON_23: TestInput(
        jokers = 1,
        accusations = [Player.KIM_LIAN_23]
    ),
    Player.HILA_23: TestInput(
        {19: 2},
        jokers = 1
    ),
    Player.LAETITIA_23: TestInput(
        jokers = 1
    ),
    Player.KIM_LIAN_23: TestInput(
        {6: 2},
        jokers = 1,
        accusations = [Player.EVERON_23, Player.SAHIL_23]
    ),
    Player.SAHIL_23: TestInput(
        {20: 7},
        jokers = 1,
        accusations = [Player.KIM_LIAN_23, Player.THOMAS_23]
    )
}
result5 = Result(DropType.EXECUTION_DROP, [Player.HILA_23])
episode5 = Episode(players5, result5, input5, questions5)

################
# Aflevering 6
players6 = [Player.EVERON_23, Player.FRESIA_23, Player.HILA_23, Player.KIM_LIAN_23, Player.LAETITIA_23, Player.SAHIL_23, Player.THOMAS_23]
# questions6 = {
# }
# input6 = {
# }
# result6 = Result(DropType.EXECUTION_DROP, [])
# episode6 = Episode(players6, result6, input6, questions6)

################
# Aflevering 7
players7 = [Player.EVERON_23, Player.FRESIA_23, Player.HILA_23, Player.KIM_LIAN_23, Player.LAETITIA_23, Player.SAHIL_23, Player.THOMAS_23]
# questions7 = {
# }
# input7 = {
# }
# result7 = Result(DropType.EXECUTION_DROP, [])
# episode7 = Episode(players7, result7, input7, questions7)

################
# Aflevering 8
players8 = [Player.EVERON_23, Player.FRESIA_23, Player.HILA_23, Player.KIM_LIAN_23, Player.LAETITIA_23, Player.SAHIL_23, Player.THOMAS_23]
# questions8 = {
# }
# input8 = {
# }
# result8 = Result(DropType.EXECUTION_DROP, [])
# episode8 = Episode(players8, result8, input8, questions8)

################
# Aflevering 9
players9 = [Player.EVERON_23, Player.FRESIA_23, Player.HILA_23, Player.KIM_LIAN_23, Player.LAETITIA_23, Player.SAHIL_23, Player.THOMAS_23]
# questions9 = {
# }
# input9 = {
# }
# result9 = Result(DropType.EXECUTION_DROP, [])
# episode9 = Episode(players9, result9, input9, questions9)

################
# Summary
season23 = Season(
    players1,
    {
        1: episode1,
        2: episode2,
        3: episode3,
        4: episode4,
        5: episode5
    }
)