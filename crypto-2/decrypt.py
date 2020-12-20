from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import string
import random
from ctypes import c_int, c_uint
import os
import itertools

def srand(seed):
    srand.r = [0 for _ in range(34)]
    srand.r[0] = c_int(seed).value
    for i in range(1, 31):
        srand.r[i] = (16807 * srand.r[i - 1]) % 2147483647
    for i in range(31, 34):
        srand.r[i] = srand.r[i - 31]
    srand.k = 0
    for _ in range(34, 344):
        rand()


def rand():
    srand.r[srand.k] = srand.r[(srand.k - 31) % 34] + srand.r[(srand.k - 3) % 34]
    r = c_uint(srand.r[srand.k]).value >> 1
    srand.k = (srand.k + 1) % 34
    return r


def generate_random_key(KEYSIZE): 
	key = b''
	for i in range(KEYSIZE):
 		key += bytes([rand()%256])
	return key


srand(1606212503)
iv=bytes.fromhex('61f6ef5c567fbcfb99961becdd0954e0')
magicb=b'255044462d312e370a25e2e3cfd30a34'
KEYSIZE=16

with open('important.enc.pdf','rb') as encrypted_pdf_file:
	ciphertext=encrypted_pdf_file.read()


for i in itertools.count(start=1606212503):
	srand(i)

	tempkey=generate_random_key(KEYSIZE)

	cipher=AES.new(tempkey,AES.MODE_CBC,iv)

	plaintext=cipher.decrypt(ciphertext)
	
	if plaintext.hex()[0:32].encode()==magicb:
		os.system("clear")
		print("\n\n[!]=> Found key for decryption(bytes): ",tempkey)
		with open('important.pdf','wb') as decrypted_pdf_file:
			decrypted_pdf_file.write(plaintext)
		break
