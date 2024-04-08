import json
from flask import Flask, request
from flask_cors import CORS
import recommendation

app = Flask(__name__)
CORS(app)

@app.route("/recommendation/")
def rec():
    sequence_str = request.args.get('sequence', '[]')
    sequence = json.loads(sequence_str) if sequence_str else []

    k = int(request.args.get('k', '3'))

    return recommendation.get(sequence, k)

if __name__ == '__main__':
    app.run()
