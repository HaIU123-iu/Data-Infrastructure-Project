print("✅ Python läuft und hat die Datei gefunden!")
import pandas as pd
from pathlib import Path

# Pfad zur CSV-Datei
csv_path = Path("/app/data/original_Citibike.csv")

print("CSV-Pfad:", csv_path)

# CSV korrekt einlesen
df_raw = pd.read_csv(
    csv_path,
    header=None,
    engine="python"
)

df = df_raw[0].str.split(",", expand=True)

#1 Header entfernen
df = df.iloc[1:].reset_index(drop=True)

# Quotes aus allen Spalten entfernen
df = df.replace('"', '', regex=True)

# Spaltennamen setzen
df.columns = [
    "tripduration",
    "starttime",
    "stoptime",
    "start_station_id",
    "start_station_name",
    "start_station_latitude",
    "start_station_longitude",
    "end_station_id",
    "end_station_name",
    "end_station_latitude",
    "end_station_longitude",
    "bikeid",
    "usertype",
    "birth_year",
    "gender"
]

print("CSV korrekt eingelesen:")
print(df.head())

#Als Parquet speichern (RAW Zone)
output_path = Path("/app/data/citibike.parquet")
df.to_parquet(output_path)

print("RAW-Parquet gespeichert:", output_path)