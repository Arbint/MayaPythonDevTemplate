import socket

host = "localhost"
port = 7001

maya_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
maya_socket.connect((host, port))

maya_code = """
print("Hello from Python")
"""

maya_socket.sendall(maya_code.encode())

maya_socket.close()

