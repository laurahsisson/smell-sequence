from flask import Flask
import recommendation

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


from markupsafe import escape

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


@app.route("/recommendation/")
def rec():
    return recommendation.get([],3)

