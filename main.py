from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome api'

@app.route('/predict',methods=['GET','POST'])
def predict():
    return 'prediction'


if __name__=='__main__':
    app.run()