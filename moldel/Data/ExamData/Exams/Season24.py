from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput

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
    Player.DANIEL_24: TestInput(jokers=1, accusations=[
                                Player.RANOMI_24, Player.SOY_24, Player.ANNICK_24])
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
    Player.ANKE_24: TestInput({20: 5}, accusations=[
                              Player.RANOMI_24, Player.NABIL_24, Player.SOY_24])
}
result4 = Result(DropType.EXECUTION_DROP, [Player.ANNICK_24])
episode4 = Episode(players4, result4, input4, questions4)

################
# Aflevering 5
players5 = [Player.ANKE_24, Player.DANIEL_24, Player.JURRE_24,
            Player.NABIL_24, Player.RANOMI_24, Player.SOY_24]
result5 = Result(DropType.NO_DROP_NOR_SCREENS, players5)
episode5 = Episode(players5, result5, dict(), dict())

################
# Aflevering 6
players6 = [Player.ANKE_24, Player.DANIEL_24, Player.JURRE_24,
            Player.NABIL_24, Player.RANOMI_24, Player.SOY_24]
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
    })
}
input6 = {
    Player.DANIEL_24: TestInput(immunity=True, accusations=[Player.JURRE_24]),
    Player.JURRE_24: TestInput({9: 1}, jokers=1, immunity=True, accusations=[Player.SOY_24]),
    Player.SOY_24: TestInput({15: 4, 19: 4}),
    Player.RANOMI_24: TestInput({14: 3, 17: 2}, jokers=1, accusations=[Player.SOY_24]),
    Player.NABIL_24: TestInput({20: 1}, accusations=[Player.ANKE_24, Player.RANOMI_24]),
    Player.ANKE_24: TestInput({16: 5}, accusations=[
                              Player.NABIL_24, Player.RANOMI_24, Player.SOY_24])
}
result6 = Result(DropType.EXECUTION_DROP, [Player.NABIL_24])
episode6 = Episode(players6, result6, input6, questions6)

################
# Aflevering 7
players7 = [Player.ANKE_24, Player.DANIEL_24,
            Player.JURRE_24, Player.RANOMI_24, Player.SOY_24]
questions7 = {
    # Welke kleur heeft de Mol in het doolhof?
    1: Question({
        # Blauw
        1: [Player.ANKE_24],
        # Geel
        2: [Player.DANIEL_24],
        # Groen
        3: [Player.SOY_24],
        # Rood
        4: [Player.RANOMI_24],
        # Zwart
        5: [Player.JURRE_24],
    }),
    # Wat is het lievelingseten van de Mol?
    3: Question({
        # Curry
        1: [],
        # Kipsate
        2: [],
        # Pannenkoeken
        3: [Player.RANOMI_24],
        # Pasta Carbonara
        4: [Player.JURRE_24],
        # Rendang, spruitjes, pizza, quattro formaggi
        5: [],
    }),
    # Naast wie stond de Mol tijdens de uitleg over de paraglide opdracht?
    5: Question({
        # Anke en Jurre
        1: [Player.SOY_24],
        # Anke en Ranomi
        2: [Player.DANIEL_24],
        # Daniel
        3: [Player.RANOMI_24],
        # Daniel en Soy
        4: [Player.ANKE_24],
        # Soy
        5: [Player.JURRE_24],
    }),
    # Welke kleur helm droeg de Mol tijdens het paragliden?
    6: Question({
        # Rood
        1: [Player.DANIEL_24],
        # Wit
        2: [Player.RANOMI_24],
        # Zwart
        3: [Player.ANKE_24, Player.SOY_24, Player.JURRE_24],
    }),
    # Als hoeveelste ging de Mol paragliden?
    7: Question({
        # Eerste
        1: [Player.RANOMI_24],
        # Tweede
        2: [Player.SOY_24],
        # Derde
        3: [Player.JURRE_24],
        # Vierde
        4: [Player.DANIEL_24],
        # Vijfde
        5: [Player.ANKE_24],
    }),
    # In welk vak eindigde de Mol na het paragliden?
    8: Question({
        # Vak 1
        1: [Player.DANIEL_24],
        # Vak 2
        2: [Player.ANKE_24],
        # Vak 3
        3: [Player.JURRE_24],
        # Vak 4
        4: [Player.RANOMI_24],
        # Vak 5
        5: [Player.SOY_24],
    }),
    # Wat heeft de Mol het liefst altijd bij zich?
    10: Question({
        # Ketting
        1: [],
        # Oplader
        2: [],
        # Powerbank
        3: [],
        # Telefoon
        4: [],
    }),
    # Had de Mol schoenen aan tijdens de opdracht op het strand?
    12: Question({
        # Ja
        1: [Player.ANKE_24, Player.RANOMI_24, Player.SOY_24],
        # Nee
        2: [Player.JURRE_24, Player.DANIEL_24],
    }),
    # Met wie had Jurre een molafspraak?
    17: Question({
        1: [Player.ANKE_24],
        2: [Player.DANIEL_24],
        3: [Player.JURRE_24],
        4: [Player.RANOMI_24],
        5: [Player.SOY_24],
    }),
    # Hoeveel jokers heeft de Mol ingezet voor de test?
    18: Question({
        # 1 joker
        1: [Player.ANKE_24, Player.DANIEL_24, Player.JURRE_24, Player.RANOMI_24],
        # 2 jokers
        2: [Player.SOY_24],
    }),
    # Wie is de Mol?
    20: Question({
        1: [Player.ANKE_24],
        2: [Player.DANIEL_24],
        3: [Player.JURRE_24],
        4: [Player.RANOMI_24],
        5: [Player.SOY_24],
    })
}
input7 = {
    Player.SOY_24: TestInput(
        {1: 4, 5: 3, 7: 1, 8: 4, 12: 1, 17: 4, 20: 4},
        jokers=2,
        accusations=[Player.JURRE_24, Player.RANOMI_24]
    ),
    Player.JURRE_24: TestInput(
        {17: 1, 20: 2},
        jokers=1,
        accusations=[Player.DANIEL_24]
    ),
    Player.DANIEL_24: TestInput(
        {3: 4, 5: 3, 12: 2, 17: 3, 20: 3},
        jokers=1,
        accusations=[Player.JURRE_24]
    ),
    Player.ANKE_24: TestInput(
        {1: 4, 3: 3, 5: 3, 7: 1, 8: 4, 17: 4, 20: 4},
        jokers=1,
        accusations=[Player.RANOMI_24, Player.SOY_24]
    ),
    Player.RANOMI_24: TestInput(
        {1: 5, 3: 4, 5: 2, 6: 3, 7: 2, 8: 1, 12: 1, 20: 5},
        jokers=1,
        accusations=[Player.SOY_24]
    )
}
result7 = Result(DropType.EXECUTION_DROP, [Player.ANKE_24])
episode7 = Episode(players7, result7, input7, questions7)

