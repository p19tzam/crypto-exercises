#Dhmosten Tzama 2019213

#!/usr/bin/env python3
import socket, os, sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

private_key=RSA.import_key(open('PrivateKey.pem', 'r').read())

def main():
    host = '127.0.0.1'
    port = 50033

    s = socket.socket()
    s.bind((host,port))
    print("server Started")
    s.listen(1)
    while True:
        c, addr = s.accept()
        print("Connection from: " + str(addr))
        data = c.recv(4096).decode()
	
        data=data.split('\n')

        rsaEnckey=bytes.fromhex(data[0])
        iv=bytes.fromhex(data[1])
        ciphertext=bytes.fromhex(data[2])
	   
        rsaKeydecrypt=PKCS1_OAEP.new(key=private_key)
        decrypted_key=rsaKeydecrypt.decrypt(rsaEnckey)

        cipher=AES.new(decrypted_key, AES.MODE_CBC,iv)

        binary_plaintext=unpad(cipher.decrypt(ciphertext), AES.block_size)

        decrypted_msg=binary_plaintext.decode()
        print(decrypted_msg)


        c.send('OK'.encode())
        c.close()

if __name__ == '__main__':
    main()
