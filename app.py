# -*- coding: utf-8 -*-
from flask import Flask
#from redis import Redis
app = Flask(__name__)
@app.route('/')
def hello():
    return "helloworkd!"
if __name__ == "__main__":
    app.debug=True
    app.run(host=('0.0.0.0'),port=5000)
