cadena = 'Geringoso'
vocales = "a e i o u"


for c in cadena:
	result = c

	if c in vocales:
		result += "p"+c
	else:
		result= c

	print(result, end="")	
print()		

		

