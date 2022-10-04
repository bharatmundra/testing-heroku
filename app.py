# from crypt import methods
import requests
from flask.views import MethodView
from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)