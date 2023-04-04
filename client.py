import socket
import threading

HOST = 'localhost'
PORT = 5000

def receber_mensagens(cliente_socket):
    while True:
        mensagem = cliente_socket.recv(1024).decode('utf-8')
        print(mensagem)

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect((HOST, PORT))

thread_receber = threading.Thread(target=receber_mensagens, args=(cliente_socket,))
thread_receber.start()

while True:
    mensagem = input("Digite uma mensagem: ")
    cliente_socket.send(mensagem.encode('utf-8'))
