"""
math server - responds to client requests to add or multiply two numbers

request format:
OPERATION <OPERAND_1> <OPERAND_2>

response format:
ANSWER <RESULT>
ERROR <ERROR REASON>

Examples

request:
MULTIPLY 5 2

response:
ANSWER 10

request:
MAKE_SOME_PIZZA pepporni mushroom

response:
ERROR operation not supported

request:
aaaa b c d

response:
ERROR server error or bad request

To try out server... 

1. start server on the commandline or in PyCharm
2. use netcat to connect:
    nc localhost 5000
    MULTIPLY 5 2
"""

import socket

HOST, PORT = '', 5000
print('Starting math server on port', PORT) 

# creates a new socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a host and port
s.bind((HOST, PORT))

# allow server to accept connections... allow 5 connection to queue up
s.listen(5)

# these are the operations we'll support
operator_map = {
    'MULTIPLY': lambda a, b: a * b,
    'ADD': lambda a, b: a + b 
}

while True:
    # accept incoming connection; gives back a new socket representing
    # the client and the address of the client. new socket can be used
    # to send and receive data
    client, address = s.accept()
    print('Got connection from:', address) 
    # get data from client socket
    data = client.recv(4096)

    if data:
        print('Data from incoming request:', data) 
        try:
            # data is in bytes object... so decode to get a string
            req = data.decode('utf-8')

            # get the operation from the request
            parts = req.split(' ')
            operator, operand_1, operand_2 = parts[:3]
            print('operator, operand_1, operand_2:', operator, operand_1, operand_2)

            # use operation to key into dictionary of operations above
            result = operator_map[operator](int(operand_1), int(operand_2))
            print('result:', result)
            res = bytes('ANSWER ' + str(result), 'utf-8')

        except KeyError as e:
            res = b'ERROR operation not supported'

        except Exception as e:
            # there was an error... just send back the exception as a string
            print('Server error / bad request: {} - {}'.format(e.__class__, e))
            res = b'ERROR server error or bad request'

        print('Sending response\n', res)
        client.send(res)

    client.close()
