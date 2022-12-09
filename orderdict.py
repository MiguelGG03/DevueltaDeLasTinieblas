from collections import OrderedDict

n = OrderedDict()
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'three'

print(n)
print('Sin OrderedDict:')

n1 = {}
n1['uno'] = 'one'
n1['dos'] = 'two'

n2 = {}
n2['dos'] = 'two'
n2['uno'] = 'one'

# ¿Tienen los mismos elementos y en el mismo orden?
print(n1)
print(n2)
print(n1 == n2)

print('Con OrderedDict:')

n1 = OrderedDict()
n1['uno'] = 'one'
n1['dos'] = 'two'

n2 = OrderedDict()
n2['dos'] = 'two'
n2['uno'] = 'one'

# ¿Tienen los mismos elementos y en el mismo orden?
print(dict(n1))
print(dict(n2))
print(n1 == n2)
