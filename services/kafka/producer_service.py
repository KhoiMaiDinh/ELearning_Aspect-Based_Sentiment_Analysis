from confluent_kafka import Producer
from .kafka_config import KAFKA_BOOTSTRAP_SERVERS

producer = Producer({'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS})

def send_analyzed_result(comment_id: str, aspects: list):
    payload = {
        "comment_id": comment_id,
        "aspects": aspects,
    }
    producer.produce('lecture.comment.analyzed', value=json.dumps(payload))
    producer.flush()