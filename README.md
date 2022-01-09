# Moldel

> 'Wie is de Mol?' is een programma op Nederland 1 dat elk jaar wordt uitgezonden sind 1999. In dit programma moeten kandidaten opdrachten doen waarmee je geld voor de pot kunt verdienen. Echter heb je ook een saboteur, die ook wel de 'Mol' wordt genoemd. De 'Mol' probeert te verhinderen dat er geld verdient wordt. De kandidaten moeten deze 'Mol' proberen te ontmaskeren. Bijna elke aflevering is er een test met vragen over de 'Mol' en de kandidaat die dan het minst weet over de 'Mol' valt af. Uiteindelijk blijven er op het einde 3 kandidaten over en degene die het meest weet over de 'Mol' is de winnaar van het spel en krijgt het bedrag dat in de pot zit.

Het **Moldel** is een programma, bedacht door Haico ([Multifacio](https://github.com/Multifacio)) dat voor elke kandidaat de waarschijnlijkheid berekend dat deze de 'Mol' is. Deze score komt tot stand door de voorspellingen van de volgende layers te combineren:

- Exam Drop Layer: Deze bepaalt wie de 'Mol' is op basis van hoe afvallers hun vragen hebben ingevuld (kandidaten waarop afvallers zitten zijn vaak niet de 'Mol').
- Exam Pass Layer: Deze bepaalt wie de 'Mol' is op basis van hoeveel jokers de kandidaten tijdens de test hebben ingezet (kandidaten die meer jokers hebben ingezet zijn vaak niet de 'Mol'). De Exam Pass Layer is ontstaan door een opmerking van Dr. Jasper de Jong, die mij geïnspireerd heeft tot deze layer.
- Wikipedia Layer: Deze bepaalt wie de 'Mol' is op basis van de kandidaten wikipedia pagina's voordat het seizoen begon. Via de wikipedia pagina's proberen ze kandidaten te linken aan bepaalde beroepen en op basis hiervan en hoeveel woorden in hun wikipedia pagina staan probeert deze layer te voorspellen wie de 'Mol' is.
- Social Media Layer: Deze layer geeft kandidaten een lagere/hogere kans op basis van de social media analyse door [Jaap van Zessen](http://www.jaapvanzessen.nl/tag/wie-is-de-mol/). Hierbij wordt onder andere gekeken naar foto's die gelekt zijn, hoe actief kandidaten op social media (Facebook, Twitter, Youtube, etc.) waren tijdens de opname periode en andere informatie die aantoont dat een kandidaat wel/niet aanwezig was tijdens een later stadium van de opname periode.
- Appearance Layer: Het idee van deze layer komt van [Mattijn van Hoek](https://github.com/mattijn/widm). Deze layer probeert te voorspellen wie de 'Mol' is op basis van hoe vaak de 'Mol' in beeld komt tijdens de eerste 4 afleveringen (de 'Mol' komt vaak minder in beeld).

## 🛠 Installeren

Voer de volgende commando's uit om op jouw computer het moldel te laten draaien:

### Installeer Git

- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Installeer Python en twee package managers

- [Python v3.9](https://www.python.org/downloads/)
- [PIP](https://pypi.org/project/pip/)
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

### Download de bestanden van deze repository

`git clone https://github.com/LennartJKlein/Moldel.git`

### Installeer de nodige Python modules in deze volgorde

`pip install aenum`

`pip install numpy`

`pip install scipy`

`pip install k-means-constrained`

`pip install sklearn`

`pip install opencv-python`

`pip install jenkspy`

`pip install rootpath`

`pip install iteround`

`pip install matplotlib`

`pip install seaborn`

`brew install enchant` (MacOS) of `sudo apt-get install libenchant1c2a` (Windows/Ubuntu)

`pip install pyenchant`

`conda install -c conda-forge dlib`

`pip install cmake`

`pip install face-recognition`

## 🎯 Uitvoeren

Nu is het zo ver; laat het programma op basis van de 5 tactieken een kansberekening maken wie de Mol is!

Ga naar de hoofdmap van het project en voer uit:

`python moldel [SEASON] [LATEST EPISODE] [--file]`

De optie `--file` is optioneel en zorgt ervoor dat de uitkomst als bestand wordt opgeslagen, ipv als popup geopend.

## 📚 Verdiepende uitleg van Multifacio

[In de README en Thesis van Haico lees je meer over de verschillende layers en tactieken van het Moldel](https://github.com/Multifacio/Moldel/tree/master/readmes)
