from inspect import stack
stack = []

stack.append('5')
stack.append('6')
stack.append('10')
stack.append('15')
 
print('stack before popped')
print(stack)

print('\n ELEMENT POPPED FROM THE STACK: ')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("stack after popped")
print(stack)

