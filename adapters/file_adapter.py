import pandas as pd

def process_file(file_path: str):
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}
