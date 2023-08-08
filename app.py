from flask import Flask
from chatbot import get_response
app = Flask(__name__)

   
@app.route('/', methods=['get']) 
def index():
    return "welcome"
 
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = get_response(user_input)
    return jsonify({'response': response})

    if __name__ == '__main__':
      app.run(debug=True) 