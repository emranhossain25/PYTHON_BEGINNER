content=True
i=1
with open('log.txt','r') as f:
    while content:
        content=f.readline()
        if 'python' in content.lower():
            print(content)
            print(f" python is present on line number{i}")
        i+=1