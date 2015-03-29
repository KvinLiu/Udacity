def fix_machine(debris, product):
	a = len(product) - 1
	r = product
	while a > -1:
		if debris.find(product[a]) == -1:
			r = "Give me something that's not useless next time."
			break
		a = a - 1
	return r

#print fix_machine('UdaciousUdacitee', 'Udacity')
#print fix_machine('buy me dat Unicorn', 'Udacity')