from confluent_kafka import Consumer
from .kafka_config import KAFKA_BOOTSTRAP_SERVERS, KAFKA_GROUP_ID

consumer = Consumer({
    'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
    'group.id': KAFKA_GROUP_ID,
    'auto.offset.reset': 'earliest'
})