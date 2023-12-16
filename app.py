from flask import Flask, render_template, request
from chatbot import predict_class, get_response

app = Flask(__name__)


@app.route('/index', methods=['POST'])
def index():
    return render_template("index.html")


@app.route('/bot', methods=['POST'])
def bot(intents_json=None):
    user_input = request.form['user_question']
    intents_list = predict_class(user_input)
    response = get_response(intents_list, intents_json) 
    return render_template("index.html", response=response)


if __name__ == '__main__':

    app.run(debug=True)
