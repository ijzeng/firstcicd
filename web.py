#!/usr/bin/python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, JZ's Dockerized demo!! Github-->JenkinPipeline-->DockerHub"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)

