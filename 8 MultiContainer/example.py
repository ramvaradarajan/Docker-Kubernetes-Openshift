from flask import Flask
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def hello():
    redis_client.incr('hits')
    total_hits = redis_client.get('hits')
    return f'Hello, this page has been visited {total_hits} times!\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
