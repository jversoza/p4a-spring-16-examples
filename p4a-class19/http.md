http
=====

* request / response protocol
* text based
* client sends request
* server sends back response

http request
```
GET /some/path HTTP/1.1
User-Agent: my amazing browser
Host: localhost:5000

optional body
```

```
POST /another/path HTTP/1.1
User-Agent: my amazing browser
Host: localhost:5000

filter=pixelate
```

```
(the action that the 
client wants to perform)
  |
  |
[http request method] [path] [http version]
[header name]:[value]
[blank line]
[body]
```

```
\r\n <--- windows style new line
each line in our request is separated by \r\n

so for example for blank line and body:
\r\n
\r\n
body
```

request methods

* GET - retrieving data
* POST - adding data
* PUT - updating
* DELETE ...

clients for making http requests
-----
__browser__

* to use GET
    * simply enter a url into url bar <-- always a GET
    * use a form that uses GET <-- like a search form (say google search)
    * we could use a browser extension to specify request method, (postman)
* to use POST
    * find a form that uses POST <-- like home.nyu.edu
    * we could use a browser extension to specify request method, (postman)

__curl__

* `-i` - this tells curl to give us both the headers and the body
    * without it just the body
    * with `-I` ... we get just headers
* `curl -i -d ''  localhost:5000` - issues a POST (use -d flag, and then data after it) 
* `curl -i loclahost:5000` - issues a POST

__nc__

* `nc host port`
* type everything yourself


http response
----
```
HTTP/1.1 200 OK
Date: Wed, 06 Apr 2016 14:03:36 GMT
Server: Apache/2.2.15 (Red Hat)
Accept-Ranges: bytes
Content-Length: 163
Content-Type: text/html; charset=UTF-8
Set-Cookie: STATICSERVERID=s4; path=/

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN">
<html>

<head>
<title></title>
<meta HTTP-EQUIV="Refresh" CONTENT="0; URL=home/index.html">
<body>
</body>
</html>
```

__response codes__

* 200 - OK (all 2xx are success)
* 301, 302, etc. - various types of redirects (all 3xx are redirects)
* 404 - PAGE NOT FOUND, 400 - BAD REQUEST (all 4xx ... basically means don't make this exact same request again... client error)
* 500 - SERVER ERROR (all 5xx are server errors... but you can try again)














