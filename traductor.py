print("Bienvenide al Traductor a Lenguage inclusivo")
print()
#print("Ingrese la Fase a traducir:")
#frase=input()

frase = 'todos somos programadores'
palabras = frase.split()
palabras_inclusive = []
frase_inclusive = []

for palabras in palabras:
    if palabras[-1] == "o":
        for p in palabras:
            palabras_inclusive.append(p)
        palabras_inclusive[-1] = "e"
        palabras_inclusive="".join(palabras_inclusive)
    elif palabras[-2] == "o":
        for p in palabras:
            palabras_inclusive.append(p)
        palabras_inclusive[-2] = "e"
        palabras_inclusive="".join(palabras_inclusive)
    else:
        for p in palabras:
            palabras_inclusive.append(p)
        palabras_inclusive = "".join(palabras_inclusive)
    frase_inclusive.append(palabras_inclusive)
    palabras_inclusive = []
frase_inclusive = " ".join(frase_inclusive)

print(frase_inclusive)
