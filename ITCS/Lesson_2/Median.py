def bigger(a,b):
	result = a
	if b > a:
		result = b
	return result

def biggerst(a,b,c):
	return bigger(bigger(a,b),c)

def median(a,b,c):
	if a == biggerst(a,b,c):
		return bigger(b,c)
	if b == biggerst(a,b,c):
		return bigger(a,c)
	if c == biggerst(a,b,c):
		return bigger(a,b)
		