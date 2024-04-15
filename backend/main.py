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

    crates = json.loads(request.args.get('crates', '[]'))
    options = json.loads(request.args.get('options', '{}'))

    return recommendation.get(aroma_sequence=sequence, crate_fnames=crates, options=options)

@app.route("/crates/<crate_fname>")
def get_crate(crate_fname):
    return crate_utils.get(crate_fname)

@app.route("/crates")
def list_crates():
    return crate_utils.list_all()


if __name__ == '__main__':
    app.run()
