def calcular_porcentaje_error(lecturas):
lecturas_erroneas = 0
for i in range(1,lecturas + 1):
temperatura = float(input(f"Inserta la temperatura ((i)):"))  
if temperatura < 10 or temperatura > 40 :
  lecturas_erroneas += 1

porcentaje_error = (lecturas_erroneas/lecturas) * 100

print(f"El sensor se equivicó (lecturas_erroneas)veces.")
print(f"El porcentaje de error del sensor es del (porcenatje_error)%")
