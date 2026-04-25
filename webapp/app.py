from flask import Flask
import os
import redis
app = Flask(__name__)
cache = redis.Redis(host=os.environ.get("REDIS_HOST", "redis"), port=6379)
@app.route("/")
def index():
    try:
        visits = cache.incr("visits")
    except:
        visits = "niedostępny (brak bazy danych)"
    return f"<h1>GitHub Cloud Lab</h1><p>Liczba odwiedzin: {visits}</p>"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
