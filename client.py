import socket
from lib import	*

HOST = 'localhost'  # Endereço IP do servidor
PORT = 5000  # Porta do servidor

# Cria um objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
s.connect((HOST, PORT))

private_key, public_key = loadKeys()
print("chaves carregadas")

while True:
    # recebe uma mensagem da entrada e manda para o servidor
    message = input("sua mensagem: ").encode()
    enc_message = rsa.encrypt(message, public_key)

    s.sendall(enc_message)
    if(message.decode() == 'endconn'): break

    # Aguarda uma resposta do servidor
    data = s.recv(4096)
    message_server = data
    dec_message = rsa.decrypt(message_server, private_key).decode()

    if(dec_message == 'endconn'): break

    # Imprime a resposta recebida
    print(f'Servidor: {dec_message}')

# Fecha a conexão
s.close()