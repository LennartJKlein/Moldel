from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput

################
# Aflevering 1
players1 = [Player.ARNOUD_1, Player.DEBORAH_1, Player.FOKE_1, Player.JOHN_1, Player.PETRA_1,
            Player.ROBIN_1, Player.SANDY_1, Player.WARNER_1, Player.WILLY_1, Player.WILMIE_1]
questions1 = {
    # De Mol is een...
    1: Question({
        # Man
        1: [Player.ARNOUD_1, Player.JOHN_1, Player.ROBIN_1, Player.WARNER_1, Player.WILLY_1],
        # Vrouw
        2: [Player.DEBORAH_1, Player.FOKE_1, Player.PETRA_1, Player.SANDY_1, Player.WILMIE_1]
    })
}
input1 = {
    Player.FOKE_1: TestInput(accusations=[Player.JOHN_1]),
    Player.WILLY_1: TestInput(accusations=[Player.JOHN_1]),
    Player.JOHN_1: TestInput(
        {1: 2},
        accusations=[Player.WILMIE_1]
    ),
    Player.WILMIE_1: TestInput(accusations=[Player.WARNER_1]),
    Player.DEBORAH_1: TestInput(accusations=[Player.ARNOUD_1]),
    Player.ARNOUD_1: TestInput(accusations=[Player.WILMIE_1]),
    Player.SANDY_1: TestInput(accusations=[Player.WILMIE_1]),
    Player.PETRA_1: TestInput(accusations=[Player.WILMIE_1, Player.ROBIN_1])
}
result1 = Result(DropType.EXECUTION_DROP, [Player.SANDY_1])
episode1 = Episode(players1, result1, input1, questions1)

################
# Aflevering 2
players2 = [Player.ARNOUD_1, Player.DEBORAH_1, Player.FOKE_1, Player.JOHN_1,
            Player.PETRA_1, Player.ROBIN_1, Player.WARNER_1, Player.WILLY_1, Player.WILMIE_1]
questions2 = dict()
input2 = {
    Player.PETRA_1: TestInput(accusations=[Player.WILMIE_1]),
    Player.FOKE_1: TestInput(accusations=[Player.JOHN_1]),
    Player.JOHN_1: TestInput(accusations=[Player.WILMIE_1]),
    Player.WILMIE_1: TestInput(accusations=[Player.WARNER_1]),
    Player.DEBORAH_1: TestInput(accusations=[Player.ARNOUD_1]),
    Player.ARNOUD_1: TestInput(accusations=[Player.WILMIE_1]),
    Player.ROBIN_1: TestInput(accusations=[Player.WILMIE_1]),
    Player.WILLY_1: TestInput(accusations=[Player.JOHN_1])
}
result2 = Result(DropType.EXECUTION_DROP, [Player.WILLY_1])
episode2 = Episode(players2, result2, input2, questions2)

################
# Aflevering 3
players3 = [Player.ARNOUD_1, Player.DEBORAH_1, Player.FOKE_1, Player.JOHN_1,
            Player.PETRA_1, Player.ROBIN_1, Player.WARNER_1, Player.WILMIE_1]
questions3 = dict()
input3 = {
    Player.ARNOUD_1: TestInput(accusations=[Player.WILMIE_1]),
    Player.WARNER_1: TestInput(accusations=[Player.WILMIE_1]),
    Player.PETRA_1: TestInput(accusations=[Player.ROBIN_1, Player.JOHN_1]),
    Player.ROBIN_1: TestInput(accusations=[Player.PETRA_1]),
    Player.FOKE_1: TestInput(accusations=[Player.JOHN_1]),
    Player.DEBORAH_1: TestInput(accusations=[Player.JOHN_1, Player.WILMIE_1]),
    Player.JOHN_1: TestInput(accusations=[Player.WARNER_1])
}
result3 = Result(DropType.EXECUTION_DROP, [Player.JOHN_1])
episode3 = Episode(players3, result3, input3, questions3)

################
# Aflevering 4
players4 = [Player.ARNOUD_1, Player.DEBORAH_1, Player.FOKE_1,
            Player.PETRA_1, Player.ROBIN_1, Player.WARNER_1, Player.WILMIE_1]
