import socket

HOST = ''  # Endereço IP do servidor
PORT = 5000  # Porta que o servidor vai escutar

# Cria um objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o objeto socket ao endereço e porta especificados
s.bind((HOST, PORT))

# Define o limite máximo de conexões simultâneas
s.listen(1)

print(f'Servidor escutando na porta {PORT}...')

# Aguarda uma conexão
conn, addr = s.accept()
print(f'Conectado por {addr}')

while True:
    # Aguarda uma mensagem do cliente
    data = conn.recv(1024)
    client_message = data.decode()

    if(client_message == 'endconn'): break

    print(f'Cliente: {client_message}')

    # Envia uma resposta para o cliente
    message = input("sua mensagem: ").encode()
    conn.sendall(message)
    if(message.decode() == 'endconn'): break

# Fecha a conexão
conn.close()
