import os
import socket
import sys

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class Client:
    # TODO:
    def __init__(self, host, port):
        # 1. Define host and port
        # 2. Create a socket
        self.host = ???
        self.port = ???
        self.socket = ???

    def connect(self):
        # 3. Connect to the server
        ???(???)

    def send_message(self, message):
        # 4. Send a message to the server
        # 5. Receive a response from the server and return it
        ???(???)
        return ???

    def recv(self, size):
        # 6. Receive data from the server and return it
        return ???(???)

    def disconnect(self):
        # 7. Close the connection
        ???

    def parse_header(self, header):
        # 8. Parse the header and return the file name and size
        return ???, ???


if __name__ == "__main__":
    # TODO:
    # 1. Create a Client object
    client = ???
    # 2. Connect to the server
    ???

    # 3. Send a message to the server and receive a response
    message = input("Enter a message: ")
    status = ???

    # 4. Check if the response isn't a header
    # 4.1 If it is, print the response and exit
    if ???:
        ???

    # 5. Parse the header
    file_name, file_size = ???(???)
    file_path = ???

    # 6. Receive the file from the server and save it
    with open(???, ???) as f:
        while True:
            ???

    # 7. Close the connection
    ???
