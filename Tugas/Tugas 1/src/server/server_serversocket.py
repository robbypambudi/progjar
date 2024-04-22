import os
import signal
import socket


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class Server:
    def __init__(self, host, port):
        # TODO:
        # 1. Define host and port
        # 2. Create a socket
        # 3. Bind the socket to the host and port
        self.host = ???
        self.port = ???
        self.socket = ???
        self.socket.bind((???, ???))

    def start(self):
        # TODO:
        # 1. Listen for incoming connections
        ???
        # print(f"Server listening on {self.host}:{self.port}")
        while True:
            # 2. Accept incoming connections
            conn, addr = ???
            # print(f"Connected by {addr}")

            # 3. Receive command and filename from client
            data = ???
            command, filename = ???

            # 4. Check if the command is "download"
            if ???:
                # 4.1 If not, send an error message to the client: "Unknown command"
                # print(f'Unknown command: {command}')
                ???
                continue

            # print(f'Requested file: {filename}')

            # 5. Check if the file exists
            # 5.1 If not, send an error message to the client: "File doesn't exists"
            filepath = ???
            if not os.path.exists(filepath):
                ???

            filesize = ???

            # 6. Send the header to the client
            # 6.1 Header format: "file-name: <filename>,\r\nfile-size: <filesize>\r\n\r\n"
            header = ???
            ???

            # 7. Send the file to the client
            with open(???, ???) as f:
                while True:
                    ???

            # 8. Close the connection
            ???


def handler(signum, frame):
    raise Exception("end of time")


if __name__ == "__main__":
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(60)
    try:
        server = Server("127.0.0.1", 65432)
        server.start()
    except Exception as e:
        signal.alarm(0)
