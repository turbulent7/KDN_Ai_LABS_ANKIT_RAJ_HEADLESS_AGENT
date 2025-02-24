from fastapi import FastAPI
from adapters.soap_adapter import soap_to_json
from adapters.file_adapter import process_file

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
