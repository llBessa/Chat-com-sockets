import socket
import threading
from lib import *

HOST = 'localhost'
PORT = 5000

# carrega as chaves publica e privada
privateKey, publicKey = loadKeys()

def receber_mensagens(cliente_socket):
    while True:
        try:
            mensagem = cliente_socket.recv(1024)
            # realiza a tradução da mensagem utilizando a chave privada carregada
            mensagem_traduzida = rsa.decrypt(mensagem, privateKey).decode()
            if(mensagem_traduzida == "disconnect"):
                print("O servidor foi finalizado")
                finalizar_programa()

            print(mensagem_traduzida)
        except:
            break

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect((HOST, PORT))

print("Conexão com o servidor iniciada")
print("digite 'disconnect' para finalizar a conexão")

# inicia a thread de recebimento de mensagens
thread_receber = threading.Thread(target=receber_mensagens, args=(cliente_socket,))
thread_receber.start()

while True:
    mensagem = input().encode()
    # realiza a criptografia da mensagem utilizando a chave publica carregada
    mensagem_criptografada = rsa.encrypt(mensagem, publicKey)
    cliente_socket.send(mensagem_criptografada)
    # finaliza a conexão
    if(mensagem.decode().lower() == "disconnect"): break