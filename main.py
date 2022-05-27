from flask import Flask 

app = Flask(__name__)
def index('/'):
    return 'Welcome api'

if __name__=='__main__':
    app.run()