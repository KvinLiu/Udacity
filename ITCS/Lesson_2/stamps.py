def stamps(n):
	if n > 0:
		a = n / 5
		b = (n - 5 * a) / 2
		c = n - 5 * a - 2 * b
		return (a, b, c)
	else:
		return "Please Positive Integer!"

	