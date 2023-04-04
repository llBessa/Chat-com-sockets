import socket
import threading
from lib import *

HOST = 'localhost'
PORT = 5000

# carrega as chaves publica e privada
privateKey, publicKey = loadKeys()

def receber_mensagens(cliente_socket):
    while True:
        mensagem = cliente_socket.recv(1024)
        mensagem_traduzida = rsa.decrypt(mensagem, privateKey).decode()
        print(mensagem_traduzida)

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect((HOST, PORT))

thread_receber = threading.Thread(target=receber_mensagens, args=(cliente_socket,))
thread_receber.start()

while True:
    mensagem = input().encode()
    mensagem_criptografada = rsa.encrypt(mensagem, publicKey)
    cliente_socket.send(mensagem_criptografada)