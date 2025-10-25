import socket
import os

# Server information
host = "127.0.0.1"
port = 12345
server_information = (host, port)

# Sets up server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_information)
server_socket.listen()
print(f"Server is listening on {host}:{port}")

# Accepts client connection
client_connection, addr = server_socket.accept()
print(f"Connection established with {addr}")

# Decides destination folder
destination = input("Input folder path where data is to go: ").strip()

if not os.path.isdir(destination):
    print("Path is not a directory.")
    client_connection.close()
    server_socket.close()
    exit(1)

try:
    # Receive the filename first
    filename = client_connection.recv(1024).decode().strip()
    print(f"Receiving file: {filename}")

    # Create full save path
    save_path = os.path.join(destination, filename)

    # Acknowledge filename received
    client_connection.sendall(b"Filename received")

    # Receive the file data
    with open(save_path, "wb") as f:
        while True:
            data = client_connection.recv(4096)
            if not data:
                break
            f.write(data)

    print(f"File successfully received and saved to {save_path}")

    # Send acknowledgment back to client
    client_connection.sendall(b"File received successfully.")

except Exception as e:
    print(f"Error encountered: {e}")

finally:
    client_connection.close()
    server_socket.close()