def asistente(texto):
palabras = texto.split()
veces_alexa = palabaras.count('alexa')

if veces_alexa == 1:
  return "Hola"
 elif veces_alexa> 1:
  return"tranquilo solo di mi nombre una vez "
