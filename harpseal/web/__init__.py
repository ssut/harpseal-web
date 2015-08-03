""":mod:`harpseal.web` --- Harpseal for Web
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from flask import Flask, jsonify, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    pass