################
# Aflevering 8
players8 = [Player.DANIEL_24, Player.JURRE_24, Player.RANOMI_24, Player.SOY_24]
result8 = Result(DropType.NO_DROP_NOR_SCREENS, players8)
episode8 = Episode(players8, result8, dict(), dict())

################
# Aflevering 9
# (executie)
players9a = [Player.DANIEL_24, Player.JURRE_24,
             Player.RANOMI_24, Player.SOY_24]
input9a = {
    Player.DANIEL_24: TestInput(accusations=[Player.JURRE_24]),
    Player.JURRE_24: TestInput(immunity=True),
    Player.RANOMI_24: TestInput(accusations=[Player.SOY_24]),
}
result9a = Result(DropType.EXECUTION_DROP, [Player.SOY_24])
episode9a = Episode(players9a, result9a, input9a, dict())

################
# Aflevering 9
# (finale test)
players9b = [Player.DANIEL_24, Player.JURRE_24, Player.RANOMI_24]
questions9b = {
    # De Mol is een...
    1: Question({
        # Man
        1: [Player.JURRE_24, Player.DANIEL_24],
        # Vrouw
        2: [Player.RANOMI_24],
    }),
    # In welke kleur kist zat de Mol opgesloten?
    3: Question({
        # Blauw
        1: [Player.RANOMI_24],
        # Groen
        2: [Player.JURRE_24],
        # Rood
        3: [Player.DANIEL_24],
    }),
    # Hoeveel levens is de Mol kwijtgeraakt tijdens de opdracht in de staalfabriek?
    7: Question({
        # Geen levens
        1: [Player.DANIEL_24],
        # Eén leven
        2: [],
    }),
    # Met wie vormde de Mol een team op de Ijsbreker?
    12: Question({
        # Anke en Annick
        1: [Player.RANOMI_24],
        # Daniel en Soy
        2: [Player.JURRE_24],
        # Jurre en Soy
        3: [Player.DANIEL_24],
    }),
    # Als hoeveelste betrad de Mol het doolhof met de fruitkratten?
    15: Question({
        # Als eerste
        1: [Player.DANIEL_24],
        # Als derde
        2: [],
        # Als zesde
        3: [],
    }),
    # Hoeveel pakbonnen heeft de Mol in handen gehad in het doolhof?
    16: Question({
        # Twee
        1: [],
        # Vier
        2: [],
        # Vijf
        3: [Player.DANIEL_24],
    }),
    # Als welk beroep werd de Mol afgebeeld in het Lord Milner Hotel?
    20: Question({
        # Barman
        1: [Player.JURRE_24],
        # Pastoor
        2: [Player.DANIEL_24],
        # Schooljuf
        3: [Player.RANOMI_24],
    }),
    # Hoeveel tegenstanders heeft de Mol geraakt tijdens de lasergame opdracht?
    35: Question({
        # Nul
        1: [],
        # Twee
        2: [],
        # Drie
        3: [Player.DANIEL_24],
    }),
    # Wie is de Mol?
    40: Question({
        1: [Player.DANIEL_24],
        2: [Player.JURRE_24],
        3: [Player.RANOMI_24],
    })
}
input9b = {
    Player.JURRE_24: TestInput({1: 1, 12: 3, 15: 1, 40: 1}, accusations=[Player.DANIEL_24]),
    Player.DANIEL_24: TestInput({3: 2, 20: 1, 40: 2}, accusations=[Player.JURRE_24]),
    Player.RANOMI_24: TestInput({7: 1, 16: 3, 35: 3, 40: 1}, accusations=[Player.DANIEL_24]),
}
result9b = Result(DropType.NO_DROP_NOR_SCREENS, players9b)
episode9b = Episode(players9b, result9b, input9b,
                    questions9b, num_questions=40)

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
        6: episode6,
        7: episode7,
        8: episode8,
        8.5: episode9a,
        9: episode9b
    }
)
