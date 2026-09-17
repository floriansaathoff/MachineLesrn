# MachineLesrn

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pandas numpy matplotlib scikit-learn fire jupyter
```

## `exercise.ipynb`

Bearbeitete Übung zu Visualisierung mit `matplotlib` und Interpolation der
Fütterungstabelle (`plan_pandas.csv`) mittels linearer bzw. polynomieller
Regression (`numpy`/`sklearn`). Einfach der Reihe nach ausführen
(`Run All`).

## `main.py`

Kommandozeilen-Tool (Abschnitt 7 der Übung), das die Tagesration für ein
beliebiges Alter (in Tagen) anhand des besten Polynom-Fits interpoliert.

```bash
# Tagesration für Tag 90 (Zielgewicht 25 kg, Standard)
python main.py age 90

# Tagesration für Tag 90 bis Tag 96 (7 Tage)
python main.py age 90 --duration=7

# anderes Zielgewicht wählen
python main.py --weight=30 age 90

# Gesamtplan als Grafik exportieren, abgefragte Tage markiert
python main.py age 90 --duration=7 --export=plan.png

# Übersicht aller Optionen
python main.py -- --help
python main.py age -- --help
```