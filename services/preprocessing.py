import tensorflow as tf
import numpy as np
from transformers import AutoTokenizer, TFRobertaModel
from keras.utils import custom_object_scope

from constants.lable import ASPECTS, REPLACEMENTS
from constants.path import TOKENIZER_PATH, MODEL_PATH

tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)

with custom_object_scope({'TFRobertaModel': TFRobertaModel}):
    model = tf.keras.models.load_model(MODEL_PATH)


def preprocess_input(feedback):
    return feedback.lower()  # Replace with actual preprocessing


def predict_feedback(feedback):
    processed_feedback = preprocess_input(feedback)
    tokenized = tokenizer(
        processed_feedback,
        max_length=tokenizer.model_max_length,
        padding='max_length',
        truncation=True,
        return_tensors='tf'
    )
    inputs = {k: tf.convert_to_tensor(v.numpy()) for k, v in tokenized.items()}
    predictions = model.predict(inputs, verbose=0)
    predictions = predictions.reshape(len(predictions), -1, 4)
    sentiment_ids = np.argmax(predictions, axis=-1)

    result = {}
    for aspect, sentiment_id in zip(ASPECTS, sentiment_ids[0]):
        result[aspect] = REPLACEMENTS[sentiment_id]
    return result
