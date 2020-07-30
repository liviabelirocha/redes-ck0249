from socket import *
import sys

def main():
    server_port = 3333
    server_socket = socket(AF_INET, SOCK_STREAM) # IPv4, TCP
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # poder reutilizar o server sem espera ser necessária
    server_socket.bind(('', server_port))
    server_socket.listen(1)
    print("Server ready")

    while 1:
        connection_socket, addr = server_socket.accept()
        print("Request accepted")

        request(connection_socket)

        print("Closing server")
        server_socket.close()
        sys.exit()

def request(connection_socket):
    try:
        message = connection_socket.recv(1024)
        
        filename = message.split()[1] 
        file = open(filename[1:], 'r')
        output = file.read()
        print("File was found")

        header = "200 OK\n\n"
        connection_socket.send(header.encode())    
        connection_socket.send(output.encode())
        
        print("File sent successfully")

    except IOError:
        print("File not found")
        header = "404 Not Found"
        connection_socket.send(header.encode())
    
    print("Closing connection")
    connection_socket.close()

if __name__ == '__main__':
    main()