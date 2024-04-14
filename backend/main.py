# flask --app main.py --debug run
import json
from flask import Flask, request
from flask_cors import CORS

import recommendation
import crate_utils

app = Flask(__name__)
CORS(app)

@app.route("/recommendation/")
def rec():
    sequence = json.loads(request.args.get('sequence', '[]'))

    k = int(request.args.get('k', '3'))
    crates = json.loads(request.args.get('crates', '[]'))

    return recommendation.get(k=k, aroma_sequence=sequence, crate_fnames=crates)

@app.route("/crates/<crate_fname>")
def get_crate(crate_fname):
    return crate_utils.get(crate_fname)

@app.route("/crates")
def list_crates():
    return crate_utils.list_all()


if __name__ == '__main__':
    app.run()
