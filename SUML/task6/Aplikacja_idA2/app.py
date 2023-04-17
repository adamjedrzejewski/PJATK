from __future__ import division
from flask import Flask, request, render_template
from fastai.vision.all import *
from fastai.vision.widgets import *

import pathlib
temp = pathlib.PosixPath
#pathlib.PosixPath - pathlib.WindowsPath # I'm running this app on a Mac

app = Flask(__name__)

model = 'model.pkl'

def model_predict(img_path, model_path):
    learn_inf = load_learner(model_path)
    pred , pred_idx , probs = learn_inf.predict(img_path)
    prob_value = probs[pred_idx] * 100 
    out = f'Na zdjęciu ewidentnie znajduje się {pred}. Wiem to z {prob_value:.02f} % prawdopodobieństwem 👨‍🔬.'
    return out

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':

        f = request.files['file']

        basepath = Path(__file__).parent
        file_path = basepath.joinpath('uploads')
        filename = 'test.jpg'
        file_path = file_path.joinpath(filename)
        f.save(file_path)

        path = Path()
        model_path = (path/model)
        out = model_predict(file_path, model_path)
        return out
    return None

if __name__ == '__main__':
    app.run(debug=True)
