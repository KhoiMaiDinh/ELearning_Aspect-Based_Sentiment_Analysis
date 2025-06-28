from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    FLASK_DEBUG =  os.getenv('FLASK_DEBUG', 'False')
    PORT = os.getenv('PORT', 5000)
    KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "myuser")
    KAFKA_GROUP_ID = os.getenv('KAFKA_GROUP_ID', 'ai-analysis-service')
    