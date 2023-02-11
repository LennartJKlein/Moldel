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
        2: [Player.NABIL_24, Player.ANNICK_24, Player.DANIEL_24, Player.RANOMI_24, Player.FROUKJE_24]
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
        6: [Player.NABIL_24, Player.ANNICK_24, Player.DANIEL_24, Player.RANOMI_24, Player.FROUKJE_24]
    }),
}
input1 = {
    Player.NABIL_24: TestInput(accusations=[Player.RANOMI_24, Player.SANDER_24, Player.FROUKJE_24, Player.ANKE_24]),
    Player.DANIEL_24: TestInput({18: 6}),
    Player.FROUKJE_24: TestInput({10: 4}, accusations=[Player.ANNICK_24, Player.DANIEL_24]),
    Player.SARAH_24: TestInput({11: 4}, accusations=[Player.FROUKJE_24, Player.RANOMI_24, Player.DANIEL_24, Player.SANDER_24]),
    Player.SANDER_24: TestInput(accusations=[Player.SOY_24, Player.FROUKJE_24, Player.SARAH_24, Player.ANNICK_24]),
    Player.ANKE_24: TestInput({1: 2}, accusations=[Player.ANNICK_24, Player.FROUKJE_24, Player.NABIL_24, Player.SANDER_24, Player.SARAH_24, Player.SOY_24]),
    Player.JURRE_24: TestInput(accusations=[Player.ANKE_24, Player.DANIEL_24, Player.NABIL_24, Player.RANOMI_24, Player.SANDER_24, Player.SARAH_24, Player.SOY_24]),
    Player.ANNICK_24: TestInput({17: 1}, accusations=[Player.FROUKJE_24, Player.RANOMI_24, Player.SARAH_24, Player.SANDER_24]),

}
result1 = Result(DropType.EXECUTION_DROP, [Player.SARAH_24])
episode1 = Episode(players1, result1, input1, questions1)

################
# Aflevering 2
players2 = [Player.ANKE_24, Player.ANNICK_24, Player.DANIEL_24, Player.FROUKJE_24, Player.JURRE_24,
            Player.NABIL_24, Player.RANOMI_24, Player.SANDER_24, Player.SOY_24]
questions2 = {
    # De Mol is een...
    1: Question({
        # Man
        1: [Player.DANIEL_24, Player.JURRE_24, Player.NABIL_24, Player.SANDER_24, Player.SOY_24],
        # Vrouw
        2: [Player.ANKE_24, Player.ANNICK_24, Player.FROUKJE_24, Player.RANOMI_24]
    }),
    # Welke kleur helm droeg de Mol in de staalfabriek?
    5: Question({
        # Blauw
        1: [Player.NABIL_24],
        # Geel
        2: [Player.ANNICK_24],
        # Groen
        3: [Player.RANOMI_24, Player.FROUKJE_24],
        # Oranje
        4: [Player.JURRE_24, Player.ANKE_24],
        # Wit
        5: [Player.SOY_24],
        # Zwart
        6: [Player.SANDER_24]
    }),
    # Heeft de Mol met een dienblad gelopen tijdens de opdracht in de staalfabriek?
    8: Question({
        # Ja
        1: [Player.NABIL_24, Player.JURRE_24, Player.SANDER_24, Player.RANOMI_24, Player.FROUKJE_24, Player.SOY_24],
        # Nee
        2: [Player.ANKE_24, Player.ANNICK_24, Player.DANIEL_24]
    }),
    # Wie is de Mol?
    20: Question({
        1: [Player.ANKE_24],
        2: [Player.ANNICK_24],
        3: [Player.DANIEL_24],
        4: [Player.FROUKJE_24],
        5: [Player.JURRE_24],
        6: [Player.NABIL_24],
        7: [Player.RANOMI_24],
        8: [Player.SANDER_24],
        9: [Player.SOY_24]
    }),
}
input2 = {
    Player.SOY_24: TestInput(accusations=[Player.NABIL_24]),
    Player.NABIL_24: TestInput({20: 4}, accusations=[Player.JURRE_24, Player.RANOMI_24, Player.SANDER_24, Player.FROUKJE_24, Player.SOY_24]),
    Player.FROUKJE_24: TestInput(accusations=[Player.NABIL_24, Player.RANOMI_24, Player.JURRE_24]),
    Player.JURRE_24: TestInput({1: 1}, accusations=[Player.DANIEL_24, Player.ANNICK_24]),
    Player.ANNICK_24: TestInput({5: 5}),
    Player.ANKE_24: TestInput(accusations=[Player.ANNICK_24, Player.FROUKJE_24, Player.RANOMI_24, Player.SOY_24]),
    Player.DANIEL_24: TestInput({8: 1}),
    Player.RANOMI_24: TestInput({20: 9}, accusations=[Player.SOY_24]),
    Player.SANDER_24: TestInput(accusations=[Player.SOY_24, Player.ANNICK_24])
}
result2 = Result(DropType.EXECUTION_DROP, [Player.FROUKJE_24])
episode2 = Episode(players2, result2, input2, questions2)

