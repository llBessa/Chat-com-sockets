import socket
import threading
from lib import *

HOST = ''
PORT = 5000

clientes = []

# manda a mensagem passada para todos os clientes conectados
def transmitir_mensagem(mensagem, remetente):
    for cliente in clientes:
        if cliente != remetente:
            cliente.send(mensagem)

def lidar_com_cliente(cliente_socket, endereco):
    print(f"Conexão estabelecida com {endereco}")
    
    # adiciona o cliente à lista
    clientes.append(cliente_socket)
    
    while True:
        # inicia o processo de leitura e tradução das mensagens enviadas pelos clientes
        mensagem = cliente_socket.recv(1024)
        mensagem_traduzida = rsa.decrypt(mensagem, privateKey).decode()
        if not mensagem:
            break
        
        mensagem_formatada = f"{endereco}: {mensagem_traduzida}"
        print(mensagem_formatada)
        # realiza a criptografia da mensagem utilizando a chave publica carregada
        mensagem_criptografada = rsa.encrypt(mensagem_formatada.encode(), publicKey)
        transmitir_mensagem(mensagem_criptografada, cliente_socket)
    
    clientes.remove(cliente_socket)
    cliente_socket.close()
    print(f"Conexão fechada com {endereco}")

# Cria as chaves publica e privada para criptografia e as salva
generateKeys()
privateKey, publicKey = loadKeys()
print("Chaves geradas com sucesso!")

# inicia um servidor com capacidade de até 5 clientes
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.bind((HOST, PORT))
servidor_socket.listen(5)

print(f"Servidor escutando na porta {PORT}")

while True:
    # o servidor começa a aceitar conexões
    cliente_socket, endereco = servidor_socket.accept()
    
    # quando uma nova conexão é realizada uma nova thread é iniciada com o intuito de receber
    # as mensagens do cliente e as repassar para todos os outros
    thread_cliente = threading.Thread(target=lidar_com_cliente, args=(cliente_socket, endereco))
    thread_cliente.start()
