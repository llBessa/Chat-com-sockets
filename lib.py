import rsa
import os
import signal
# gera as chaves publica e privada na pasta keys
def generateKeys():
    (publicKey, privateKey) = rsa.newkeys(512)
    with open('keys/publicKey.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1())
    with open('keys/privateKey.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1())

# retorna o valor das chaves publica e privada em forma de tupla
def loadKeys():
    with open('keys/publicKey.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('keys/privateKey.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return privateKey, publicKey

# kill no processo do programa atual
def finalizar_programa():
    pid = os.getpid()
    os.kill(pid, signal.SIGINT)