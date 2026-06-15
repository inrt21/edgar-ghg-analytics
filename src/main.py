from reader import load_data
from analytics import gas_fluctuation, country_totalsum, evaluate_trend, fit_trend, forecasted_trend
from plotting import fluctuation_graph, countrytotals_graph,current_trend, future_trend

if __name__ == "__main__":
    df = load_data()
    for gas in ["CO2", "N2O", "CH4"]:
        fluctuation_result = gas_fluctuation(df, "United Kingdom", gas)
        fluctuation_graph(fluctuation_result, gas)
    countrytotals_graph(country_totalsum(df))
    uk_co2 = gas_fluctuation(df, "United Kingdom", "CO2")
    model = fit_trend(uk_co2)
    evaluate_trend(uk_co2)
    current_trend(uk_co2, model)
    recent = uk_co2[uk_co2["Year"] >=2000]
    recent_model = fit_trend(recent)
    forecast_df = forecasted_trend(recent_model)
    future_trend(recent, forecast_df)
    

