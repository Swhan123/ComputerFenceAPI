from flask import Flask, request, render_template
import DBManager

app = Flask('app')

@app.route('/')
def home():
  return render_template('tester.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'GET':
    return render_template('register.html')
  else:
    id = request.form['id']
    ps = request.form['password']
    DBManager.register(id, ps)
    return 'SUCCESS'

@app.route('/login', methods=['POST'])
def login():
  id = request.form['id']
  ps = request.form['password']
  check = DBManager.login(id, ps)
  if check = "ACCEPT":
    return 

app.run(host='0.0.0.0', port=8080, debug=True)
