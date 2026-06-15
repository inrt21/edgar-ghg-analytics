# edgar-ghg-analytics-platform
Global GHG Emissions Analytics Platform: Time-Series Forecasting, Clustering and Trend Analysis (EDGAR 1970–2024)
tech stack: Python, Pandas, Scikit-learn, matplotlib, seaborn

Overview
This project maps global emissions while leveraging the United Kingdom as a primary time-series case study. By focusing on the UK's 54-year record, it isolates localized structural breaks and macroeconomic anomalies, providing a rigorous testing ground to evaluate Ordinary Least Squares regression against non-linear forecasting architectures before expanding the time-series models globally.

Key Insights
- Accelerating modern decline: UK emissions have decreased since 1970, but the rate of decline accelerated markedly in the modern era (post-2000), driven by structural shifts in policy and energy and by sudden macroeconomic shocks.
- Emission inequality: The distribution of emissions across countries is extremely right-skewed. A small fraction of industrial nations act as statistical outliers driving global totals, while the majority contribute a negligible baseline - a textbook Pareto pattern.
- Model evolution: OLS linear modeling across the full dataset (1970-2024) introduced bias from the structural flattening effects of the 1970s-80s. Restricting the model to the modern era (2000-2024) improved tracking accuracy but exposed the intrinsic need for non-linear ARIMA structures.

Problem Statement
Global climate strategies and corporate sustainability frameworks rely on accurate GHG forecasting to set actionable reduction targets. Modeling emissions introduces two statistical challenges:
- Temporal non-linearity and structural breaks: Environmental data does not behave linearly. Data from 1970 to the late 1990s carries structural legacy noise (limited regulation, one-off events) that artificially flattens predictive regression slopes. Applying OLS across the entire timeline introduces historical bias, creating a visible discontinuity at the forecast boundary and failing to capture the accelerated decline of the modern era (2000-2024)
- Extreme spatial inequality: Aggregating emissions globally without accounting for country-level variance yields generalized, ineffective models that ignore the heavy-tailed distribution of emitters.
Without isolating modern trends and transitioning from rigid linear fits to adaptive time-series models, stakeholders risk strategic decisions based on flawed projects.

Why It Matters
- Global and geopolitical: Because emissions follow a Pareto distribution, initiatives like the Paris Agreement cannot treat all nations identically. Data-driven modeling lets international bodies identify, monitor, and hold accountable the specific outlier nations driving global trajectories.
- Macroeconomic and business strategy: Sustainability is now a core financial risk factor. As governments implement carbon taxes and cap-and-trade penalties, businesses must project regional emission trends to forecast overhead and head compliance risk. Predictive models also inform supply-chain decisions, shifting logistics and manufacturing away from high-emission, high-tax regions towards areas with sustained structural declines in GHG intensity.

Project Motivation
As an aspiring data scientist with a deep commitment to environmental conservation, this is fundamentally a passion project - an attempt to bridge a personal drive to protect the natural world with the statistical modeling required to understand it. 
Rather than accepting standard visualizations at face value, the project is an intellectual sandbox for exploring how-real world historical shocks break traditional linear modeling. It demonstrates a complete data science lifecycle: identifying the mathematical limitations of a simple linear model, isolating modern data to minimize historical bias, and laying the analytical groundwork for advanced time-series and unsupervised learning. 
This repository is not a static portfolio piece but a living foundation I intend to scale and refine throughout my studies and career as my technical toolkit expands. 

Exploratory Data Analysis
Gas-specific temporal fluctuations (United Kingdom):
- Carbon Dioxide (CO2): A steep downward trajectory, falling from ~675,000 Gg in 1970 to under 300,000 Gg by 2024. Localized dips appear to coincide with major economic contractions such as the 2008 financial crisis and the 2020 COVID-19 lockdowns.
- Nitrous Oxide (N2O): A distinct early anomaly - surging through the 1970s to a peak of ~161 Gg before a sustained decline. This is consistent with the post-war boom in synthetic nitrogen fertilizer use before precision agriculture began stabilizing it in the late 1980s.
- Methane (CH4): A stable, continuous downward trend from 1990 onwards, cutting historical baselines by more than half.
Cross country distribution: The global profile is severely right-skewed - a few outlier nations dominate output while the median nation contributes a statistically negligible amount. Global progress is therefore dictated disproportionately by a few key actors.

