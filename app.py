from dotenv import load_dotenv


from flask import Flask, jsonify
from services.analysis_worker import run_worker

from config import Config

app = Flask(__name__)

# Initialize environment variables
app.config['SECRET_KEY'] = Config.SECRET_KEY
app.config['DEBUG'] = Config.FLASK_DEBUG.lower() == 'true'

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

run_worker()
if __name__ == '__main__':
    load_dotenv()  
    port = int(Config.PORT)
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG'])
