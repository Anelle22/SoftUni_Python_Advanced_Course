random_string = input().split()
stack = []

while random_string:
    stack.append(random_string.pop())

print(" ".join(stack))