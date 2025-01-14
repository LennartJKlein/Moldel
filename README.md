# Moldel AI

Een algoritme om de Mol te voorspellen.

## 🔦 Nieuwste voorspelling (s25e4, 2024)

![Voorspelling na aflevering 4, seizoen 24 (2024)](https://github.com/LennartJKlein/Moldel/blob/master/results/Season%2025%20(2024)/s25e4.png?raw=true)

## 📺 Over Wie is de Mol

> _'Wie is de Mol?' is een programma op Nederland 1 dat elk jaar wordt uitgezonden sind 1999. In dit programma moeten kandidaten opdrachten doen waarmee je geld voor de pot kunt verdienen. Echter heb je ook een saboteur, die ook wel de 'Mol' wordt genoemd. De 'Mol' probeert te verhinderen dat er geld verdient wordt. De kandidaten moeten deze 'Mol' proberen te ontmaskeren. Bijna elke aflevering is er een test met vragen over de 'Mol' en de kandidaat die dan het minst weet over de 'Mol' valt af. Uiteindelijk blijven er op het einde 3 kandidaten over en degene die het meest weet over de 'Mol' is de winnaar van het spel en krijgt het bedrag dat in de pot zit._

## 💡 Over het project

Het **Moldel** is een algoritme, bedacht door Haico Dorenbos ([Multifacio](https://github.com/Multifacio)) dat voor elke kandidaat de waarschijnlijkheid berekent dat deze de 'Mol' is. Deze score komt tot stand door de voorspellingen van de volgende 'layers' te combineren:

* **Exam Drop Layer**: Kijkt voor elke kandidaat of de afvaller van de aflevering antwoorden op hem/haar had ingevuld tijdens de test.
* **Exam Accusations Layer**: Kijkt naar gesproken beschuldigingen tijdens de test. Voor elke kandidaat wordt gekeken hoe vaak hij/zij wordt verdacht, of hij/zij door de afvaller wordt verdacht, of hij/zij de afvaller verdacht en of hij/zij dezelfde beschuldigingen als andere spelers doet. ©[Lennart Klein](https://github.com/LennartJKlein)
* **Exam Pass Layer**: Kijkt voor elke kandidaat hoeveel jokers hij/zij heeft ingezet bij de test.
* **Money Layer**: Kijkt voor elke kandidaat welke invloed hij/zij had op het bedrag in de pot.
* **Wikipedia Layer**: Kijkt voor elke kandidaat naar diens beroep en de grootte van diens wikipedia-pagina.
* **Social Media Layer**: Kijkt naar social media activiteit. Gelekte foto's, activiteit van kandidaten tijdens de opnameperiode, afwezigheid van de kandidaat, etc.
* **Appearance Layer**: Kijkt naar hoe veel een kandidaat in beeld komt. ©[Mattijn van Hoek](https://github.com/mattijn/widm)

## 🛠 Installeren

Je hebt een aantal programma's, software en pakketten nodig om het Moldel uit te voeren op je computer.

### Installeer deze software

* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Python v3.9 of hoger](https://www.python.org/downloads/)
* [PIP](https://pypi.org/project/pip/)
* [Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

### Download de bestanden van deze repository

```python
git clone https://github.com/LennartJKlein/Moldel.git
```

### Installeer modules voor Python in deze volgorde

```bash
# For macOS (Apple Silicon M1 chip):
arch -x86_64 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
arch -x86_64 /usr/local/bin/brew install enchant

# For macOS (intel chip)
brew install enchant

# For Windows/Ubuntu
sudo apt-get install libenchant1c2a 

# For all platforms
pip install aenum numpy scipy k-means-constrained sklearn scikit-learn opencv-python jenkspy rootpath iteround matplotlib progress seaborn tinify
pip install pyenchant
conda install -c conda-forge dlib
pip install cmake face-recognition
```

## 🚀 Uitvoeren

Nu is het zo ver; laat het algoritme op basis van de 5 tactieken een kansberekening maken wie de Mol is! Ga naar de hoofdmap van het project en voer het commando uit:

 `python moldel predict [SEASON] [LATEST EPISODE] [--file]`

_De optie `--file` is optioneel en zorgt ervoor dat de uitkomst als bestand wordt opgeslagen, ipv als popup geopend._

⚠️ _Let op: voor MacOS met M1 chips dien je bij elke nieuwe terminal eerst dit commando uit te voeren: `export PYENCHANT_LIBRARY_PATH=/opt/homebrew/lib/libenchant-2.dylib`_

## 📝 Nieuwe data invoeren

### Exam Drop Layer

1. Maak een bestand aan in de map `Data/ExamData/Exams` met het nummer van het seizoen.
2. Voeg het pad naar dit nieuwe bestand toe aan `All.py` (in diezelfde map).
3. Vul het bestand met enkel de informatie die tijdens en na de test in de aflevering is. Zie ook [`ModelTechniques.md`](/LennartJKlein/Moldel/blob/master/moldel/Data/ExamData/ModelTechniques.md) voor meer toelichting.

### Exam Pass Layer

1. Maak een bestand aan in de map `Data/ExamData/Exams` met het nummer van het seizoen.
2. Voeg het pad naar dit nieuwe bestand toe aan `All.py` (in diezelfde map).
3. Vul het bestand met enkel de informatie die tijdens en na de test in de aflevering te zien is. Denk aan jokers, vrijstellingen, of er een afvaller is, wie dat is. Zie ook [`ModelTechniques.md`](/LennartJKlein/Moldel/blob/master/moldel/Data/ExamData/ModelTechniques.md) voor meer toelichting.

### Exam Accusations Layer

1. Maak een bestand aan in de map `Data/ExamData/Exams` met het nummer van het seizoen.
2. Voeg het pad naar dit nieuwe bestand toe aan `All.py` (in diezelfde map).
3. Vul de array `accusations` bij elke `TestInput` enkel met de hardop uitgesproken beschuldigingen.

### Money Layer

1. Maak een bestand aan in de map `Data/ExerciseData/Exercises` met het nummer van het seizoen.
2. Voeg het pad naar dit nieuwe bestand toe aan `All.py` (in diezelfde map).
3. Noteer elke opdracht in een aflevering. Noteer daarin het maximaal te halen bedrag. Als er geld is verdiend, voeg per bedrag dan toe wie daar `major` en wie `minor` heeft bijgedragen. Gebruik dit systeem ook als er min-geld is verdiend dat uit de pot gaat. Voor meer info zie de comments bij de [DataClasses](/LennartJKlein/Moldel/blob/master/moldel/Data/ExerciseData/Dataclasses).

### Wikipedia Layer

Kopieer de wikipediapagina van de persoon van titel tot en met de categorieën onderaan diens pagina.

* Plak dit in een .txt bestand in de map `Data/Wikipedia/WikiFiles`.
* Voeg de nieuwe file toe in het bestand `Linker.py` om hem te koppelen aan de bijbehorende kandidaat.

### Social Media Layer

Wanneer uit de social media kanalen van een deelnemer blijkt dat deze persoon niet bij alle opnames van de serie aanwezig kon zijn, is deze persoon niet de Mol. Vul de naam daarom handmatig in in het bestand `Data/SocialMediaData/SocialMediaData.py`.

### Appearance Layer

Het Moldel neemt van de eerste 5 afleveringen mee hoeveel seconden elke kandidaat in beeld komt. Voor elke nieuwe aflevering die je wil laten analyseren moet je de volgende stappen volgen:

1. Zorg dat voor elke kandidaat van het seizoen een portretfoto in de map `Data/Faces` staat
2. Voeg de aflevering die geanalyseerd moet worden toe in de map `Data/AppearanceData`
3. Pas de instellingen in het bestand `Layers/Appearance/VideoParserSettings.py` aan, zodat ze kloppen voor jouw seizoen en aflevering.
4. Voer het volgende commando uit vanuit de map `moldel`, zodat de aflevering automatisch geanalyseerd wordt: `python -m Layers.Appearance.VideoParser`

Hoe veel een kandidaat in beeld komt tijdens deze aflevering, is nu opgeslagen in het Moldel.

## 📝 Trainen van het geheugen van het Moldel

Het Moldel kun je trainen, zodat z'n geheugen groter wordt. Doe dit elke keer dat een seizoen is afgelopen en de Mol bekend is, om dat seizoen aan zijn geheugen toe te voegen.

1. Pas de instellingen in het bestand `Settings.py` aan, zodat alle afgeronde seizoenen zijn opgenomen.
2. Voer uit: `python moldel train [LAYER]`

## 📚 Verdiepende uitleg van Multifacio

[In de README en thesis van Haico lees je meer over de verschillende layers en tactieken van het Moldel](https://github.com/Multifacio/Moldel/tree/master/readmes)
