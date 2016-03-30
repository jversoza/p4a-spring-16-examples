# Definitions

A __server__ can refer to a long running program that waits for and handles requests from _clients_. For example, a web server waits for requests from a browser, and it sends back a response when it gets a request for a web page.

A __client__ is a program that makes a request to a _server_.

A __socket__ is an abstraction that represents an endpoint of a connection. It's defined by an IP address / hostname and a port number (within the context of a connection).

A __port__ number is part of a communication end point that allows multiple services to be run on the same host / ip address. Port numbers from 0 to 1023 are reserved for specific services. For example, http, the protocol for communication on the web, is on port 80.
