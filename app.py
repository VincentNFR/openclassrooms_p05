from flask import Flask, render_template, redirect, url_for, request,jsonify
from werkzeug.wrappers import Request, Response

from ressources.prediction_model import PredictionModel

pred_model = PredictionModel()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/api/predict", methods=["GET"])

def predict():
    msg_data={}
    arr_results = []
    for k in request.args.keys():
        val=request.args.get(k)
        msg_data[k]=val
    arr_results = pred_model.predict(msg_data)
    if len(arr_results)==0:
        msg_result = 'No tag found...'
    else:
        msg_result = ' | '.join(arr_results)
    return msg_result

if __name__ == "__main__":
    app.run()