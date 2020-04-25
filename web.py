#!/usr/bin/python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "AAA Hello, JZ's Dockerized demo!! Github-->JenkinPipeline-->DockerHub.. 1"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)

