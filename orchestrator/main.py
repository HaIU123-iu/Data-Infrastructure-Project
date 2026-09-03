import os
import subprocess

def run_ingestion():
    print("Starte Ingestion Service...")
    subprocess.run(["python", "/app/ingestion_service/ingestion.py"], check=True)

def run_processing():
    print("Starte Processing Service...")
    subprocess.run(["python", "/app/processing_service/processing.py"], check=True)

def run_transformation():
    print("Starte Transformation Service...")
    subprocess.run(["python", "/app/transformation_service/transform.py"], check=True)

def run_api():
    print("Starte API Service...")
    subprocess.run(["python", "/app/api_service/main.py"], check=True)

if __name__ == "__main__":
    print("Orchestrator gestartet")
    run_ingestion()
    run_processing()
    run_transformation()
    run_api()
    print("Pipeline erfolgreich abgeschlossen")
