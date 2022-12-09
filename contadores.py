from collections import Counter


l = [1,2,3,4,1,2,3,1,2,1]
animales = "gato perro canario perro canario perro"

print(Counter(l))
print(Counter("palabra"))
c = Counter(animales.split())
print(c)
''' La funcion most_common() devuelve una lista de tuplas con el elemento y su conteo'''
print(c.most_common(1))
print(c.most_common(2))
print(c.most_common())

print(c.items())
print(c.keys())
print(c.values())

print(list(c))
print(dict(c))
print(set(c))
