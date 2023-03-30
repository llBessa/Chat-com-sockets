import socket

HOST = 'localhost'  # Endereço IP do servidor
PORT = 5000  # Porta do servidor

# Cria um objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
s.connect((HOST, PORT))

while True:
    # recebe uma mensagem da entrada e manda para o servidor
    message = input("sua mensagem: ").encode()

    s.sendall(message)
    if(message.decode() == 'endconn'): break

    # Aguarda uma resposta do servidor
    data = s.recv(1024)
    message_server = data.decode()

    if(message_server == 'endconn'): break

    # Imprime a resposta recebida
    print(f'Servidor: {message_server}')

# Fecha a conexão
s.close()