from collections import defaultdict

d = defaultdict(float)  # tipo flotante por defecto
print(d['algo'])
print(d)
defaultdict(float, {'algo': 0.0})
d = defaultdict(str)  # tipo cadena por defecto
d['algo'] = 'otro valor'
print(d['algo'])
print(d)