# edgar-ghg-analytics
Global GHG Emissions Analytics Platform: Time-Series Forecasting, Clustering and Trend Analysis (EDGAR 1970–2024)

This project maps global emissions while leveraging the United Kingdom as a primary time-series case study. By focusing on the UK's 54-year dataset, the project isolates localized structural breaks and macroeconomic anomalies, providing a rigorous testing ground to evaluate linear regression against non-linear forecasting architectures before expanding the time-series models globally. 

Key insights:
- Accelerating Modern Decline: While emissions have steadily decreased since 1970, the rate of decline has accelerated significantly in the modern era (post-2000), driven heavily by structural shifts in policy, energy, and sudden macroeconomic shocks.
- Emission inequality: The distribution of emissions across countries is extremely right-skewed. A tiny fraction of industrial nations act as extreme statistical outliers driving global numbers, while the vast majority of nations contribute a negligible baseline.
- Model evolution: Initial OLS Linear modeling across the full historical dataset (1970-2024) introduced severe bias due to the structural flattening effects of the 1970s and 80s. Isolating the model to the modern era (2000-2024) drastically improved tracking accuracy but highlighted the intrinsic need for non-linear ARIMA structures.

Problem statement

With the rising importance of sustainability, global climate strategies and corporate sustainability frameworks rely heavily on accurate Greenhouse gas (GHG) forecasting to set actionable emission reduction targets. However, modeling global emissions introduces statistical challenges:

- Temporal non-linearity and Structural Breaks: Environmental data does not behave linearly. Historical data spanning from 1970 to the late 1990s contain structural legacy noise such as lack of regulation and events, that artificially flatten predictive regression slopes. Applying standard Ordinary Least Squares (OLS) regression across the entire timeline introduces severe historical bias, creating a visible discontinuity and failing to capture the accelerated velocity of decline seen in the modern era (2000-2024)
- Extreme Spatial Inequality: Aggregating emissions data globally without factoring in country-level variance yields generalized, ineffective policy models that ignore the heavy-tailed distribution of global emitters.

Without isolating these modern trends and transitioning from rigid geometric lines to adaptive time-series models, stakeholders risk making critical strategic decisions based on flawed, outdated projects. 

Global and Business Significance 

The insights derived from accurate GHG tracking hold immense value across two main horizons:

1. Global and Geopolitical impact: Because global emissions follow a strict Pareto Principle (where a tiny fraction of actors cause the vast majority of the impact), global climate initiatives like the Paris Agreement cannot treat all nations with a broad brush. Data-driven modeling allows international bodies to surgically identify, monitor, and hold accountable the specific outlier nations driving global trajectories.
2. Macroeconomic and Business Strategy: for modern multi-national corporations, sustainability is no longer a public relations metric - it is a core financial risk factor. Regulatory compliance and taxation remain as a critical subject as governments implement stricter carbon taxes and cap-and-trade penalties, businesses must accurately project regional emission trends to forecast overhead costs and hedge against compliance penalties. Supply Chain Optimizaiton is another critical subject as companies looking to future-proof their operations use these predictive models in order to shift logistics and manufacturing hubs away from high-emission, high-tax regions into areas demonstrating sustained, structural declines in GHG intensity.

Project Motivation 

As an aspiring Data Scientist with a profound respect for nature and a commitment to environment conservation, edgar GHG Analytics is fundamentally a passion project. It was born out of a desire to bridge the gap between my personal drive to sustain our natural world and the rigorous statistical modeling required to actually understand it. 

Rather than accepting standard data visualizations at face value, this project serves as an intellectual sandbox to explore how real-world historical shocks break traditional linear modeling. It is designed to demonstrate a complete data science lifecycle: identifying the mathematical limitations of a simple linear model, isolating modern data to minimize historical bias, and laying the analytical groundwork for advanced time-series and unsupervised learning applications. 

Most importantly, this repository is not a static portfolio piece; it is a living foundation. I intend to actively scale and refine throughout my studies and future career by integrating new, advanced methodologies as my technical toolkit expands, ultimately evolving a personal passion into a production-grade analytical platform

Exploratory Data Analysis (EDA)

1. Gas-Specific Temporal Fluctuations:
- Carbon Dioxide (CO2): Displays a steep downward trajectory, falling from ~675,000 Gg in 1970 to under 300,000 Gg by 2024. Sharp, localized anomalies correspond directly with major global economic contractions, such as the 2008 Global Financial Crisis and the 2020 Covid-19 Lockdowns.
- Nitrous Oxide (N2O): Exhibits a distinct anomaly - surging heavily throughout the 1970s to a peak of ~161 Gg before entering a sustained long-term decline. This spike signals the massive post-WWII boom in global synthetic nitrogen fertilizer use before precision agriculture began stabilizing it in the late 1980s.
- Methane (CH4): Demonstrates a highly stable, continous downward trend from 1990 onwards, cutting historical baselines by more than half.
2. Cross Country Distribution Analysis
  The global emissions profile displays a severe right-skew, where a select few outlier nations dominate global output, while the median global nation contributes a statistically negligible amount. This textbook Pareto Principle means Global progress is fundamentally dictated by the environmental policies of a few key geopolitical actors.

