
"""
todo: return object directly
list of final project proposals
* netid
* title
* description
"""
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
app.debug = True

proposals = [{"netid":"jjv222", "title":"How to spell", "description":"How do you spell mammal?"}, {"netid":"abc123", "title":"decorators", "description":"sooo functional!"}]

"""
how do we display this list of projects?
"""
@app.route('/projects')
def projects():
    return render_template('projects.html', projects=proposals)

@app.route('/projects/add', methods=['POST','GET'])
def projects_add():
    if request.method == 'POST':
        proposals.append({'netid':request.form['netid']})
        return redirect('/projects')
    elif request.method == 'GET':
        return render_template('projects_add.html', projects=proposals)

app.run()







