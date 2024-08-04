# mi_tupla = (1,2,3,4)
# print(type(mi_tupla))

# # t = (5,5.2, 'hola')

# # mi_tupla[0] = 5 no se puede cambiar elementos de una tupla porque son inmutables.

# mi_tupla2 = (1,2,(10,20),4)
# print(mi_tupla2[2][1]) #accedemos para imprimir el numero 20 una tupla dentro de otra tupla

# mi_tupla = list(mi_tupla)
# print(type(mi_tupla))

# mi_tupla = tuple(mi_tupla)
# print(type(mi_tupla))


# t = (1,2,3) # tupla con 3 elementos 1,2,3
# x,y,z = t  # asignamos valor a las vaiables x,y y z

# print(x,y,z)

# print(len(t)) # imprime el valor del tamaño de la tupla t

# t = (1,2,3,1) # admiten valores duplicados

# print(t.count(1)) # cuenta cuantos elementos tienen el valor 1


mi_tupla = (1,2,3,2,3,1,3,2,3,3,1,3,2,2,1,3,2)
print(mi_tupla.count(2))

mi_tupla = (1,2,3,2,3,1,3,2)
mi_lista = list(mi_tupla)
print(type(mi_lista))

mi_tupla = (1,2,3,4)
a,b,c,d = mi_tupla
print(a,b,c,d)