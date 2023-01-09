# Moldel

Een algoritme om de Mol te voorspellen.

## 🔦 Nieuwste voorspelling (s24e0, 2023)

![Voorspelling na aflevering 1, seizoen 24 (2023)](https://github.com/LennartJKlein/Moldel/blob/master/results/Season%2024%20(2023)/s24e1.png?raw=true)

## 📺 Over Wie is de Mol

> _'Wie is de Mol?' is een programma op Nederland 1 dat elk jaar wordt uitgezonden sind 1999. In dit programma moeten kandidaten opdrachten doen waarmee je geld voor de pot kunt verdienen. Echter heb je ook een saboteur, die ook wel de 'Mol' wordt genoemd. De 'Mol' probeert te verhinderen dat er geld verdient wordt. De kandidaten moeten deze 'Mol' proberen te ontmaskeren. Bijna elke aflevering is er een test met vragen over de 'Mol' en de kandidaat die dan het minst weet over de 'Mol' valt af. Uiteindelijk blijven er op het einde 3 kandidaten over en degene die het meest weet over de 'Mol' is de winnaar van het spel en krijgt het bedrag dat in de pot zit._

## 💡 Over het project

Het **Moldel** is een algoritme, bedacht door Haico ([Multifacio](https://github.com/Multifacio)) dat voor elke kandidaat de waarschijnlijkheid berekent dat deze de 'Mol' is. Deze score komt tot stand door de voorspellingen van de volgende 'layers' te combineren:

- **Exam Drop Layer**: Kijkt voor elke kandidaat of de afvaller van de aflevering antwoorden op hem/haar had ingevuld tijdens de test.
- **Exam Accusations Layer**: Kijkt naar gesproken beschuldigingen tijdens de test. Voor elke kandidaat wordt gekeken hoe vaak hij/zij wordt verdacht, of hij/zij door de afvaller wordt verdacht, of hij/zij de afvaller verdacht en of hij/zij dezelfde beschuldigingen als andere spelers doet.
- **Exam Pass Layer**: Kijkt voor elke kandidaat hoeveel jokers hij/zij heeft ingezet bij de test.
- **Money Layer**: Kijkt voor elke kandidaat welke invloed hij/zij had op het bedrag in de pot.
- **Wikipedia Layer**: Kijkt voor elke kandidaat naar diens beroep en de grootte van diens wikipedia-pagina.
- **Social Media Layer**: Kijkt naar social media activiteit. Gelekte foto's, activiteit van kandidaten tijdens de opnameperiode, afwezigheid van de kandidaat, etc.
- **Appearance Layer**: Kijkt naar hoe veel een kandidaat in beeld komt. ©[Mattijn van Hoek](https://github.com/mattijn/widm)

## 🛠 Installeren

Je hebt een aantal programma's, software en pakketten nodig om het Moldel uit te voeren op je computer.

### Installeer deze software

- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Python v3.9](https://www.python.org/downloads/)
- [PIP](https://pypi.org/project/pip/)
- [Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

### Download de bestanden van deze repository

```python
git clone https://github.com/LennartJKlein/Moldel.git
```

### Installeer modules voor Python in deze volgorde

```python
pip install aenum
pip install numpy
pip install scipy
pip install k-means-constrained
pip install sklearn
pip install opencv-python
pip install jenkspy
pip install rootpath
pip install iteround
pip install matplotlib
pip install progress
pip install seaborn

brew install enchant # macOS
sudo apt-get install libenchant1c2a # Windows/Ubuntu

pip install pyenchant
conda install -c conda-forge dlib
pip install cmake
pip install face-recognition
```

## 🚀 Uitvoeren

Nu is het zo ver; laat het algoritme op basis van de 5 tactieken een kansberekening maken wie de Mol is! Ga naar de hoofdmap van het project en voer het commando uit:

`python moldel predict [SEASON] [LATEST EPISODE] [--file]`

_De optie `--file` is optioneel en zorgt ervoor dat de uitkomst als bestand wordt opgeslagen, ipv als popup geopend._

## 📝 Nieuwe data invoeren

### Exam Drop Layer

### Exam Pass Layer

### Exam Accusations Layer

Alleen gesproken beschuldigingen opschrijven.

### Wikipedia Layer

Kopieer de wikipediapagina van de persoon van titel tot en met de categorieën onderaan diens pagina. Plak dit in een .txt bestand in de map `WikiFiles`. Voeg de nieuwe file toe in het bestand `Linker.py` om hem te koppelen aan de bijbehorende kandidaat.

### Social Media Layer

### Appearance Layer

In het Moldel wordt **elke** aflevering geanalyseerd hoe vaak iemand in beeld komt. Je moet voor elke nieuwe aflevering de volgende stappen volgen:

1. Zorg dat voor elke kandidaat van het seizoen een portretfoto in de map `Data/AppearanceData/Faces` staat
2. Voeg de aflevering die geanalyseerd moet worden toe in de map `Data/AppearanceData`
3. Pas de instellingen in het bestand `Layers/Appearance/VideoParserSettings.py` aan, zodat ze kloppen voor jouw seizoen en aflevering.
4. Laat de aflevering automatisch analyseren vanuit de map 'moldel' met het commando: `python -m Layers.Appearance.VideoParser`

Hoe veel een kandidaat in beeld komt tijdens deze aflevering, is nu opgeslagen in het Moldel.

## 📝 Trainen van het geheugen van het Moldel

Het Moldel kun je trainen, zodat z'n geheugen groter wordt. Doe dit elke keer dat een seizoen is afgelopen en de Mol bekend is, om dat seizoen aan zijn geheugen toe te voegen.

1. Pas de instellingen in het bestand `Settings.py` aan, zodat alle afgeronde seizoenen zijn opgenomen.
2. Voer uit: `python moldel train [LAYER]`

## 📚 Verdiepende uitleg van Multifacio

[In de README en Thesis van Haico lees je meer over de verschillende layers en tactieken van het Moldel](https://github.com/Multifacio/Moldel/tree/master/readmes)
