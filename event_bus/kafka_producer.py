from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def send_to_kafka(topic: str, data):
    producer.send(topic, value=data)
    return {"status": "Data sent to Kafka"}