Predictive Modeling
Phase 1 - Full period Linear Regression (1970-2024): 
- Approach: OLS Regression across the entire 54-year dataset
- Limitation: The high-emission data of the 1970s-80s pulled the slope flatter than the recent trend, creating a visible discontinuity at the 2025 forecast boundary and overestimating future emissions because the model could not adjust to the modern accelerated decline.
Phase 2 - Modern-Era Isolation (2000-2024):
- Approach: Training data restricted to the modern era to capture the contemporary trajectory.
- Result: Removing late-20th-century legacy noise aligned the model with the modern velocity of decline, projecting an emissions total of approximately 300,000 Gg by 2034

Model Limitations and Roadmap
Even restricted to 2000-2024, linear regression assumes a constant rate of change. Residual analysis suggests errors are not random - a straight line cannot capture changing rates of decline, autocorrelation, or cyclical variation.
Next steps:
- Advanced Time-Series Forecasting (ARIMA/SARIMA): Move from a rigid trend line to a stochastic framework that handles historical momentum, stationarity, and autocorrelation.
- Time-series decomposition: Separate the signal into trend, seasonality, and residual components to isolate true environmental progress from cyclical fluctuation.
- Statistical anomaly detection (z-scores): Flag points sitting 2-3 standard deviations from the rolling mean to automatically profile macro-events such as 2008 and 2020.
- Unsupervised clustering (K-Means): Segment nations into "Emission personas"(e.g. rapidly decarbonizing economies, high-growth industrial nations, negligible-impact baselines) to replace the one-size-fits-all modeling with cluster-specific forecasts.
- Feature engineering and Normalization: Integrate World Bank Population and GDP data to derive per-capita emissions and carbon intensity (emissions per GBP of GDP).
- Interactive dashboard: Deploy a web tool to toggle gases, select clusters, and isolate custom date ranges.
Tech Stack
Language: Python
Libraries: Pandas, Scikit-learn, Matplotlib, Seaborn
Tooling: uv (Environment and dependency management)


## Repository Structure

```text
├── data/                              # EDGAR datasets (raw .xlsx excluded via .gitignore — see below)
│   └── emissions_data.csv             # Consolidated dataset produced by the pipeline
├── src/
│   ├── __init__.py                    # Marks src as a package
│   ├── reader.py                      # Data ingestion & consolidation
│   ├── analytics.py                   # EDA, OLS regression, modern-era segmentation
│   ├── plotting.py                    # Chart generation
│   └── main.py                        # Execution entry point
├── .python-version                    # Pinned Python version
├── pyproject.toml                     # Project metadata & dependencies
├── uv.lock                            # Deterministic dependency lockfile
└── README.md
```

How To Run This Project
The raw .xlsx datasets are excluded from version control (large binary files) and distributed via GitHub Releases. 

#1. Clone the repository
git clone https://github.com/yourusername/edgar-ghg-analytics.git
cd edgar-ghg-analytics
#2. Download the raw datasets from the Releases page and place all three
#.xlsx files in the data/ directory (see link below)
#3. Install dependencies and sync the environment
uv sync
#4. Run the pipeline
uv run src/main.py

Data download: the raw EDGAR datasets are here. 
[https://github.com/inrt21/edgar-ghg-analytics/releases/download/v1.0.0-data/EDGAR_N2O_m_1970_2024.zip]
Ensure all three files (IEA_EDGAR_CO2_m_1970_2024.xlsx, EDGAR_CH4_m_1970_2024.xlsx, EDGAR_N2O_m_1970_2024.xlsx) are placed in data/.

Data Source
Emissions Database for Global Atmospheric Research (EDGAR), via the joint IEA-EDGAR CO₂ dataset and EDGAR CH₄/N₂O datasets, covering monthly emissions by country, 1970–2024.
