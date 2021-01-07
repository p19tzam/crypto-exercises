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

Στις πρώτες γραμμές κώδικα κάνω import τα modules για crypto και rsa(PKCS1_OAEP). Public key cryptography standard 1(ο αριθμός 1 αντικατοπτρίζει τον RSA). \


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
    	c, addr = s.accept() # κάνει accept τα connections απο client
    	print("Connection from: " + str(addr))
    	data = c.recv(4096).decode()  # δέχεται data απο το client και έχει buffer 4096 bytes και κάνει decode.
    
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
```
