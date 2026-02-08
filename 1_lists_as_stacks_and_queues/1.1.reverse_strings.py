random_string = list(input())
stack = []

for i in range(len(random_string)):
    removed_item = random_string.pop()
    stack.append(removed_item)

print("".join(stack))
