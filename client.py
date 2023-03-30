import socket

HOST = 'localhost'  # Endereço IP do servidor
PORT = 5000  # Porta do servidor

# Cria um objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
s.connect((HOST, PORT))

# Envia uma mensagem para o servidor
s.sendall('Olá, servidor!'.encode())

# Aguarda uma resposta do servidor
data = s.recv(1024)

# Imprime a resposta recebida
print(f'Resposta do servidor: {data.decode()}')

# Fecha a conexão
s.close()