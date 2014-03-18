#!flask/bin/python


from flask import Flask, jsonify, abort, make_response, request
from . import compute
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


@app.route('/<string:seed>.html')
def html(seed):
    return open(app.serve_dir + '/%s.html' % seed).read()


@app.route('/<string:seed>.js')
def jq(seed):
    return open(app.serve_dir + '/%s.js' % seed).read()


@app.route('/<string:seed>.css')
def css(seed):
    return open(app.serve_dir + '/%s.css' % seed).read()


@app.route('/<string:seed>.bed')
def bed(seed):
    return open(app.serve_dir + '/%s.bed' % seed).read()


@app.route('/bedserver/api/v1.0/projects', methods=['GET'])
def get_samples():
    return jsonify({'projects': app.get_samples()})


@app.route('/bedserver/api/v1.0/samples/<string:prj_name>/<string:sample_name>', methods=['GET'])
def get_sample(prj_name, sample_name):
    if not request.args:
        abort(400)
    for s in [ 'start', 'stop', 'chrm', 'step', 'size' ]:
        if not s in request.args:
            abort(400)

    start = request.args['start']
    stop = request.args['stop']
    chrm = request.args['chrm'].encode('latin-1')
    step = request.args['step']
    size = request.args['size']

    fn = "%s/%s/%s.bed.gz" % (app.serve_dir, prj_name, sample_name)
    dpoints = compute.data_points(fn, start, stop, chrm, step, size)
    return json.dumps(dpoints)
