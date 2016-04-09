"""
web_server.py
=====
This file is both a web server and a web application in one. We'll consider
a web server as a long running program that handles client connections,
accepts requests and sends back responses. The web application is some
program that works on the request and constructs a response. The server and
the app work together to field requests and send back responses.

We'll be creating a web site that's role-playing game themed (sooo nerdy).
It'll respond to the following URLs:

localhost:5000/creatures --> list out a bunch of creatures 
localhost:5000/ --> link to creatures and dice
localhost:5000/dice --> generates a random number from 1 through 6
"""
import socket

# WEB APPLICATION 

import random
class Request:
    """Represents an HTTP request. Parses a request and creates properties
    on this request instance. For example... if the request is:

    GET /dice HTTP/1.1
    User-Agent: my suuuuper cool browser
    Accepts: text/html

    # req is an instance of Request:
    req.path --> "/dice"
    req.method --> "/GET"
    req.http_version --> "HTTP/1.1"

    This request object ignores the headers.
    """
    def __init__(self, request_text):
        self.parse_request(request_text)
        
    def parse_request(self, request_text):
        """Extract path, method and http version from string version of HTTP
        request. Save in instance variables.
        """
        # grab the first line (split by carriage return \r and newline \n - 
        # http specs mention that \r\n represents newlines)
        request_parts = request_text.split('\r\n')
        parts = request_parts[0].split(' ')
        self.method, self.path, self.http_version = parts
        print(self.method, self.path, self.http_version)
        
# routes contains mappings of paths to functions
# for example, the path /dice would map to a function called dice:
# {'/dice': dice}
# that function will be called to generate a response
routes = {}

def route(path):
    """decorator (with parameter) for used to map a path to a function
    """
    def decorator(old_f):
        # add path and function to routes dictionary
        routes[path] = old_f

        # just give back the old function unmodified
        return old_f

    return decorator

@route('/')
def home(req):
    html = 'The homepage! '
    html += 'Check out <a href="/creatures">creatures</a> '
    html += 'or <a href="/dice">dice</a>.'
    return  html

@route('/creatures')
def creatures(req):
    return 'Creatures: <ul><li>Griffin</li><li>Zombie</li></ul>'

@route('/dice')
def dice(req):
    return "Dice Roll: {}".format(random.randint(1, 6))

# WEB SERVER
HOST, PORT = '', 5000
QUEUE = 5
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(QUEUE)
print('starting server on port', PORT)
while True:

    client, address = s.accept()

    # we're using a fixed size here, but some strategies for getting "all"
    # of the data sent by the client include:
    # 1. fixed size (obvs)
    # 2. server and client agree on delimiter character so server knows when
    #    all data is received
    # 3. client sends the number of bytes the server should expect and server
    #    continues to recv until size
    data = client.recv(4096)
    if data:
        data_text = data.decode('utf-8')
        request_text = data_text
        req = Request(request_text)

        # get the function that handles the path of the incoming request
        handle_route = routes.get(req.path, None)

        if handle_route:
            # if the path exists, then our response will be the result
            # of using calling that function
            response_body = handle_route(req)

            # notice that the body comes after a blank line (2 \r\n's)
            res = 'HTTP/1.1 200 OK\r\nContent-Type:text/html\r\n\r\n{}'.format(response_body)
        else:
            # if the key doesn't exist, that means we don't have that
            # path! give back a 404
            res = 'HTTP/1.1 404 Page not found\r\n\r\n<strong>404 - page not found</strong>'
    
        client.send(bytes(res, 'utf-8'))
    client.close()
