from flask import Flask, render_template, request
from chatbot import predict_class, get_response


app = Flask(__name__)


@app.route('/index', methods=['POST', "GET"])
def index():
    return render_template("index.html")


@app.route('/submit', methods=['POST', "GET"])
def submit():
    user_input = request.form.get('user_question')
    intents_list = predict_class(user_input)
    response = get_response(intents_list, "intents")
    return render_template("index.html", user_input=user_input, response=response)


if __name__ == '__main__':
    
    app.run(debug=True)
