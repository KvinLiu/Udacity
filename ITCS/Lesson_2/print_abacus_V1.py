def print_abacus(i):
	s,r,n = "00000*****", str(10 ** 10 + i), 1
	while n < 11:
		print "|" + s[:10 - int(r[n])] + "   " + s[10 - int(r[n]):] + "|"
		n = n + 1