# sets no admiten valores duplicados
#3 maneras de generar un set o conjunto
# mi_set = set([1,2,3,4])
# mi_set = set({1,2,3,4})
# mi_set = set((1,2,3,4))

mi_set2 = {1,2,3,4,5} #manera sencilla de generar un set
print(type(mi_set2))

# mi_set = {1,2,3,4,5,6,1,1,1,1,1} # no se puede generar valores duplicados en un set como el 1
# print(mi_set) # al imprimir solo muestra los valores no duplicados

print(len(mi_set2))

print(2 in mi_set2) # devuelve valor boleano si se encuentra el 2 en el set devuelve true

s1 = {1,2,3}
s2 = {3,4,5}

s3 = s1.union(s2)
print(s3)

s1.add(4)
print(s1)


