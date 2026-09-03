from fastapi import FastAPI
import pandas as pd
app = FastAPI()
@app.get("/health")
def health():
    return{"status": "ok", "message": "API läuft"}

from fastapi.responses import JSONResponse
import os
@app.get("/rides_per_day")
def get_rides_per_day():
    try:
        file_path = os.path.join("..", "serving_zone", "riders_per_day.parquet")
        print("Gesuchter Pfad:", os.path.abspath(file_path))
        df = pd.read_parquet(file_path)
        data = df.to_dict(orient="records")
        return {"rows": len(data), "data": data[:10]}
    except Exception as e:
        print("FEHLER", e)
        return {"error": str(e)}

@app.get("/rides_per_hour")
def get_rides_per_hour():
    try:
        file_path = os.path.join("..", "serving_zone", "rides_per_hour.parquet")
        df = pd.read_parquet(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

@app.get("/rides_per_week")
def get_rides_per_week():
    try:
        file_path = os.path.join("..", "serving_zone", "rides_per_week.parquet")
        df = pd.read_parquet(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

@app.get("/rides_per_month")
def get_rides_per_month():
    try:
        file_path = os.path.join("..", "serving_zone", "rides_per_month.parquet")
        df = pd.read_parquet(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

@app.get("/peak_days")
def get_peak_days():
    try:
        file_path = os.path.join("..", "serving_zone", "peak_days.parquet")
        df = pd.read_parquet(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

@app.get("/peak_hours")
def get_peak_hours():
    try:
        file_path = os.path.join("..", "serving_zone", "peak_hours.parquet")
        df = pd.read_parquet(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

@app.get("/top_startstations")
def get_top_startstations():
    try:
        file_path = os.path.join("..", "serving_zone", "top_startstations.parquet")
        df = pd.read_parquet(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

@app.get("/top_endstations")
def get_top_endstations():
    try:
        file_path = os.path.join("..", "serving_zone", "top_endstations.parquet")
        df = pd.read_parquet(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

@app.get("/top_stations")
def get_top_stations():
    try:
        file_path = os.path.join("..", "serving_zone", "top_stations.parquet")
        df = pd.read_parquet(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

@app.get("/top_routes")
def get_top_routes():
    try:
        file_path = os.path.join("..", "serving_zone", "top_routes.parquet")
        df = pd.read_parquet(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

@app.get("/Station_load_per_hour")
def get_top_routes():
    try:
        file_path = os.path.join("..", "serving_zone", "Station_load_per_hour.parquet")
        df = pd.read_parquet(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

@app.get("/gender_stats")
def get_top_routes():
    try:
        file_path = os.path.join("..", "serving_zone", "gender_stats.parquet")
        df = pd.read_parquet(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

@app.get("/birthyear_stats")
def get_top_routes():
    try:
        file_path = os.path.join("..", "serving_zone", "birthyear_stats.parquet")
        df = pd.read_parquet(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

@app.get("/user_type_stats")
def get_top_routes():
    try:
        file_path = os.path.join("..", "serving_zone", "user_type_stats.parquet")
        df = pd.read_parquet(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

@app.get("/daytype_stats")
def get_top_routes():
    try:
        file_path = os.path.join("..", "serving_zone", "daytype_stats.parquet")
        df = pd.read_parquet(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

@app.get("/duration_stats")
def get_top_routes():
    try:
        file_path = os.path.join("..", "serving_zone", "duration_stats.parquet")
        df = pd.read_parquet(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

@app.get("/duplicate_stats")
def get_top_routes():
    try:
        file_path = os.path.join("..", "serving_zone", "duplicate_stats.parquet")
        df = pd.read_parquet(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

@app.get("/invalid_stats")
def get_top_routes():
    try:
        file_path = os.path.join("..", "serving_zone", "invalid_stats.parquet")
        df = pd.read_parquet(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}  

@app.get("/null_values")
def get_top_routes():
    try:
        file_path = os.path.join("..", "serving_zone", "null_values.parquet")
        df = pd.read_parquet(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)} 