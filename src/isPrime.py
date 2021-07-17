def is_prime(a):
	if (a==2):
		True
	elif ((a<2) or (a%2==0)):
		return False
	elif (a>2):
		for i in range(2, a):
			if not(a%i):
				return False

	return True