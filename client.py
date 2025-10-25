import os
import socket

# sets up server connection
host = "127.0.0.1"
port = 12345
server_information = (host, port)

# Creates server socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Takes file path as an input
file_path = input("Please input a file path: ")

if os.path.isfile(file_path):
    # Opens the file and stores the data in a variable
    with open(file_path, "rb") as f:
        file_data = f.read()

    #  Sends it to another computer
    try:
        client_socket.connect(server_information)
        client_socket.sendall(file_data)
        client_socket.recv(4096)
        client_socket.close()
    except Exception as e:
        print(f"Unexpected error: {e}")
else:
    print("Path is not a file.")