# Housing Affordability & Eviction Risk Early Warning System

## Project overview
Build a county-level policy analytics system that identifies areas at elevated risk of housing distress and eviction using public U.S. housing and socioeconomic data.

## Objective
The goal is to help policymakers target limited housing support resources more effectively by ranking counties by near-term risk and simulating intervention strategies.

## Data sources
- ACS / Census API
- HUD CHAS API
- Eviction Lab county data

## Methods
- Data engineering
- Panel / time-series feature engineering
- Classification or regression modeling
- Risk ranking
- Policy targeting analysis
- Fairness / limitations review

## Repo structure
- `data/`: raw, interim, processed datasets
- `notebooks/`: EDA and experiments
- `src/`: reusable Python code
- `app/`: Streamlit app
- `reports/`: figures, tables, and brief

## Setup
```bash
pip install -r requirements.txt
```

## Initial roadmap
1. Acquire and validate data
2. Build county-year panel
3. Engineer features and define target
4. Train baseline model
5. Add policy targeting and dashboard

## Status
In progress