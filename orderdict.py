from collections import OrderedDict

n = OrderedDict()
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'three'

print(n)

n1 = OrderedDict()
n1['uno'] = 'one'
n1['dos'] = 'two'

n2 = OrderedDict()
n2['dos'] = 'two'
n2['uno'] = 'one'

# ¿Tienen los mismos elementos y en el mismo orden?
print(n1 == n2)
False
