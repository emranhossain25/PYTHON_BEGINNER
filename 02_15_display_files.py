from itertools import count


lines=['EMRAN\n', 'lOVES\n', 'PYTHON\n']

with open('files_15.txt','w') as f:
    f.writelines(lines)

with open('files_15.txt','r') as f:
 line=f.readlines()

count = 0

for l in lines:
    count +=1
    print("l{}: {}".format(count,l.strip()))