import os
import socket

# sets up server connection
host = "127.0.0.1"
port = 12345
server_information = (host, port)

# Creates client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Takes file path as an input
file_path = input("Please input a file path: ").strip()

if os.path.isfile(file_path):
    # Opens the file and stores the data in a variable
    with open(file_path, "rb") as f:
        file_data = f.read()

    # Extracts the file name
    file_name = os.path.basename(file_path)

    # Sends it to another computer
    try:
        client_socket.connect(server_information)

        # Send filename first
        client_socket.sendall(file_name.encode())
        client_socket.recv(1024)  # wait for ack

        # Then send the actual file
        client_socket.sendall(file_data)

        # Wait for final server confirmation
        client_socket.recv(4096)
        client_socket.close()

        print("File sent successfully.")

    except Exception as e:
        print(f"Unexpected error: {e}")

else:
    print("Path is not a file.")