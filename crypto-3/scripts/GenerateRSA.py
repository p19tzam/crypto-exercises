from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

rsaKeyParameters = RSA.generate(1024)  #Generate RSA parameters
keyPublic = rsaKeyParameters.publickey()  #extract from the generated RSA parameters only the (n,e) for the public key
pubKeyPEM = keyPublic.exportKey() #Convert the public key to a format named PEM. This function returns bytes.

pubKeyFile=open('PublicKey.pem','wb+') #Open a file name PublicKey.pem in write (w) and binary (b) mode.

pubKeyFile.write(pubKeyPEM)  #write the contexts of pubKeyPEM
pubKeyFile.close()  #close the file

#Here we do the same for the private key
privKeyPEM = rsaKeyParameters.exportKey()  

privateKeyFile=open('PrivateKey.pem','wb+')
privateKeyFile.write(privKeyPEM)
privateKeyFile.close()

