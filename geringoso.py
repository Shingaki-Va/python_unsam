#cadena = 'Geringoso'
vocales = "a e i o u"
print("Bienvenido al conversor de palabras a Geringoso")
cadena = input("Ingrese la palabra a traducir: ")

for c in cadena:
	result = c

	if c in vocales:
		result += "p"+c
	else:
		result= c

	print(result, end="")	
print()		

		

