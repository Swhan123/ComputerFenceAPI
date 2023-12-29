from flask import Flask

app = Flask('app')

@app.route('/')
def home():
  return '잘~ 실행중이니 걱정 안하셔도 됩니더'

app.run(host='0.0.0.0', port=8080, debug=True)
