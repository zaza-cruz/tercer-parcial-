def tienda_varitas():
  clientes_totales = 0
  clientes_compraron = 0
  ventas_varitas = [0, 0, 0, 0]  # Contador de ventas para cada tipo de varita

  while True:
      entra_cliente = input("¿Entra un cliente? (si/no): ")
      if entra_cliente.lower() != 'si':
          break

      clientes_totales += 1

      compra_algo = input("¿Compró algo? (si/no): ")
      if compra_algo.lower() == 'si':
          clientes_compraron += 1

          print("Varitas disponibles:")
          print("1. Varita de Saúco\n2. Varita de Espino\n3. Varita de Sauce\n4. Varita de Acebo")

          varita_elegida = int(input("¿Qué varita compró? Elige 1, 2, 3 o 4: "))
          if 1 <= varita_elegida <= 4:
              ventas_varitas[varita_elegida - 1] += 1

  print(f"\nClientes totales: {clientes_totales}")
  print(f"Clientes que compraron: {clientes_compraron}")
  print("Clientes que no compraron: ", clientes_totales - clientes_compraron)

  for i in range(4):
      varita_plural = "varitas" if ventas_varitas[i] != 1 else "varita"
      print(f"Hoy se vendieron {ventas_varitas[i]} {varita_plural} de {nombre_varita(i + 1)}.")

  print("¡Qué gran día para Ollivanders!")

def nombre_varita(numero):
  nombres = ["Varita de Saúco", "Varita de Espino", "Varita de Sauce", "Varita de Acebo"]
  return nombres[numero - 1]

# Ejecutar el programa
tienda_varitas()
