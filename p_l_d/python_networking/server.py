import socket # two computer use this to connect to each other
import sys

def create_socket():
    """create a socket that coennects two computer
    """
    try:
        global host
        global port
        global c

        host = ""
        port = 9999
        s = socket.socket() # create a socket

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the Port: " + str(port))
        s.bind((host, port)) # bind the host and port
        s.listen(5) # tolerance 5 bad connections before throwing an error

    except socket.error as msg:
        print("Socket bindning error: " + str(msg) + "\n" + "Retrying . . .")
        bind_socket()


