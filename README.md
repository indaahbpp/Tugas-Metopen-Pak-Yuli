# Rainfall–Flood Discharge Analysis

## Overview

This repository contains datasets, analysis scripts, figures, and supporting files used in my undergraduate research on the relationship between rainfall characteristics and flood discharge estimation using hydrological analysis methods.

The repository was created as part of the Reproducible Research assignment. It demonstrates how hydrological data and computational analysis can be organized to ensure transparency, reproducibility, and verification of research findings.

---

## Research Objective

The objectives of this study are:

- Analyze the relationship between maximum rainfall and flood discharge.
- Estimate flood discharge using the Rational Method.
- Evaluate the influence of rainfall intensity on peak flood discharge.
- Develop statistical and regression models to describe the relationship between rainfall and flood discharge.

---

## Repository Structure

```
rainfall-flood-discharge-analysis/
│
├── data/
│   ├── Rainfall dataset (.xlsx)
│   ├── Flood discharge dataset
│   ├── Processed data
│   └── Supporting files
│
├── scripts/
│   └── analysis.py
│
├── figures/
│   ├── Scatter plots
│   ├── Regression plots
│   ├── Correlation matrix
│   └── Flood discharge graphs
│
├── README.md
├── requirements.txt
├── LICENSE
└── LICENSE-DATA.md
```

---

## Data

The repository contains hydrological data collected from rainfall records and flood discharge estimation.

Variables include:

- Maximum daily rainfall (mm)
- Rainfall intensity (mm/hour)
- Catchment area (km²)
- Runoff coefficient
- Time of concentration (hour)
- Estimated flood discharge (m³/s)

---

## Analysis

The analysis includes:

- Descriptive statistics
- Rainfall intensity calculation using the Mononobe equation
- Flood discharge estimation using the Rational Method
- Correlation analysis
- Linear regression
- Multiple regression
- Data visualization using scatter plots and regression graphs

---

## Software

The analysis was conducted using Python.

Required packages are listed in:

```
requirements.txt
```

---

## How to Run

1. Clone this repository

```
git clone https://github.com/yourusername/rainfall-flood-discharge-analysis.git
```

2. Install required packages

```
pip install -r requirements.txt
```

3. Run the analysis

```
python scripts/analysis.py
```

---

## License

- Source code is licensed under the MIT License.
- Dataset is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0).

---

## Author

**Indah Berlian**

Department of Civil and Environmental Engineering

IPB University

2026
