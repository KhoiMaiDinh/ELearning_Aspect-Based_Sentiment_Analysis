from flask import Flask, request, jsonify
from services.preprocessing import predict_feedback

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        feedback = data.get('feedback', None)
        if not feedback:
            return jsonify({'error': 'Feedback text is required.'}), 400

        prediction = predict_feedback(feedback)
        return jsonify({'feedback': feedback, 'prediction': prediction}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
