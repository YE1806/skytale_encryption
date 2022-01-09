import argparse

def encrypt(word, number):
	a = word
	u = number

	t = len(a)//u
	diff = u*(t+1)-len(a)
	if len(a)%u != 0:
		for i in range(diff):
			a += '.'

	k = len(a)//u

	tmp = []
	for i in range(u):
		tmp.append('')

	for i in range(0,len(a), u):
		if i+u >= len(a):
			if len(a)%u == 0:
				for j in range(u):
					tmp[j] += a[i+j]
			else:
				for j in range(len(a)-i):
					tmp[j] += a[i+j]
				break
		else:
			for j in range(u):
				tmp[j] += a[i+j]

	result1 = ""
	for element in tmp:
		result1 += element

	print("Encrypted: ", result1)

def decrypt(word, number):
	a = word
	u = number
	k = len(a)//u
	if len(a)%u != 0:
		k += 1

	r = []

	for i in range(k):
		r.append('')

	for i in range(0, len(a), k):
		if i+k >= len(a):
			for j in range(len(a)-i):
				r[j] += a[i+j]
			break
		for j in range(k):
			r[j] += a[i+j]
		i = i+j

	result = ""
	for element in r:
		result += element
	print("Decrypted: ", result) 

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Skytale encryption/decryption.')
	parser.add_argument('-enc', help='-enc [text to encrypt]')
	parser.add_argument('-dec', help='-dec [text to decrypt]')
	parser.add_argument('-n', help='Number of U')
	args, leftovers = parser.parse_known_args()
	args = parser.parse_args()

	if args.enc is not None:
		print("Encrpyting ", args.enc)
		encrypt(args.enc, int(args.n))
	if args.dec is not None:
		print("Decrypting: ", args.dec)
		decrypt(args.dec, int(args.n))