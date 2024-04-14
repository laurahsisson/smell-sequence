# flask --app main.py --debug run
import json
from flask import Flask, request
from flask_cors import CORS

import recommendation
import crate

app = Flask(__name__)
CORS(app)

@app.route("/recommendation/")
def rec():
    sequence_str = request.args.get('sequence', '[]')
    sequence = json.loads(sequence_str) if sequence_str else []

    k = int(request.args.get('k', '3'))

    return recommendation.get(k=k, aroma_sequence=sequence)

@app.route("/crates/<crate_fname>")
def get_crate(crate_fname):
    return crate.get(crate_fname)

@app.route("/crates")
def list_crates():
    return crate.list_all()


if __name__ == '__main__':
    app.run()
