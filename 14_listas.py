# mi_lista = ['a','b','c','d']

# print(type(mi_lista))

# otra_lista = ['hola', 55, 6.1]

# resultado = len (mi_lista)

# print(resultado)

# resultado = mi_lista[2]
# print(resultado)

# resultado = mi_lista.index("c")
# print(resultado)

# nombre ="Johana"

# resultado=mi_lista[0:2]
# print(resultado)

# mi_lista2 = ['e','f','g']

# resultado = mi_lista + mi_lista2
# print(resultado)

# mi_lista[0]='alfa'
# print(mi_lista)

# mi_lista.append('z')
# print(mi_lista)

# mi_lista.pop()
# print(mi_lista)

# mi_lista.pop(0)
# print(mi_lista)

# mi_lista=['l','b','i','a']
# mi_lista.sort()
# print(mi_lista)

# mi_lista.reverse()
# print(mi_lista)

medios_trasporte= ['avion', 'auto', 'barco', 'bicicleta']
medios_trasporte.append('motocicleta')
print(medios_trasporte)

frutas = ['manzana', 'banana','mango', 'cereza', 'sandia']
eliminado = frutas.pop(2)
print(eliminado)

nombres = ['Juan', 'Luis', 'Melissa']
print(nombres)
print(nombres[1])
print(nombres[-1])
print(nombres[1:])
nombres[1] = 'Maria'
print(nombres)

print(len(nombres))
nombres.append('Johan')
print(nombres)

nombres.insert(1, 'Laura')
print(nombres)

nombres.remove('Laura')
print(nombres)

nombres.pop()
print(nombres)

del nombres[0]
print(nombres)

nombres.clear()
print(nombres)

del nombres
print(nombres)