################
# Aflevering 3
players3 = [Player.ANKE_24, Player.ANNICK_24, Player.DANIEL_24, Player.JURRE_24,
            Player.NABIL_24, Player.RANOMI_24, Player.SANDER_24, Player.SOY_24]
questions3 = {
    # Welke kleur had de quat van de Mol?
    4: Question({
        # Wit
        1: [Player.ANNICK_24, Player.JURRE_24, Player.ANKE_24, Player.SOY_24, Player.NABIL_24, Player.DANIEL_24],
        # Geel
        2: [Player.RANOMI_24, Player.SANDER_24],
    }),
    # Vertrok de Mol als laatste na het aantikken van de tablet, tijdens de opdracht in de duinen?
    5: Question({
        # Ja
        1: [Player.ANNICK_24],
        # Nee
        2: [Player.ANKE_24, Player.DANIEL_24, Player.JURRE_24, Player.NABIL_24, Player.RANOMI_24, Player.SANDER_24, Player.SOY_24],
    }),
    # Diende het team van de Mol het codewoord in op de ijsbreker?
    18: Question({
        # Ja
        1: [Player.SOY_24, Player.DANIEL_24, Player.JURRE_24],
        # Nee
        2: [Player.ANKE_24, Player.ANNICK_24, Player.NABIL_24, Player.RANOMI_24, Player.SANDER_24],
    }),
    # Wie is de Mol?
    20: Question({
        1: [Player.ANKE_24],
        2: [Player.ANNICK_24],
        3: [Player.DANIEL_24],
        4: [Player.JURRE_24],
        5: [Player.NABIL_24],
        6: [Player.RANOMI_24],
        7: [Player.SANDER_24],
        8: [Player.SOY_24]
    }),
}
input3 = {
    Player.SOY_24: TestInput({4: 1}, jokers=1, accusations=[Player.NABIL_24]),
    Player.NABIL_24: TestInput({5: 2}, accusations=[Player.ANNICK_24]),
    Player.ANNICK_24: TestInput({20: 6}, jokers=1, accusations=[Player.RANOMI_24]),
    Player.RANOMI_24: TestInput(jokers=1, accusations=[Player.SOY_24, Player.ANNICK_24]),
    Player.JURRE_24: TestInput({18: 1}, jokers=2, accusations=[Player.RANOMI_24, Player.NABIL_24, Player.ANNICK_24, Player.DANIEL_24]),
    Player.DANIEL_24: TestInput(jokers=1, accusations=[Player.RANOMI_24, Player.SOY_24, Player.ANNICK_24])
}
result3 = Result(DropType.EXECUTION_DROP, [Player.SANDER_24])
episode3 = Episode(players3, result3, input3, questions3)

################
# Aflevering 4
players4 = [Player.ANKE_24, Player.ANNICK_24, Player.DANIEL_24, Player.JURRE_24,
            Player.NABIL_24, Player.RANOMI_24, Player.SOY_24]
questions4 = {
    # Wat is de geboorteplaats van de Mol?
    2: Question({
        # Eindhoven
        1: [Player.SOY_24],
        # Heerenveen
        2: [Player.ANKE_24],
        # Hilversum
        3: [Player.ANNICK_24],
        # Luxemburg
        4: [Player.DANIEL_24],
        # Sauwerd
        5: [Player.RANOMI_24],
        # Waalwijk
        6: [Player.NABIL_24],
        # Wageningen
        7: [Player.JURRE_24]
    }),
    # Als hoeveelste betrad de Mol het doolhof?
    5: Question({
        1: [Player.DANIEL_24],
        2: [Player.NABIL_24],
        3: [Player.JURRE_24],
        4: [Player.ANKE_24],
        5: [Player.ANNICK_24],
        6: [Player.RANOMI_24],
        7: [Player.SOY_24]
    }),
    # In welke groep zat de Mol tijdens de opdracht met de badeend?
    13: Question({
        # In de groep met 2 kandidaten
        1: [Player.DANIEL_24, Player.ANNICK_24],
        # In de groep met 5 kandidaten
        2: [Player.ANKE_24, Player.DANIEL_24, Player.RANOMI_24, Player.NABIL_24, Player.JURRE_24]
    }),
    # Heeft de Mol het kistje geopend tijdens de opdracht met de badeend?
    15: Question({
        # Ja
        1: [Player.JURRE_24],
        # Nee
        2: [Player.DANIEL_24, Player.ANNICK_24, Player.ANKE_24, Player.DANIEL_24, Player.RANOMI_24, Player.NABIL_24]
    }),
    # Wie is de Mol?
    20: Question({
        1: [Player.ANKE_24],
        2: [Player.ANNICK_24],
        3: [Player.DANIEL_24],
        4: [Player.JURRE_24],
        5: [Player.NABIL_24],
        6: [Player.RANOMI_24],
        7: [Player.SOY_24]
    }),
}
input4 = {
    Player.NABIL_24: TestInput(accusations=[Player.RANOMI_24]),
    Player.DANIEL_24: TestInput({5: 3}, accusations=[Player.JURRE_24, Player.RANOMI_24, Player.SOY_24, Player.ANNICK_24]),
    Player.ANNICK_24: TestInput({2: 4}, accusations=[Player.DANIEL_24]),
    Player.RANOMI_24: TestInput({13: 2}, accusations=[Player.SOY_24, Player.ANNICK_24]),
    Player.SOY_24: TestInput({15: 2}),
    Player.ANKE_24: TestInput({20: 5}, accusations=[Player.RANOMI_24, Player.NABIL_24, Player.SOY_24])
}
result4 = Result(DropType.EXECUTION_DROP, [Player.ANNICK_24])
episode4 = Episode(players4, result4, input4, questions4)

