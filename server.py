import socket
import os

# Server information
HOST = "127.0.0.1"
PORT = 12345

# Sets up server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Server is listening on {HOST}:{PORT}")

# Accept client connection
client_connection, addr = server_socket.accept()
print(f"Connection established with {addr}")

# Ask where to save incoming file
destination_folder = input("Input folder path where file should be saved: ").strip()
if not os.path.isdir(destination_folder):
    print("Invalid directory. Exiting.")
    client_connection.close()
    server_socket.close()
    exit(1)

try:
    # Receive filename first (until newline)
    filename = b""
    while True:
        chunk = client_connection.recv(1)
        if chunk == b"\n" or not chunk:
            break
        filename += chunk

    filename = filename.decode()
    destination_path = os.path.join(destination_folder, filename)
    print(f"Receiving file: {filename}")

    # Now receive the file data and write it
    with open(destination_path, "wb") as f:
        while True:
            data = client_connection.recv(4096)
            if not data:
                break
            f.write(data)

    print(f"File successfully received and saved to {destination_path}")

    # Send acknowledgment to client
    client_connection.sendall(b"File received successfully.")

except Exception as e:
    print(f"Error encountered: {e}")

finally:
    client_connection.close()
    server_socket.close()
import socket
import os

# Server information
HOST = "127.0.0.1"
PORT = 12345

# Sets up server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Server is listening on {HOST}:{PORT}")

# Accept client connection
client_connection, addr = server_socket.accept()
print(f"Connection established with {addr}")

# Ask where to save incoming file
destination_folder = input("Input folder path where file should be saved: ").strip()
if not os.path.isdir(destination_folder):
    print("Invalid directory. Exiting.")
    client_connection.close()
    server_socket.close()
    exit(1)

try:
    # Receive filename first (until newline)
    filename = b""
    while True:
        chunk = client_connection.recv(1)
        if chunk == b"\n" or not chunk:
            break
        filename += chunk

    filename = filename.decode()
    destination_path = os.path.join(destination_folder, filename)
    print(f"Receiving file: {filename}")

    # Now receive the file data and write it
    with open(destination_path, "wb") as f:
        while True:
            data = client_connection.recv(4096)
            if not data:
                break
            f.write(data)

    print(f"File successfully received and saved to {destination_path}")

    # Send acknowledgment to client
    client_connection.sendall(b"File received successfully.")
except Exception as e:
    print(f"Error encountered: {e}")
finally:
    client_connection.close()
    server_socket.close()