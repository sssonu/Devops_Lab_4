from flask import Flask
import time, math

app = Flask(__name__)

@app.route("/")
def home():
    # Simulate CPU work for ~0.5s
    start = time.time()
    while time.time() - start < 0.5:
        math.sqrt(12345.6789)
    return "Hello from Social Media API! 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)