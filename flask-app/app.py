from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    app_env = os.getenv("APP_ENV", "development")  # Default to development if not set
    return f"Hello, Flask! Running in {app_env} mode."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

