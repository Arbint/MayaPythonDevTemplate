import socket
import argparse

def send_file_to_maya(file_path):
    with open(file_path, "r") as file:
        python_code = file.read()

    send_to_maya(python_code)

def send_to_maya(code):
    host = "localhost"
    port = 7001

    maya_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    maya_socket.connect((host, port))

    maya_socket.sendall(code.encode())

    maya_socket.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send Python code to Maya")
    parser.add_argument("file", type=str, help="Path to the Python file to send to Maya")
    args = parser.parse_args()

    send_file_to_maya(args.file)
