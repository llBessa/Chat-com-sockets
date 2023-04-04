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
        mensagem = cliente_socket.recv(1024).decode('utf-8')
        if not mensagem:
            break
        
        mensagem_formatada = f"{endereco}: {mensagem}"
        print(mensagem_formatada)
        transmitir_mensagem(mensagem_formatada.encode('utf-8'), cliente_socket)
    
    clientes.remove(cliente_socket)
    cliente_socket.close()
    print(f"Conexão fechada com {endereco}")

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.bind((HOST, PORT))
servidor_socket.listen(5)

print(f"Servidor escutando na porta {PORT}")

while True:
    cliente_socket, endereco = servidor_socket.accept()
    thread_cliente = threading.Thread(target=lidar_com_cliente, args=(cliente_socket, endereco))
    thread_cliente.start()