################
# Aflevering 5
players5 = [Player.ANKE_24, Player.DANIEL_24, Player.JURRE_24, Player.NABIL_24, Player.RANOMI_24, Player.SOY_24]
result5 = Result(DropType.NO_DROP_NOR_SCREENS, players5)
episode5 = Episode(players5, result5, dict(), dict())

################
# Aflevering 6
players6 = [Player.ANKE_24, Player.DANIEL_24, Player.JURRE_24, Player.NABIL_24, Player.RANOMI_24, Player.SOY_24]
questions6 = {
    # Als welk beroep werd de Mol afgebeeld tijdens de opdracht in het Lord Milner hotel?
    9: Question({
        # Bankier
        1: [Player.SOY_24],
        # Barman
        2: [Player.JURRE_24],
        # Chauffeur
        3: [Player.NABIL_24],
        # Conducteur
        4: [Player.ANKE_24],
        # Pastoor
        5: [Player.DANIEL_24],
        # Schooljuf
        6: [Player.RANOMI_24],
    }),
    # Wat zat er in de envelop die de Mol opende aan het einde van de opdracht in het Lord Milner hotel?
    14: Question({
        # Geld
        1: [Player.DANIEL_24],
        # Joker
        2: [Player.JURRE_24, Player.ANKE_24],
        # De Mol opende geen envelop
        3: [Player.RANOMI_24, Player.NABIL_24, Player.SOY_24],
    }),
    # Wie is de Mol?
    15: Question({
        1: [Player.ANKE_24],
        2: [Player.DANIEL_24],
        3: [Player.JURRE_24],
        4: [Player.NABIL_24],
        5: [Player.RANOMI_24],
        6: [Player.SOY_24]
    }),
    # Als hoeveelste liep de Mol weg van de test voordat de roadtrip begon?
    16: Question({
        # Als eerste
        1: [Player.DANIEL_24],
        # Als tweede
        2: [Player.JURRE_24],
        # Als derde
        3: [Player.SOY_24],
        # Als vierde
        4: [Player.RANOMI_24],
        # Als vijfde
        5: [Player.NABIL_24],
        # Als zesde
        6: [Player.ANKE_24],
    }),
    # Wat was het kenteken van de auto waarin de Mol zat tijdens de roadtrip?
    17: Question({
        # KG 16 SV GP
        1: [Player.RANOMI_24, Player.NABIL_24, Player.JURRE_24],
        # KG 24 YJ GP
        2: [Player.SOY_24, Player.DANIEL_24, Player.ANKE_24],
    }),
    # Hoeveel eieren heeft de Mol geraakt tijdens de opdracht op eieren schieten?
    19: Question({
        # 0
        1: [Player.RANOMI_24, Player.ANKE_24, Player.DANIEL_24],
        # 2
        2: [],
        # 4
        3: [],
        # 1
        4: [Player.NABIL_24, Player.JURRE_24],
        # 3
        5: [],
        # 5
        6: [Player.SOY_24],
    }),
    # Heeft de Mol diens kist meegenomen tijdens de roadtrip?
    20: Question({
        # Ja
        1: [Player.ANKE_24, Player.NABIL_24, Player.RANOMI_24, Player.SOY_24],
        # Nee
        2: [Player.DANIEL_24, Player.JURRE_24],
    }),
}
input6 = {
    Player.DANIEL_24: TestInput(immunity=True, accusations=[Player.JURRE_24]),
    Player.JURRE_24: TestInput({9: 1}, jokers=1, immunity=True, accusations=[Player.SOY_24]),
    Player.SOY_24: TestInput({15: 4, 19: 4}),
    Player.RANOMI_24: TestInput({14: 3, 17: 2}, jokers=1, accusations=[Player.SOY_24]),
    Player.NABIL_24: TestInput({20: 1}, accusations=[Player.ANKE_24, Player.RANOMI_24]),
    Player.ANKE_24: TestInput({16: 5}, accusations=[Player.NABIL_24, Player.RANOMI_24, Player.SOY_24]),
}
result6 = Result(DropType.EXECUTION_DROP, [Player.NABIL_24])
episode6 = Episode(players6, result6, input6, questions6)

################
# Summary
season24 = Season(
    players1,
    {
        1: episode1,
        2: episode2,
        3: episode3,
        4: episode4,
        5: episode5,
        6: episode6
    }
)
