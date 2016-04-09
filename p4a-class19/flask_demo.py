"""
flask is a web framework

* a framework is a library that makes doing some web dev related things easier
* flask is not the server (though it has a built in server for development)

installing flask

* via PyCharm ... search for flask
* or `pip install flask`
* or add to requirements.txt / `pip freeze`

heart of flask is an application object (represents your web app)
"""
# Flask <-- constructor to create application object
from flask import Flask, render_template
app = Flask(__name__)
app.debug = True # <-- debug mode so that stack trace shows up in response

@app.route('/')
def hello():
    return 'hello from 380'

@app.route('/test-post', methods=['POST'])
def test_post():
    return 'yup, that was a POST'

@app.route('/template-test', methods=['POST', 'GET'])
def template_test():
    return render_template('test.html', foo='bar', baz=['qux', 'quxx'])

app.run()




















