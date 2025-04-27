import json
from services.kafka.consumer_service import consumer
from services.kafka.producer_service import producer
from services.preprocessing import predict_feedback
from constants.kafka_topic import COMMENT_CREATED, COMMENT_PROCESSED

def run_worker():
    consumer.subscribe([COMMENT_CREATED])

    print("AI Worker is now listening for new comments...")

    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue

        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue
        print(f"Received new comment: {msg.value()}")
        data = json.loads(msg.value())
        print(f"Received new comment: {data}")
        feedback = data.get('content')
        comment_id = data.get('lecture_comment_id')

        if not feedback or not comment_id:
            print("Invalid data format received.")
            continue

        try:
            prediction = predict_feedback(feedback)
            response = {
                "comment_id": comment_id,
                "aspects": prediction
            }
            
            producer.produce(COMMENT_PROCESSED, value=json.dumps(response))
            producer.flush()
            print(f"Analyzed result for comment {comment_id}: {response}")
        except Exception as e:
            print(f"Processing error: {e}")

    consumer.close()
