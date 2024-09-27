import numpy as np
import itertools

cipher = np.loadtxt('0059xordecryption\\0059_cipher.txt',delimiter=',',dtype=int)

def decrypt(message,key):
	return "".join([chr(char) for char in message^np.tile(key,485)])


'''
keys = list(itertools.product(np.linspace(97,122,26,dtype=int),repeat=3))
for key in keys:
	decodedmessage = decrypt(cipher,key)
	if "the" in decodedmessage and "and" in decodedmessage:
		print(key)
		print(decodedmessage)
		'''


print(sum(map(ord,decrypt(cipher,(101, 120, 112)))))