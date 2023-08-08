import flask

app = Flask(__name__)



@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = get_response(user_input)
    return jsonify({'response': response})

   
@app.route('/', methods=['get']) 
def index():
    return render_template(index.html)
 
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = get_response(user_input)
    return jsonify({'response': response})

    if __name__ == '__main__':
    app.run(debug=True) 