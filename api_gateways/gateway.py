from fastapi import FastAPI
from adapters.soap_adapters import soap_to_json
from adapters.file_adapter import process_file

from event_bus.kafka_producer import send_to_kafka
from transformations.transform import transform_data


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Headless Agent API Gateway Running"}

@app.get("/fetch-soap-data")
def fetch_soap_data():
    return soap_to_json()

@app.post("/upload-file")
def upload_file(file_path: str):
    return process_file(file_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

from event_bus.kafka_producer import send_to_kafka
from transformation.transform import transform_data

@app.post("/process-data")
def process_data(file_path: str):
    raw_data = process_file(file_path)
    transformed_data = transform_data(raw_data)
    send_to_kafka("processed_data", transformed_data)
    return {"message": "Data processed and sent to Kafka"}

