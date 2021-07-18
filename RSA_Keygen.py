from isPrime import is_prime

class Generator():

	def setPrimes(self, p, q):
		self.p = p
		self.q = q

	def calculate(self):
		self.calcN()
		self.calcPhi()
		self.calcE()
		self.calcD()

	def calcN(self):
		self.n = self.p * self.q

	def calcPhi(self):
		self.phi = (self.p - 1) * (self.q - 1)

	def calcE(self):
		# 1 < e < phi(n)
		# co-prime with phi(n) & n
		
		for e in range (2, self.phi):
			if gcd(e, self.phi) == 1:
				self.e = e
				break

	def calcD(self):
		# d * e % phi(n) = 1
		self.d = modInv(self.e, self.phi)

	def getPublicKey(self):
		return self.e

	def getPrivateKey(self):
		return self.d


def gcd(a, b):

	while a % b > 0:

	    R = a % b
	    a = b
	    b = R
	    
	return b

def gcdExtended(a, b):
	
	x0, x1, y0, y1 = 0, 1, 1, 0

	while a != 0:

		(q, a), b = divmod(b, a), a
		y0, y1 = y1, y0 - q * y1
		x0, x1 = x1, x0 - q * x1

	return b, x0, y0

def modInv(a, b):

	gcd, x, y = gcdExtended(a, b)

	if x < 0:
		x += b

	return x % b