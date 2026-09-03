import pandas as pd
from pathlib import Path

# Pfad zur CURATED-Datei
curated_path = Path("/app/data/citibike_clean.parquet")

df = pd.read_parquet(curated_path)

# Beispiel 1: Fahrten pro Tag
df['date'] = df['starttime'].dt.date
riders_per_day = df.groupby('date').size().reset_index(name='riders')

# Beispiel 2: Top-Startstationen
top_stations = df.groupby('start_station_name').size().reset_index(name='riders')

# Beispiel 3: Durchschnittliche Fahrtdauer
avg_duration_sec = df['tripduration'].mean()
avg_duration_min = avg_duration_sec / 60

print("Durchschnittliche Fahrtdauer (Minuten):", avg_duration_min)

riders_per_day.to_parquet("/app/data/riders_per_day.parquet")
top_stations.to_parquet("/app/data/top_stations.parquet")

print("Serving-Daten gespeichert.")

# Fahrten pro Stunde
df['start_hour'] = df['starttime'].dt.hour
rides_per_hour = df.groupby('start_hour').size().reset_index(name='ride_count')
rides_per_hour.to_parquet("/app/data/rides_per_hour.parquet", index=False)
print("Fahrten pro Stunde gespeichert:")
print(rides_per_hour)

#Fahrten pro Tag
df['start_date'] = df['starttime'].dt.date
rides_per_day = df.groupby('start_date').size().reset_index(name='ride_count')
rides_per_day.to_parquet("/app/data/rides_per_day.parquet", index=False)
print("Fahrten pro Tag gespeichert:")
print(riders_per_day)

#Fahrten pro Woche
df['start_week'] = df['starttime'].dt.isocalendar().week
rides_per_week = df.groupby('start_week').size().reset_index(name='ride_count')
rides_per_week.to_parquet("/app/data/rides_per_week.parquet", index=False)
print("Fahrten pro Woche gespeichert:")
print(rides_per_week)

#Fahrten pro Monat
df['start_month'] = df['starttime'].dt.month
rides_per_month = df.groupby('start_month').size().reset_index(name='ride_count')
rides_per_month.to_parquet("/app/data/rides_per_month.parquet", index=False)
print("Fahrten pro Monat gespeichert:")
print(rides_per_month)

#Rush Hours
peak_hours = rides_per_hour.sort_values(by='ride_count', ascending=False).head(5)
peak_hours.to_parquet("/app/data/peak_hours.parquet", index=False)
print("Peak Hours gespeichert:")
print(peak_hours)

#Peak Days
peak_days = rides_per_day.sort_values(by='ride_count', ascending=False).head(5)
peak_days.to_parquet("/app/data/peak_days.parquet", index=False)
print("Peak Days gespeichert:")
print(peak_days)

#Top-Startstationen
top_startstations = (
    df.groupby('start_station_name')
    .size()
    .reset_index(name='ride_count')
    .sort_values(by='ride_count', ascending=False)
    .head(10)
)
top_startstations.to_parquet("/app/data/top_startstations.parquet", index=False)
print("Top-Startstationen gespeichert:")
print(top_startstations)

#Top-Endstationen
top_endstations = (
    df.groupby('end_station_name')
    .size()
    .reset_index(name='ride_count')
    .sort_values(by='ride_count', ascending=False)
    .head (10)
)
top_endstations.to_parquet("/app/data/top_endstations.parquet", index=False)
print("Top-Endstationen gespeichert:")
print(top_endstations)

#Beliebteste Routen
routes = (
    df.groupby(['start_station_name', 'end_station_name'])
    .size()
    .reset_index(name='ride_count')
    .sort_values(by='ride_count', ascending=False)
    .head(10)
)
routes.to_parquet("/app/data/top_routes.parquet", index=False)
print("Beliebteste Routen gespeichert:")
print(routes)

#Stations-Auslastung pro Stunde
station_load_per_hour = (
    df.groupby(['start_station_name', 'start_hour'])
    .size()
    .reset_index(name='ride_count')
    .sort_values(by='ride_count', ascending=False)
)
station_load_per_hour.to_parquet("/app/data/Station_load_per_hour.parquet", index=False)
print("Stations-Auslastung pro Stunde gespeichert:")
print(station_load_per_hour.head(20)) #nur die Top 20 anzeigen

#Fahrten nach Gender
gender_stats = (
    df.groupby('gender')
    .size()
    .reset_index(name='ride_count')
    .sort_values(by='ride_count', ascending=False)
)
gender_stats.to_parquet("/app/data/gender_stats.parquet", index=False)
print("Fahrten nach Gender gespeichert:")
print(gender_stats)

#Fahrten nach User-Typ
user_type_stats = (
    df.groupby('usertype')
    .size()
    .reset_index(name='ride_count')
    .sort_values(by='ride_count', ascending=False)
)
user_type_stats.to_parquet("/app/data/user_type_stats.parquet", index=False)
print("Fahrten nach User-Type gespeichert")
print(user_type_stats)

#Fahrten nach Geburtsjahr
birthyear_stats = (
    df.groupby('birth_year')
    .size()
    .reset_index(name='ride_count')
    .sort_values(by='ride_count', ascending=False)
)
birthyear_stats.to_parquet("/app/data/birthyear_stats.parquet", index=False)
print("Fahrten nach Geburtsjahr gespeichert:")
print(birthyear_stats)

#Anzahl Null-Werte
null_values = (
    df.isnull().sum()
    .reset_index(name='null_count')
    .rename(columns={'index':'column'})
    .sort_values(by='null_count', ascending=False)
)
null_values.to_parquet("/app/data/null_values.parquet", index=False)
print("Null-Werte gespeichert")
print(null_values)

#Anzahl Duplikate
duplicate_count = df.duplicated().sum()
duplicate_stats = pd.DataFrame({
    'metric': ['duplicate_rows'],
    'count': [duplicate_count]
})
duplicate_stats.to_parquet("/app/data/duplicate_stats.parquet", index=False)
print("Duplikate gespeichert")
print(duplicate_stats)

#Fehlerhafte Datensätze
invalid_rows = df[df['tripduration']<= 0].shape[0]
invalid_stats = pd.DataFrame({
    'metric': ['invalid_tripduration'],
    'count': [invalid_rows]
})
invalid_stats.to_parquet("/app/data/invalid_stats.parquet", index=False)
print("Fehlerhafte Datensätze gespeichert")
print(invalid_stats)

#Weekday vs Weekend
df['weekday'] = df['starttime'].dt.weekday #0=Mo...6=So
df['day_type'] = df['weekday'].apply(lambda x: 'weekend' if x >= 5 else 'weekday')
daytype_stats = (
    df.groupby('day_type')
    .size()
    .reset_index(name='ride_count')
    .sort_values(by='ride_count', ascending=False)
)
daytype_stats.to_parquet("/app/data/daytype_stats.parquet", index=False)
print("Weekday vs Weekend gespeichert:")
print(daytype_stats)

#Dauer in Minuten
df['duration_min'] = df['tripduration'] / 60
duration_stats = pd.DataFrame({
    'metric': ['avg_duration_min', 'min_duration_min', 'max_duration_min'],
    'value': [
        df['duration_min'].mean(),
        df['duration_min'].min(),
        df['duration_min'].max()
    ]
})
duration_stats.to_parquet("/app/data/duration_stats.parquet", index=False)
print("Dauer in Minuten gespeichert:")
print(duration_stats)
