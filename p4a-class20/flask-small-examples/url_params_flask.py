from flask import Flask, url_for
app = Flask(__name__)
app.debug = True

# trailing slash forces redirect if no slash
@app.route('/foo/')
def foo():
    return 'foo'

@app.route('/bar')
def bar():
    return 'bar'

@app.route('/baz/<qux>')
def baz(qux):
    return qux

@app.route('/xyz')
def abc():
    return 'abc'

@app.route('/test')
def test():
    return url_for('abc')


app.run()
