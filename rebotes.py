# rebotes.py
# Archivo de ejemplo
# Ejercicio

print("Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que toca el piso salta 3/5 de la altura desde la que cayó. ");
print()

altura = 100 
indice= 10         # altura en metros
num_billetes = 1
i = 0

while i < 10:
		
    print(i, round(altura*0.6,4))
    i = i + 1
    altura=altura*0.6



