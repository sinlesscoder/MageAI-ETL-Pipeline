## Pandas Profiling

### Description

- `pandas_profiling` is a Python module that leverages pandas to learn insights about the data quality of your columns and rows to give you a comprehensive web-based report that is saved a `.html` file.

### Features

- Summary Statistics for Each Column
- Feature Interaction (Correlation Plots)
- Missing Value Analysis
- Duplicate Analysis

### Installation

- Via `pip`

```bash
pip install pandas-profiling
```

### Basic Usage

```python
import pandas_profiling

# Assuming you have a DataFrame, you can create a profile_report

df.profile_report()
```
