from flask import Flask
from services.analysis_worker import run_worker

app = Flask(__name__)


run_worker()
if __name__ == '__main__':
    app.run(debug=True)