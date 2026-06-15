import pandas as pd
from pathlib import Path

FILES = {
    "CO2": "IEA_EDGAR_CO2_m_1970_2024.xlsx",
    "N2O": "EDGAR_N2O_m_1970_2024.xlsx",
    "CH4": "EDGAR_CH4_m_1970_2024.xlsx",

}
#Loads all 3 EDGAR emission files and combines them into one dataframe
def load_data(data_dir: Path | str = Path("data")) -> pd.DataFrame:
    data_dir = Path(data_dir)
    frames = [pd.read_excel(data_dir / fname, sheet_name="TOTALS BY COUNTRY", skiprows=9) for fname in FILES.values()
    ]
    return pd.concat(frames, axis=0, ignore_index=True)


