from socket import *
import sys

def main():
    server_port = 3333
    server_socket = socket(AF_INET, SOCK_STREAM) # IPv4, TCP
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # poder reutilizar o server sem espera ser necessária
    server_socket.bind(('', server_port))
    server_socket.listen(1)
    print("Servidor iniciado e pronto para receber uma requisição")

    while 1:
        connection_socket, addr = server_socket.accept()
        print(f"Requisição aceita vindo de {addr}")

        request(connection_socket)

def request(connection_socket):
    try:
        message = connection_socket.recv(1024).decode()
        filename = message.split()[1] 
        file = open(f'./files/{filename[1:]}.txt', 'r')
        output = file.read()
        print("O arquivo foi encontrado")

        header = "HTML/1.1 200 OK\n\n"
        connection_socket.send(header.encode())
        for i in range(0, len(output)):
            connection_socket.send(output[i].encode())
        
        print("Arquivo enviado com sucesso")

    except IOError:
        print("Arquivo não encontrado")
        header = "HTML/1.1 404 Not Found"
        connection_socket.send(header.encode())
    
    print("Servidor pronto para receber outra requisição")
    connection_socket.close()

if __name__ == '__main__':
    main()