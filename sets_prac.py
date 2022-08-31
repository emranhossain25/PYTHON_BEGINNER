#s={18, "18",21}
#print(s)
from audioop import add


s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)
print(len(s))