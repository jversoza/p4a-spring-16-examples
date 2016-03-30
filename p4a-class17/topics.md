# Topics

## sockets review

* review sockets
    * echo server
    * `s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)`
    * echo client
        * write a client
        * use netcat as client
        * use browser as client
    * (push both to github)
* definitions from previous class
* review bytes vs str
    * echo server again, shout version 
    * all uppercase
    * and 3 exclamation points
* look at math server again
* try to use browser 

## HTTP

* protocol for communication on the web
* request response
* text based
* method path / resource you'd like to retrieve
* request
    * request line
    * headers 
    * body
* response
    * status line
    * headers
    * body
* show request/response with diff clients
   * netcat
   * curl
   * browser
* carriage return, line feed 

## ACTIVITY!!!111!1

* examine a request
    1. copy the echo_server.py file from above
    2. run it in PyCharm or terminal
    3. use a client to connect to your server; you can choose one of the following:
        * use your browser to make a request to localhost:5000
        * use `curl -i curl -i localhost:5000`
        * (optional) want to see what a POST looks like???
            * check out the man page `man curl`
            * search for POST by typing forward slash then POST /POST
    4. notice the string that's returned... that's the _actual_ http request that your client is sending!
* based on the request... figure out how to parse out the method and path, and drop the information into a class:
    * modify echo_server so that the data it receives is turned into a string
    * assign it to a variable called `request_text`...
    * create a class called `Request` that represents an http request
    * __note that newlines in http requests are reprented by \r\n__!!!
    * it should have a constructor that takes a string of an http request...
    * it should have a field, `method` that contains the http method (like `GET`, `POST`, etc.
    * it should have a field, `path`, that contains the path of the resource being requested (`/`, `/pizzas`, `/robots/neptr.html`, etc.)
    * it should have a field, `http_version`, that contains the http version of the request
    * (optional / if you have time) - a field called `headers` that is a dictionary of all of the header name/header value pairs (`Content-Type: text/html`)
    * it should have a method that parses the incoming string to fill in the above fields
    * create a new `Request` object using your `request_text` variable

## Back to HTTP

* implement request object
* show google chrome network tab
    * hey, why is it making all of those other requests?
    * that's kind of frightening!
    * difference between POST and GET
    * show a form
    * login to nyu home!?
* oh yeah, headers
    * [req headers](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields#Field_names)
    * ... what do I accept? what character encoding do I want? what client am I?
    * [response headers](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields#Response_fields)
    
## Web Servers and Web Frameworks

* usually different applications
    * web server... just handles:
        * connections
        * receiving a request
        * sending back a request
        * maybe serving static files
    * web app
        * takes a request and does some _thing_ based on request
        * creates a response
    * examples, Django or Flask, and uwsgi, gunicorn
    * examples... PHP and apache or nginx
* though... sometimes the same
    * see node
    * ...and what we're building

## Demo

* create role-playing site
    * /dice ... random number 1 - 6
    * /creatures ... a list of creatures in the game
    * / ... links to dice and creatures
    * add some html / content-type
* start inline with conditional
* create functions
* dictionary of functions
* decorator for routes and handle_request function with 404!

## Flask

* installation
* setup
    * `from flask import Flask`
    * `app = Flask(__name__)`
    * `app.run()`
    * to debug... `app.debug = True`
* for routing... `@app.route('/')`
* for method... `@app.route('/login', methods=['GET', 'POST'])`
* templating:
    * `from flask import render_template`
    * `return render_template('hello.html', name=name)`
    * templates go in `/templates`
    * [pythonic syntax](http://jinja.pocoo.org/docs/dev/templates/)
    * `{{var 1}}`
    * `{% for creature in creatures %}`
    * `{% endfor %}`
* accessing request data
    * `from flask import request` 
    * `request.method` 
    * `request.path` 
    * `request.form['field_name']`
