from genericpath import isfile
import socket

# sets up server connection
host = "127.0.0.1"
port = 12345
server_information = (host, port)

# Creates server socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Takes file path as an input
file_path = input("Please input a file path: ")

if file_path.isfile():
    # Opens the file and stores the data in a variable
    with open(file_path, "rb") as f:
        file_data = f.read()
        file_data.encode()

    #  Sends it to another computer
    try:
        client_socket.connect(server_information)
        client_socket.send(file_data)
        client_socket.recv(1024)
        client_socket.close()
    except Exception as e:
        print(f"Unexpected error: {e}")
else:
    print("Path is not a file.")