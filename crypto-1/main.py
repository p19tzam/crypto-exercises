#Dhmosten Tzama
#A.M. 2019213
#version Python 2.7

import os,sys

from affineCipher import *
from vigenereCipher import *
from substitutionCipher import *


def menuChoiceCheck(choice):
	while(choice!="0" and choice!="1" and choice!="2"):
		print "Select right cipher..!\n"
		choice=raw_input("Choice:>> ")
	return choice

def menu():
	print "\nPlease select cipher \n0:Affine\n1:Vigerene\n2:Substitution"


def main():
	os.system("clear")
	menu()
	choice=raw_input("Choice:>> ")
	choice=menuChoiceCheck(choice)

	os.system("clear")

	if choice=="0": #Affine
		key=getRandomKeyaAFF()
		os.system("clear")
		print "[Affine Cipher]\n"
		message=raw_input("Please type the message to be encrypted: ")
		print "\nGenerating Random key for Affine cipher...\n"
		encryptedMsg = encryptAFF(key, message)
		decryptedMsg = decryptAFF(encryptedMsg,key)
		print "The ciphertext is: ",encryptedMsg
		print "The plaintext is: ",decryptedMsg
		print ""

	elif choice=="1": #Vigerene
		os.system("clear")
		print "[Vigerene Cipher]\n"
		message=raw_input("Please type the message to be encrypted: ")
		print "\n\n"
		encryptedMsg = encryptVIG('P2019213', message)
		decryptedMsg = decryptVIG('p2019213',encryptedMsg)
		print "The ciphertext is: ",encryptedMsg
		print "The plaintext is: ",decryptedMsg
		print ""

	else: #Substitution
		key=getRandomKeySUB() #from substituion file functions
		os.system("clear")
		print "[Substitution Cipher]\n"
		message=raw_input("Please type the message to be encrypted: ")
		print "\nGenerating Random key for Substitution cipher...\n"
		encryptedMsg = encryptSUB(message,key)
		decryptedMsg = decryptSUB(encryptedMsg,key)
		print "The ciphertext is: ",encryptedMsg
		print "The plaintext is: ",decryptedMsg
		print ""

if __name__=='__main__':
	main()
