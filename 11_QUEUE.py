queue=[]

queue.append('10')
queue.append('15')
queue.append('20')
queue.append('25')

print('ELEMENT BEFORE DEQUEUING')
print(queue)

print("\nELEMENT  DEQUEUING ")
print(queue.pop())
print(queue.pop())
print(queue.pop())

print("\n ELEMENT AFTER DEQUEUING")
print(queue)