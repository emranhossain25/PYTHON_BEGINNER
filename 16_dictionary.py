from ast import operator


import operator
d={1: 2,3: 4,4: 3,2: 1,0: 0}

s=sorted(d.items(),key=operator.itemgetter(1))

print('ascending order : ',s)

s1=dict( sorted(d.items(),key=operator.itemgetter(1),reverse=True))