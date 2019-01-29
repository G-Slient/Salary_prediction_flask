# Create API of ML model using flask


# Import libraries
import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict():
    
    # Get the data from the POST request.
    #data = request.get_json(force=True)
    #data = request.args['exp']
    data=request.args.get('exp')
    #data=request.get_json(silent=True, cache=False)
    data = int(data)
    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([[np.array(data)]])
    
    # Take the first value of prediction
    output = prediction[0]
    
    return jsonify(output) 
    

@app.route('/',methods=['GET'])
def work():
	return 'Hello, welcome!! This is Salary prediction module.'

if __name__ == '__main__':
    app.run(port=5000, debug=True)
