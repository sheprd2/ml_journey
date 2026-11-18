# ml_journey

My machine learning learning journey, one small project at a time.

## Contents

- `rain.py` – exploratory analysis of Indian rainfall data (1901–2015) with pandas. Focuses on the Kerala subdivision: finds the wettest year, computes average monthly rainfall, the overall annual mean, counts years with above-average rainfall, checks for missing values, drops years with missing annual rainfall, computes average annual rainfall per decade, and saves the cleaned Kerala data to `kerala_clean.csv`.
- `plots.py` – visualises the cleaned Kerala data with matplotlib and seaborn: annual rainfall trend with the average line, average monthly rainfall, and average rainfall per decade. Saves `annual_trend.png`, `monthly_trend.png` and `decadal_trend.png`.
- `rainfall in india 1901-2015.csv` – dataset with monthly, seasonal and annual rainfall (mm) per meteorological subdivision.
- `kerala_clean.csv` – output of `rain.py`: Kerala rows with missing annual values removed, plus a `DECADE` column.

## Usage

```bash
pip install pandas matplotlib seaborn
python rain.py    # cleans the data and writes kerala_clean.csv
python plots.py   # reads kerala_clean.csv and saves the charts
```
