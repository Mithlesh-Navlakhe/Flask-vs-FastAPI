#installation steps
#virtualenv envname
#activate environment .\envname\Scripts\activate
#pip freeze requirements.txt
#pip freeze > requirements.txt
#create main.py
#pip install flask flask-restx
#python main.py
# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request, json
from flask_restx import Api, Resource

# creating a Flask app
app = Flask(__name__)
api = Api(app)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/home', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):

		data = "hello world"
		return jsonify({'data': data})

# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):
	return jsonify({'data': num**2})

# driver function
if __name__ == '__main__':
	app.run(debug = True)

