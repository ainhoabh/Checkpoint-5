# Cree un bucle For de Python

nombres = ['María', 'Ana', 'Pedro']
nombres_sin_a = []

for nombre in nombres:
  if 'a' not in nombre:
    nombres_sin_a.append(nombre)

print(nombres_sin_a)


# Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.

def suma(num1, num2, num3):
  return num1 + num2 + num3

print(suma(2,3,5))


# Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.

suma = lambda num1, num2, num3: num1 + num2 + num3

print(suma(2,3,5))


# Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.

nombre = 'Enrique'

lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

if nombre in lista_nombre:
  print('El nombre está en la lista.')
else:
  print('El nombre no está en la lista')
