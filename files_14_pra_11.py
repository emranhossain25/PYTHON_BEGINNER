from ast import With

import os
oldname='sample3.txt'
newname='rename_file.txt'

with open(oldname,'r') as f:
    content=f.read()
with open(newname,'w') as f:
    f.write(content)

os.remove(oldname)