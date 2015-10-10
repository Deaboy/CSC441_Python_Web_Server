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

"Dan, why would you write something so basic and useless?"

This was written for a class project. The purpose was to understand the basics
of TCP connections and how the application layer of the network stack is
responsible for formulating valid HTTP responses and handling incoming HTTP
requests.

