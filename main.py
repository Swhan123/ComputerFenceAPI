from flask import Flask, request, render_template
import DBManager

app = Flask('app')

@app.route('/')
def home():
  return render_template('tester.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
  '''id = request.headers['id']
  ps = request.headers['password']'''
  #for API Tester
  id = request.form['id']
  ps = request.form['password']
  DBManager.register(id, ps)
  return '잘~ 실행중이니 걱정 안하셔도 됩니더'

app.run(host='0.0.0.0', port=8080, debug=True)
