import RSA_Keygen
import RSA_Encryption
from isPrime import is_prime
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def getInput():

	validInput = False

	while not validInput:

		p = int(input(bcolors.OKCYAN + "Enter any prime number eg. (13, 17, 19, 23...): " + bcolors.ENDC))
		q = int(input(bcolors.OKCYAN + "Enter a DIFFERENT prime number eg. (13, 17, 19, 23...): " + bcolors.ENDC))
		m = input(bcolors.OKCYAN + "Enter a message to encrypt eg. (Hello, M, Test, Python) " + bcolors.ENDC)

		if (not is_prime(p) or not is_prime(q)):
			os.system('cls')  
			print(bcolors.FAIL + "One of your numbers is not a prime number!" + bcolors.ENDC)

		elif(p == q):
			os.system('cls')  
			print(bcolors.FAIL + "Your two prime numbers are the same!" + bcolors.ENDC)

		elif(p*q < len(m)):
			os.system('cls')  
			print(bcolors.FAIL + "Your message is too large or your prime numbers are too small" + bcolors.ENDC)

		else:
			print('\n\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
			validInput = True

		m = modifyInput(m)

	return p, q, m

def modifyInput(message):
	
	if len(message) > 1:
		msg = int(''.join(str(ord(c)) for c in message))
	else:
		msg = int(ord(message))

	return msg

def main():

	p, q, msg = getInput()

	kg = RSA_Keygen.Generator()
	kg.setPrimes(p, q)
	kg.calculate()

	print(bcolors.HEADER + f"\nPublic Key: ({kg.getPublicKey()},{kg.n})" + bcolors.ENDC)
	print(bcolors.HEADER +"Private Key: ", kg.getPrivateKey(), bcolors.ENDC)

	

	print(bcolors.BOLD + "\nMessage: ", msg, bcolors.ENDC)

	er = RSA_Encryption.Cipher()
	cyphertext = er.crypt(msg, kg.getPublicKey(), kg.n)
	print(bcolors.BOLD + "Encrypted Text: ", cyphertext, bcolors.ENDC)

	text = er.crypt(cyphertext, kg.getPrivateKey(), kg.n)
	print(bcolors.BOLD + "Unencrypted Text: ", text, bcolors.ENDC)

if __name__ == "__main__":
	main()