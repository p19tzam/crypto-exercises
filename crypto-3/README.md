### Crypto excercise 3

# Server

```python
#!/usr/bin/env python3
import socket, os, sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
```

Στις πρώτες γραμμές κώδικα κάνω import τα modules για crypto και rsa(PKCS1_OAEP). Public key cryptography standard 1(ο αριθμός 1 αντικατοπτρίζει τον RSA). 


```python
private_key=RSA.import_key(open('PrivateKey.pem', 'r').read())
```
Αρχικοποίηση του private key στον server για την αποκρυπτογράφηση του key. \
Χρησιμοποιώ το RSA.import_key για να κάνω read το RSA key που έχω κάνει generate απο τον κώδικα [generate.py](https://github.com/p19tzam/crypto-exercises/blob/main/crypto-3/scripts/GenerateRSA.py).

### main

```python

host = '127.0.0.1' # η IP που “ακούει” ο server δηλαδή η IP που θα επικοινωνήσει ο client
port = 50033 # h PORT που “ακούει” ο server δηλαδή η PORT που θα επικοινωνήσει ο client
s = socket.socket() # Εδώ δημιουργώ ενα TCP socket.
s.bind((host,port)) # Kάνει bind στο host και port
print("server Started")
s.listen(1) # εδώ λέει οτι δέχεται 1 client 
```



```python
while true:
    	c, addr = s.accept() # κάνει accept τα connections απο client
    	print("Connection from: " + str(addr))
    	data = c.recv(4096).decode()  # δέχεται data απο το client και έχει buffer 4096 bytes και κάνει decode.
    
    	data=data.split('\n') # Διαχωρίζω τα string data που δέχομαι με newline

    	rsaEnckey=bytes.fromhex(data[0]) # 0=rsa encrypted key
    	iv=bytes.fromhex(data[1]) # 1=iv for decryption
    	ciphertext=bytes.fromhex(data[2]) # 2=ciphertext for message decryption
       
    	rsaKeydecrypt=PKCS1_OAEP.new(key=private_key) # το ciphertext του rsa encryption και δίνω 
    	decrypted_key=rsaKeydecrypt.decrypt(rsaEnckey) # decrypt rsa και έχουμε το key

    	cipher=AES.new(decrypted_key, AES.MODE_CBC,iv) # κάνει decrypt το key σαν cleartext

    	binary_plaintext=unpad(cipher.decrypt(ciphertext), AES.block_size) # και κάνουμε decrypt το message απο τον client.

    	decrypted_msg=binary_plaintext.decode() # decode απο bytes σε text
    	print(decrypted_msg) # print
```

[Source code](https://github.com/p19tzam/crypto-exercises/blob/main/crypto-3/scripts/server.py)

# Client

```python
#!/usr/bin/env python3 
import socket, os.path, datetime, sys, rsa
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
```

Στις πρώτες γραμμές κώδικα κάνω import τα modules για crypto και rsa(PKCS1_OAEP). Public key cryptography standard 1(ο αριθμός 1 αντικατοπτρίζει τον RSA). 

```python
key=get_random_bytes(16) # generate random 16 bytes key
iv=get_random_bytes(16) # generate random 16 bytes key
public_key=RSA.import_key(open('PublicKey.pem', 'r').read()) # Αρχικοποίηση του public key στον client για την κρυπτογράφηση του key. \
```

Χρησιμοποιώ το RSA.import_key για να κάνω read το RSA key που έχω κάνει generate απο τον κώδικα 


```python
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

    s.close() # close the socket
```

