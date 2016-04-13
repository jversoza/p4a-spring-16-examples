from flask import Flask, render_template, request
# create the actual app object
app = Flask(__name__)
# show stack traces on front-end (on client side)
app.debug = True

todo_items = ['make the slides', 'create 2nd milestone']

"""
if you want static files... simply create a static directory
access via /static/path/to/file
"""
"""
if you want templates, drop in templates directory
templates can have any extension
 
we used {% block block_name %} and extends for template inheritance
jinja2 is name of templating system
"""
"""
GET /the/form
POST/GET data to /path/action
maybe redirect
"""
@app.route('/todo')
def todo():
    # our response is the rendered template of todo.html
    return render_template('todo.html', things_todo=todo_items)

@app.route('/todo/add', methods=['GET', 'POST'])
def todo_add():
    if request.method == 'GET':
        return render_template('todo-add.html')
    else:
        # print(request.form['todo_item'], request.form['priority'])
        todo_items.append(request.form['todo_item'])
        return "got it!!!!"


@app.route('/debug')
def debug():
    # request if imported, represents
    # current http request
    return (request.method, request.url)
# this is saying... call this function when
# an http request to / is issued
@app.route('/')
def hello():
    # this will return implicitly a 200, with Content-Type
    # text/html
    return render_template("hello.html", greeting="hello world!!!!!!!")


# run on port 50000
app.run()