Predictive Modeling and Regression Architecture

Phase 1: Full-period Linear Regression (1970-2024)
- Approach: Ordinary Least Squares (OLS) regression applied to the entire 54-year dataset.
- Limitation: The high-emission, high-volatilitiy data of the 1970s and 1980s pulled the global slope flatter than the recent trend. This created a visible discontinuity at the forecast boundary (2025), overestimating future emissions because the model could not adjust to the modern accelerated rate of decline.
Phase 2: Modern Era Isolation (2000-2024)
- Approach: To capture contemporary environmental trajectories, the training data was isolated to the modern era (2000-2024).
- Result: By eliminating the historical legacy noise of the late 20th century, the model successfully aligned with the modern velocity of decline, projecting an emissions drop well below the 200,000 Gg threshold by 2034.

Model Limitations and Next Steps

While isolating the 2000-2024 data created a more defensible and responsive regression model, Linear Regression possesses an inherent architectural flaw for this use case: it assumes a constant, unyielding rate of change. Residual analysis reveals that errors are not random; they are systematically widening because a straight line cannot natively capture changing rates of decline (acceleration/deceleration), autocorrelation, or cyclical macroeconomic variations. 

To resolve these limitations and evolve this project into a comprehensive analytical platform, the next iteration will implement the following roadmap:

1. Advanced Time-Series Forecasting (ARIMA/SARIMA): Shifting the predictive pipeline from a rigid geometric trend-line to a stochastic time-series framework (Autoregressive Integrated Moving Average). This will allow the model to process historical momentum, stationarity, and non-linear trajectories while natively addressing autocorrelation.
2. Programmatic Time-Series Decomposition:Implementing seasonal decomposition to mathematically separate the data into three distinct layers: the underlying long-term Trend, the repeating cyclical patterns (Seasonality), and the random white noise (Residuals). This isolates true environmental progress from annual atmospheric fluctuations.
3. Statistical Anomaly Detection (Z-Scores): Integrating an algorithmic anomaly detection layer using rolling Z-Scores. The system will automatically identify and flag structural data points that sit 2 or 3 standard deviations away from the historical mean, allowing for the automated profiling of global macro-events like the 2008 crash or 2020 lockdowns based strictly on statistical thresholds.
4. Unsupervised Learning for Country Clustering (K-Means): Applying a K-Means clustering algorithm to segment the world's nations into distinct "Emission Personas" (e.g., "Rapidly Decarbonizing Modern Economies", "High-Growth Industrial Nations", and "Negligible-Impact Baselines"). This replaces a flawed "one-size-fits-all" global approach with targeted, cluster specific forecasting models.
5. Feature Engineering and Normalization (Per-Capita and GDP): To prevent population sizes or massive economic outputs from distorting the analytical narrative, external World Bank metrics will be integrated to create normalized features:
- Emissions Per Capita: To measure individual carbon footprints across different nations.
- Emissions per USD of GDP (Carbon Intensity): To evaluate how cleanly or efficiently a country generates economic value.
6. Interactive Dashboard: Transitioning the project from a static code repository into a user-facing analytical tool. A web dashboard will be deployed, allowing the ability to dynamically toggle between different greenhouse gases, select specific country clusters, and isolating custom date ranges-significantly elevating the user experience and data accessibility.

Current Tech stack
Language: Python
Libraries: Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn

Repository Structure

├── .cursor/               # Cursor IDE configuration settings
├── data/                  # Raw and processed EDGAR emission datasets
│   ├── EDGAR_CH4_m_1970_2024.xlsx      # Raw methane emissions source data
│   ├── EDGAR_N2O_m_1970_2024.xlsx      # Raw nitrous oxide emissions source data
│   ├── IEA_EDGAR_CO2_m_1970_2024.xlsx  # Raw carbon dioxide emissions source data (IEA/EDGAR joint dataset)
│   └── emissions_data.csv              # Cleaned, consolidated dataset processed by the analytics pipeline
├── src/                   # Python source scripts for the analytics pipeline
│   ├── __init__.py        # Initializer making src a package module
│   ├── analytics.py       # Core logic for OLS regression & modern segmentation
│   ├── main.py            # Main execution entry point for the platform
│   ├── plotting.py        # Chart generation code for gas fluctuations & distributions
│   └── reader.py          # Data ingestion
├── .python-version        # Specifies the pinned Python version for the project
├── pyproject.toml         # Project metadata, configurations, and build dependencies
├── README.md              # Comprehensive project documentation
└── uv.lock                # Lockfile ensuring strict deterministic dependency reproduction

How To Run This Project

1. clone the repository: git clone https://github.com/yourusername/edgar-ghg-analytics.git cd edgar-ghg-analytics
2. Install dependencies and sync the environment through uv: uv sync
3. run the analytics pipeline: Execute the core entry point script by using the isolated project environment: uv run src/main.py

The analytics platform relies on the Emissions Database for Global Atmospheric Research, below is the downloadlink to a zip file containing the Raw EDGAR Datasets  
[https://github.com/inrt21/edgar-ghg-analytics/releases/download/v1.0.0-data/EDGAR_N2O_m_1970_2024.zip]
Please ensure your local data/ directory matches the layout described in the repository
