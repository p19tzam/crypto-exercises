#Dhmosten Tzama 2019213

#!/usr/bin/env python3 
import socket, os.path, datetime, sys, rsa
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key=get_random_bytes(16)
iv=get_random_bytes(16)
public_key=RSA.import_key(open('PublicKey.pem', 'r').read())

def main():
    host = '127.0.0.1'
    port = 50033

    s = socket.socket()
    s.connect((host, port))

    cipherRSA=PKCS1_OAEP.new(key=public_key)
    ciphertextRSA=cipherRSA.encrypt(key)

    msg=str(input("Encrypted message for server: "))
    binMsg=msg.encode('utf-8') #convert to bytes

    cipher=AES.new(key, AES.MODE_CBC,iv)
    ciphertext=cipher.encrypt(pad(binMsg, AES.block_size)) #ciphertext

    data=str(ciphertextRSA.hex())+"\n"+str(iv.hex())+"\n"+str(ciphertext.hex())+"\n"

    s.send(data.encode())
    ack = s.recv(4096).decode()
    print("I received from server this message:",ack)

    s.close()

if __name__ == '__main__':
    main()
