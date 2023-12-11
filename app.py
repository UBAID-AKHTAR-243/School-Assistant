from flask import Flask,render_template,request,jsonify,url_for
from chatbot import get_response,predict_class
import json
import chatbot


app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    return render_template("index.html")
 


 
@app.route('/', methods=['POST'])
def bot():
    user_input = request.form['user_question']
    intents_list = predict_class(user_input)
    response = get_response(intents_list, intents_json) 
return render_template("index.html",response= response)
if __name__ == '__main__':
  app.run(debug=True)
