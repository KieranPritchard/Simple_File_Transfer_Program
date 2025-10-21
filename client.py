import socket

# sets up server connection
host = "127.0.0.1"
port = 12345
server_information = (host, port)

# Creates server socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Takes file path as an input
file_path = input("Please input a file path: ")

# Opens the file and stores the data in a variable

#  Sends it to another computer
