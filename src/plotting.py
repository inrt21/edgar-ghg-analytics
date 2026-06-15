from analytics import gas_fluctuation, country_totalsum, evaluate_trend, fit_trend, forecasted_trend
from reader import load_data
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def fluctuation_graph(fluctuation_result: pd.DataFrame, gas: str) -> None:
    sns.lineplot(x=fluctuation_result["Year"], y=fluctuation_result["Total"])
    plt.xlabel("Year")
    plt.ylabel(f"Total {gas} Emissions (Gg)")
    plt.title(f"Fluctuation of {gas} Throughout the Years")
    plt.show()

def countrytotals_graph (country_totals: pd.DataFrame) -> None:
    sns.histplot(country_totals, bins=50)
    plt.xlabel("Total CO2 Emissions (Gg)")
    plt.ylabel("Number of Countries")
    plt.title("Distribution of CO2 Emissions Across Countries")
    plt.show()

def current_trend(fluctuation_result: pd.DataFrame, model: LinearRegression) -> None:
    X = fluctuation_result[["Year"]]
    plt.scatter(fluctuation_result["Year"], fluctuation_result["Total"], label="Actual")
    plt.plot(fluctuation_result["Year"], model.predict(X), color="green", label="Trend line")
    plt.xlabel("Year")
    plt.ylabel("Total CO2 Emissions (Gg)")
    plt.title("CO2 Emissions Trend")
    plt.legend()
    plt.show()

def future_trend(fluctuation_result: pd.DataFrame, forecast_df: pd.DataFrame) -> None:
    plt.plot(fluctuation_result["Year"], fluctuation_result["Total"], label="Actual(2000-2024)")
    plt.plot(forecast_df["Year"], forecast_df["Predicted_Total"], linestyle="--", color="green", label="Forecast(2025-2034)")
    plt.xlabel("Year")
    plt.ylabel("Total CO2 Emissions Forecast (Gg)")
    plt.title("CO2 Emissions Forecast")
    plt.legend()
    plt.show()
