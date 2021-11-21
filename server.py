import flask
from flask import send_file, request
from flask_restful import Resource, Api, reqparse

import heartpy as hp
import os
import time
import json
from utils import *
import matplotlib.pyplot as plt
def analyze():
    with open('/tmp/data.csv', 'r') as fin:
        dat = fin.read().splitlines(True)
    with open('/tmp/data.csv', 'w') as fout:
        fout.writelines(dat[3:-2])


    data = hp.get_data('/tmp/data.csv')
    # sample rate is 100  Hz
    wd, m = hp.process(data, sample_rate=100.0)

    # serialize results into json
    export_data = json.dumps(wd, cls=NumpyEncoder)
    export_measures = json.dumps(m, cls=NumpyEncoder)

    # make a graph
    fig = hp.plotter(wd, m, show=False)
    fig.savefig('/tmp/plot.png')
    return export_measures



app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp'
api = Api(app)
parser = reqparse.RequestParser()


@app.route('/img')
def root():
    return send_file("/tmp/plot.png", mimetype='image/jpeg')

@app.route("/upload/", methods=['POST'])
def upload_file():
    from werkzeug.datastructures import FileStorage
    FileStorage(request.stream).save(os.path.join(app.config['UPLOAD_FOLDER'], 'data.csv'))
    return analyze()
    #return 'OK', 200
 

if __name__ == "__main__":
    app.run(debug=True)
    #http_server.serve_forever()