questions4 = dict()
input4 = {
    Player.DEBORAH_1: TestInput(accusations=[Player.ARNOUD_1]),
    Player.ARNOUD_1: TestInput(accusations=[Player.WILMIE_1]),
    Player.WILMIE_1: TestInput(accusations=[Player.WARNER_1, Player.ROBIN_1]),
    Player.PETRA_1: TestInput(accusations=[Player.ROBIN_1]),
    Player.ROBIN_1: TestInput(accusations=[Player.WILMIE_1])
}
result4 = Result(DropType.EXECUTION_DROP, [Player.WARNER_1])
episode4 = Episode(players4, result4, input4, questions4)

################
# Aflevering 5
players5 = [Player.ARNOUD_1, Player.DEBORAH_1, Player.FOKE_1, Player.PETRA_1, Player.ROBIN_1,  Player.WILMIE_1]
questions5 = {
    # Wat deed de Mol maandag?
    2: Question({
        # Boogschieten
        1: [Player.ROBIN_1],
        # Karten
        2: [Player.PETRA_1],
        # Whale watching
        3: [Player.ARNOUD_1, Player.DEBORAH_1, Player.FOKE_1, Player.WILMIE_1]
    }),
    # De mol heeft...
    3: Question({
        # Een donkere huid
        1: [Player.ROBIN_1, Player.DEBORAH_1],
        # Een lichte huid
        2: [Player.ARNOUD_1, Player.FOKE_1, Player.PETRA_1, Player.WILMIE_1]
    })
}
input5 = {
    Player.ARNOUD_1: TestInput({2: 2, 3: 2}, accusations=[Player.WILMIE_1]),
    Player.WILMIE_1: TestInput(accusations=[Player.ROBIN_1]),
    Player.ROBIN_1: TestInput(accusations=[Player.WILMIE_1]),
    Player.DEBORAH_1: TestInput(accusations=[Player.ROBIN_1]),
    Player.FOKE_1: TestInput(accusations=[Player.WILMIE_1]),
    Player.PETRA_1: TestInput({3: 2}, accusations=[Player.WILMIE_1])
}
result5 = Result(DropType.EXECUTION_DROP, [Player.FOKE_1])
episode5 = Episode(players5, result5, input5, questions5)

################
# Aflevering 6
players6 = [Player.ARNOUD_1, Player.DEBORAH_1, Player.PETRA_1, Player.ROBIN_1,  Player.WILMIE_1]
questions6 = {
    # De mol heeft...
    3: Question({
        # Een donkere huid
        1: [Player.ROBIN_1, Player.DEBORAH_1],
        # Een lichte huid
        2: [Player.ARNOUD_1, Player.PETRA_1, Player.WILMIE_1]
    })}
input6 = {
    Player.DEBORAH_1: TestInput(accusations=[Player.PETRA_1]),
    Player.ARNOUD_1: TestInput({3: 2}, accusations=[Player.WILMIE_1]),
    Player.WILMIE_1: TestInput(accusations=[Player.ROBIN_1, Player.PETRA_1]),
    Player.ROBIN_1: TestInput(accusations=[Player.WILMIE_1]),
    Player.PETRA_1: TestInput(immunity=True, accusations=[Player.WILMIE_1])
}
result6 = Result(DropType.EXECUTION_DROP, [Player.ARNOUD_1])
episode6 = Episode(players6, result6, input6, questions6)

################
# Aflevering 7
players7 = [Player.DEBORAH_1, Player.PETRA_1, Player.ROBIN_1,  Player.WILMIE_1]
questions7 = dict()
input7 = {
    Player.PETRA_1: TestInput(accusations=[Player.DEBORAH_1]),
    Player.WILMIE_1: TestInput(accusations=[Player.ROBIN_1]),
    Player.DEBORAH_1: TestInput(accusations=[Player.ROBIN_1]),
    Player.ROBIN_1: TestInput(accusations=[Player.WILMIE_1])
}
result7 = Result(DropType.EXECUTION_DROP, [Player.WILMIE_1])
episode7 = Episode(players7, result7, input7, questions7)

################
# Aflevering 8
players8 = [Player.DEBORAH_1, Player.PETRA_1, Player.ROBIN_1]
questions8 = dict()
input8 = {
    Player.ROBIN_1: TestInput(accusations=[Player.PETRA_1]),
    Player.DEBORAH_1: TestInput(accusations=[Player.PETRA_1])
}
result8 = Result(DropType.EXECUTION_DROP, [Player.ROBIN_1])
episode8 = Episode(players8, result8, input8, questions8, num_questions=40)

################
# Summary
season1 = Season(
    players1,
    {
        1: episode1,
        2: episode2,
        3: episode3,
        4: episode4,
        5: episode5,
        6: episode6,
        7: episode7,
        8: episode8
    }
)
