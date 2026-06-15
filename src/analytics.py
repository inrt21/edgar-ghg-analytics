import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from reader import load_data

df = load_data()
month_cols = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print("Countries: ", df["Name"].nunique())
print(df["Substance"].value_counts())

def gas_fluctuation(df: pd.DataFrame, name: str, gas: str) -> pd.DataFrame:
    subset = df[(df["Substance"] == gas) & (df["Name"] == name)].copy()
    subset["Total"] = subset[month_cols].sum(axis=1)
    subset["Change"] = subset["Total"].diff()
    return subset[["Name","Year","Total","Change"]]

def country_totalsum(df: pd.DataFrame) -> pd.DataFrame:
    co2 = df[(df["Substance"] == "CO2")].copy()
    co2["Annual"] = co2[month_cols].sum(axis=1)
    country_totals = co2.groupby("Name")["Annual"].sum()
    return country_totals

def fit_trend(fluctuation_result: pd.DataFrame) -> LinearRegression:
    X = fluctuation_result[["Year"]]
    y = fluctuation_result["Total"]
    model = LinearRegression()
    model.fit(X, y)
    print(f"Slope: {model.coef_[0]: .2f}")
    print(f"R²: {model.score(X, y): .3f}")
    return model

def evaluate_trend(fluctuation_result: pd.DataFrame, split_year: int = 2015) -> float:
    train = fluctuation_result[fluctuation_result["Year"] <= split_year]
    test = fluctuation_result[fluctuation_result["Year"] > split_year]
    model = LinearRegression()
    model.fit(train[["Year"]], train["Total"])
    predictions = model.predict(test[["Year"]])
    mae = mean_absolute_error(test["Total"], predictions)
    print(f"MAE on {len(test)} held-out years: {mae: .2f} Gg")
    return mae
    
def forecasted_trend(model: LinearRegression, start: int=2025, end: int = 2034) -> pd.DataFrame:
    future = pd.DataFrame({"Year": range(start, end +1)})
    future["Predicted_Total"] = model.predict(future)
    return future
    
