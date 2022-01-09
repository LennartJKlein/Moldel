# Moldel

> _'Wie is de Mol?' is een programma op Nederland 1 dat elk jaar wordt uitgezonden sind 1999. In dit programma moeten kandidaten opdrachten doen waarmee je geld voor de pot kunt verdienen. Echter heb je ook een saboteur, die ook wel de 'Mol' wordt genoemd. De 'Mol' probeert te verhinderen dat er geld verdient wordt. De kandidaten moeten deze 'Mol' proberen te ontmaskeren. Bijna elke aflevering is er een test met vragen over de 'Mol' en de kandidaat die dan het minst weet over de 'Mol' valt af. Uiteindelijk blijven er op het einde 3 kandidaten over en degene die het meest weet over de 'Mol' is de winnaar van het spel en krijgt het bedrag dat in de pot zit._

Het **Moldel** is een algoritme, bedacht door Haico ([Multifacio](https://github.com/Multifacio)) dat voor elke kandidaat de waarschijnlijkheid berekent dat deze de 'Mol' is. Deze score komt tot stand door de voorspellingen van de volgende 'layers' te combineren:

- **Exam Drop Layer**: Kijkt naar antwoorden op de test en wie er afvalt.
- **Exam Pass Layer**: Kijkt wie hoeveel jokers bij de test heeft ingezet.
- **Wikipedia Layer**: Kijkt naar wikipediapagina's van de kandidaten. Kijkt naar beroepen, aantal woorden, etc.
- **Social Media Layer**: Kijkt naar social media activiteit. Gelekte foto's, activiteit van kanidaten tijdens de opnameperiode, aanwezigheid van de kandidaat, etc.
- **Appearance Layer**: Kijkt naar hoe vaak een kandidaat in beeld komt. [Mattijn van Hoek](https://github.com/mattijn/widm) ontdekte een tendens dat de Mol relatief weinig (onderste 20%) in beeld is in de eerste 5 afleveringen.

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
