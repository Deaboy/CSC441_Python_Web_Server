# CSC441_Python_Web_Server

A very basic web server written in Python and using the build-in **socket**
submodule. Accepts simple HTTP GET requests and returns a 200 response if the
file was successfully found, a 404 response if the requested file was not found,
and a 500 response if an internal server error occured.

- Serves rudimentary GET requests
- Does not support PHP
- Does not support HTTP POST requests
- Is not multithreaded (all operations are done serially)

## And Before you Ask...

> Dan, why would you write something so basic and useless?

This was written for a class project. The purpose was to understand the basics
of TCP connections and how the application layer of the network stack is
responsible for formulating valid HTTP responses and handling incoming HTTP
requests.

So yes, while it may be useless in the grand scheme of things, it's already
served its purpose of educating me and any passerbys on the concepts behind web
servers.

> Why did you write it in Python 2.7?

Because that's all I had installed on my Mac at the time and I didn't feel like
installing the Python 3.5 runtime. I would have preferred 3.5, but whatever.

> Wait, why are you using a Mac?

Next question please.

> Did anyone really ask you these questions?

Nope.

## Usage

> How do I run your code?

1. Make sure you have python 2.7 installed on your computer
2. Clone the repo to your computer
3. Open the cloned directory in your terminal/command prompt
4. Type `python httpserver.py`
