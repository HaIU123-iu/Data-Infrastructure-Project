import pandas as pd
from pathlib import Path
#1 RAW-Daten laden
raw_path = Path("/app/data/citibike.parquet")
clean_path = Path("/app/data/citibike_clean.parquet")

print("RAW-Daten geladen:", raw_path)

#Einlesen
df = pd.read_parquet(raw_path)

#2 Spaltennamen bereinigen
df.columns = (
    df.columns
    .str.replace('"', '') # Anführungszeichen entfernen
    .str.replace(' ', '_') # Leerzeichen ersetzen
    .str.lower() #alles klein
)

print("Spaltennamen bereinigt:")
print(df.columns)

#3 Datentypen setzen
df['starttime'] = pd.to_datetime(df['starttime'], errors='coerce')
df['stoptime'] = pd.to_datetime(df['stoptime'], errors='coerce')

df['tripduration'] = pd.to_numeric(df['tripduration'], errors='coerce')
df['birth_year'] = pd.to_numeric(df['birth_year'], errors='coerce')
df['gender'] = pd.to_numeric(df['gender'], errors='coerce')

#4 Null-Werte entfernen
df = df.dropna(subset=['tripduration', 'starttime', 'stoptime'])

#5 Duplikate entfernen
df = df.drop_duplicates()

#6 Fehlerhafte Zeilen filtern
df = df[df['tripduration'] > 0] # Dauer muss positiv sein 
df = df[df['starttime'] < df['stoptime']] # Start < Stop

#7 Datumsspalten erzeugen 
df['date'] = df['starttime'] .dt.date
df['year'] = df['starttime'] .dt.year
df['month'] = df['starttime'] .dt.month
df['week'] = df['starttime'] .dt.isocalendar().week
df['hour'] = df['starttime'] .dt.hour

#8 CURATED-Datei speichern
curated_path = Path("citibike_clean.parquet")
df.to_parquet(clean_path)

print("CURATED-Datei gespeichert:", clean_path)

# tripduration numerisch machen
df['tripduration'] = pd.to_numeric(df['tripduration'], errors='coerce')
