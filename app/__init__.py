#!flask/bin/python


from flask import Flask, jsonify, abort, make_response
import json


app = Flask(__name__)


def get_samples():
    return json.loads(app.redis.get("samples"))

app.get_samples = get_samples


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/sapi/api/v1.0/samples', methods=['GET'])
def get_samples():
    return jsonify({'samples': app.get_samples()})


@app.route('/sapi/api/v1.0/samples/<int:sample_id>', methods=['GET'])
def get_sample(sample_id):
    sample = filter(lambda s: s['id'] == sample_id, app.get_samples())
    if len(sample) == 0:
        abort(404)
    return jsonify({'sample': sample[0]})
