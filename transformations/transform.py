from pydantic import BaseModel
from typing import List

class StandardizedData(BaseModel):
    id: int
    name: str
    value: float

def transform_data(raw_data: List[dict]):
    transformed = []
    for item in raw_data:
        transformed.append(StandardizedData(
            id=int(item["ID"]),
            name=item["Name"],
            value=float(item["Value"])
        ).dict())
    return transformed
