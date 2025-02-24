import streamlit as st
from kafka import KafkaConsumer
import json

st.title("📊 Real-Time Data Stream")

consumer = KafkaConsumer(
    "processed_data",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

st.write("Listening for incoming data...")

for message in consumer:
    st.json(message.value)
