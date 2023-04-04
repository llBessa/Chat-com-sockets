import socket
import threading
from lib import *

HOST = ''
PORT = 5000

clientes = []

def transmitir_mensagem(mensagem, remetente):
    for cliente in clientes:
        if cliente != remetente:
            cliente.send(mensagem)

def lidar_com_cliente(cliente_socket, endereco):
    print(f"Conexão estabelecida com {endereco}")
    
    clientes.append(cliente_socket)
    
    while True:
        mensagem = cliente_socket.recv(1024)
        mensagem_traduzida = rsa.decrypt(mensagem, privateKey).decode()
        if not mensagem:
            break
        
        mensagem_formatada = f"{endereco}: {mensagem_traduzida}"
        print(mensagem_formatada)
        mensagem_formatada_criptografada = rsa.encrypt(mensagem_formatada.encode(), publicKey)
        transmitir_mensagem(mensagem_formatada_criptografada, cliente_socket)
    
    clientes.remove(cliente_socket)
    cliente_socket.close()
    print(f"Conexão fechada com {endereco}")

# Cria as chaves publica e privada para criptografia e as salva
generateKeys()
privateKey, publicKey = loadKeys()
print("Chaves geradas com sucesso!")

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.bind((HOST, PORT))
servidor_socket.listen(5)

print(f"Servidor escutando na porta {PORT}")

while True:
    cliente_socket, endereco = servidor_socket.accept()
    thread_cliente = threading.Thread(target=lidar_com_cliente, args=(cliente_socket, endereco))
    thread_cliente.start()
