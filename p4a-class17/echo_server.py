"""
create a server... that just echoes back whatever we send it
"""
import socket
# .... ip v 4 ... 255.255.255.255 .... 2 way (bi-directional) communication
# .... messages you send will be guaranteed to be delivered... in the sequence they were sent

HOST, PORT = '', 5000
QUEUE = 5
""" creating a new socket"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

""" allows restarts without waiting for time out"""
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

""" this is the hostname and port that i'm serving on"""
s.bind((HOST, PORT))

""" wait for connections... how many connection queue up"""
s.listen(QUEUE)
print('starting server on port', PORT)
while True:

    """ accept an incoming connection"""
    client, address = s.accept()
    data = client.recv(4096)
    if data:
        data_text = data.decode('utf-8')
        res = data_text
        #something = b"looks like a string but it's not"
        """ bytes represents an immutable sequence of bytes"""
        client.send(bytes(res, 'utf-8'))
    client.close()




