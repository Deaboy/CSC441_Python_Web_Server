"""
Author: Daniel Andrus
Date: 2015-10-09
Course: CSC 441: Networking/Data Communications
Professor: Dr. Mengyu Qiao
"""

import atexit
import socket
import os

# define server constants
TCP_IP = ''             # bind to any IP
TCP_PORT = 80           # bind to default port 80
BUFFER_SIZE = 1024

# Prepare a seversocket with port number
s = socket.socket()         # create socket object
s.bind((TCP_IP, TCP_PORT))  # bind object to port
s.listen(1)                 # listens to port

print ('Server online')

def exit_handler():
    s.close()
    print('\nServer closed')



def main():
    
    while True: 
        print('Ready to serve')

        # accept and process incoming connections
        c = 0
        addr = 0

        # close graciously when user kills server
        try:
            c, addr = s.accept()
        except KeyboardInterrupt:
            break

        client_ip, client_port = addr

        # print connection info
        print ('Connection from ' + client_ip + ':' + str(client_port))

        file_path = ''

        try:
            # receive HTTP request
            data = c.recv(BUFFER_SIZE)
            #print (data)

            # tokenize HTTP message header
            http_request = data
            http_lines = data.split("\n")

            # find filename in the message string array (use split function)
            for line in http_lines:
                line_items = line.split(' ')
                if line_items[0] == 'GET':
                    file_path = line_items[1]
                    break

            print ('requesting file ' + file_path)
            file_path = '.' + file_path.replace('%20', ' ')

            # manipulate file_path to work with file system
            if os.path.isdir(file_path):
                file_path = file_path + ('' if file_path.endswith('/') else '/') + 'index.html'

            # open the requested file
            file_object = open(file_path, 'r')

            print ('serving file: ' + file_path)

            #read the file into a string
            file_content = file_object.read()

            #close the file
            file_object.close()

            #Send one HTTP header line into socket *check the header for 200 OK, and add an empty line at the end
            c.send('HTTP/1.1 200 OK\n\n')

            #Send the data content of the requested file to the client (may need a loop)
            c.send(file_content)

        except IOError:
            print ('file not found: ' + file_path)

            # unable to open file: send 404
            c.send('HTTP/1.1 404 Not Found\n\n')

            try:
                # attempt to find and send custom 404 error page
                file_object = open('404.html', 'r')
                file_content = file_object.read()
                file_object.close()
                c.send(file_content)

            except IOError:
                # 404.html file not found, send default 404 page
                c.send('<html><head><title>404 Not Found</title></head><body><h1>Not Found</h1><p>The requested URL was not found on this server.</p></body></html>')

        except Exception as e:
            print ('an error occured:')
            print (e)

            # send 500 page to user
            c.send('HTTP/1.1 500 Internal Server Error\n\n')
            c.send('<html><head><title>500 Internal Server Error</title></head><body><h1>Internal Server Error</h1><p>The server encountered an error while processing your request.</p></body></html>')

        finally:
            # Close client socket 
            c.close()

    # close serversocket
    s.close()


atexit.register(exit_handler)

try:
    main()
except KeyboardInterrupt:
    pass
    