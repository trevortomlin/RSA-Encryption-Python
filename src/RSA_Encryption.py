class Cipher():

	def crypt(self, msg, key, n):
		text = pow(msg, key, n)
		return text