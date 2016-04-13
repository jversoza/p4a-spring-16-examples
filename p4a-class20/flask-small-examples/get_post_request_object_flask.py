from flask import Flask, request
app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def index():
    return 'index page!'

@app.route('/both', methods=['GET', 'POST'])
def both():
    return 'both'

@app.route('/post-only', methods=['POST'])
def post_only():
    return 'post'

@app.route('/request-info', methods=['POST', 'GET'])
def request_info():
    """
    form
    args
    values
    headers
    method
    path
    url
    """
    return str(request.form)

app.run()
