# ml_journey

My machine learning learning journey, one small project at a time.

## Contents

- `rain.py` – exploratory analysis of Indian rainfall data (1901–2015) with pandas. Focuses on the Kerala subdivision: finds the wettest year, computes average monthly rainfall, the overall annual mean, counts years with above-average rainfall, checks for missing values, drops years with missing annual rainfall, computes average annual rainfall per decade, and saves the cleaned Kerala data to `kerala_clean.csv`.
- `rainfall in india 1901-2015.csv` – dataset with monthly, seasonal and annual rainfall (mm) per meteorological subdivision.
- `kerala_clean.csv` – output of `rain.py`: Kerala rows with missing annual values removed, plus a `DECADE` column.

## Usage

```bash
pip install pandas
python rain.py
```
