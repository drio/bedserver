#!flask/bin/python


from flask import Flask, jsonify, abort, make_response, request
import json
import os


app = Flask(__name__)


def get_samples():
    data = {}
    for root, dirs, files in os.walk(app.serve_dir):
        for file in files:
                if file.endswith(".bed.gz.tbi"):
                    print os.path.join(root, file)
                    k = root.split("/")[-1]
                    v = file.replace(".bed.gz.tbi", "")
                    if k in data:
                        data[k].append(v)
                    else:
                        data[k] = [v]
    return data

app.get_samples = get_samples


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/bedserver/api/v1.0/projects', methods=['GET'])
def get_samples():
    return jsonify({'samples': app.get_samples()})


@app.route('/bedserver/api/v1.0/samples/<string:prj_name>/<string:sample_name>', methods=['GET'])
def get_sample(prj_name, sample_name):
    if not request.json or not 'start' in request.json:
        abort(400)
    if not 'stop' in request.json:
        abort(400)
    if not 'chrm' in request.json:
        abort(400)
    if not 'step' in request.json:
        abort(400)

    start = request.json['start']
    stop = request.json['stop']
    chrm = request.json['chrm']
    step = request.json['step']

    return jsonify({'sample': prj_name, 'start': start, 'stop': stop, 'chrm': chrm, 'step': step})
