from flask import Flask,render_template,request,jsonify,url_for
from chatbot import get_response,predict_class
import json


app = Flask(__name__)


 
@app.route('/', methods=['POST'])
def index():
    user_input = request.form['user_input']
    intents_list = predict_class(user_input)
    response = get_response(intents_list, intents_json)  # Pass intents_json here
    return jsonify({'response': response})
if __name__ == '__main__':
  app.run(debug=True)