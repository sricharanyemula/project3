from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return 'Your in home page'

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/addition-form', methods=['GET'])
def addition():
    return render_template('index2.html')
@app.route('/addition-form', methods=['POST'])
def addition_form():
    num1 = request.form['a']
    num2 = request.form['b']
    return {'reponse': int(num1) + int(num2)}

@app.route('/subtraction-form', methods=['GET'])
def subtraction():
    return render_template('index3.html')
@app.route('/subtraction-form', methods=['POST'])
def subtraction_form():
    num1 = request.form['a']
    num2 = request.form['b']
    return {'response': int(num1) - int(num2)}

@app.route('/multiplication-form', methods=['GET'])
def multiplication():
    return render_template('index4.html')
@app.route('/multiplication-form', methods=['POST'])
def multiplication_form():
    num1 = request.form['a']
    num2 = request.form['b']
    return {'response': int(num1) * int(num2)}

@app.route('/division-form', methods=['GET'])
def division():
    return render_template('index5.html')
@app.route('/division-form', methods=['POST'])
def division_form():
    num1 = request.form['a']
    num2 = request.form['b']
    return {'response': int(num1) / int(num2)}

app.run()