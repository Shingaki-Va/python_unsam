# hipoteca.py
# Archivo de ejemplo
# Ejercicio
saldo = 500000.0 
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes=0
pago_extra = 1000

while saldo > 0 :
	pago_actual = pago_mensual + (pago_extra if mes<12 else 0)
	saldo = saldo * (1+tasa/12) - pago_actual
	total_pagado = total_pagado + pago_actual
	mes += 1
	
            

print('Total pagado', round(total_pagado, 2), "en: ", mes," meses")