from bottle import Bottle
from consumer import consume_suggest, consume_train

app = Bottle()

@app.route('/hello')
def hello():
    return "Hello World!"


@app.route('/train/<strategy>')
def train(strategy):
    return consume_train(strategy)


@app.route('/suggest/<strategy>')
def suggest(strategy):
    return consume_suggest(strategy)


app.run(host='localhost', port=8080, debug=True)
