from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def get_api_key():
    api_key = os.environ.get("API_KEY", "No API Key found")
    return f"API Key: {api_key}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
