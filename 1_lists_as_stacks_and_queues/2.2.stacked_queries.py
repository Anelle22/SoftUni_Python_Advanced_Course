number_of_lines = int(input())
stack = []

for i in range(number_of_lines):
    query = input()
    if "1" in query:
        query_as_list = query.split()
        number = query_as_list[1]
        stack.append(number)
    elif query == "2" and stack:
        stack.pop()
    elif query == "3" and stack:
        max_element = int(stack[0])
        for item in stack:
            if int(item) > max_element:
                max_element = int(item)
        print(max_element)
    elif query == "4" and stack:
        min_element = int(stack[0])
        for item in stack:
            if int(item) < min_element:
                min_element = int(item)
        print(min_element)

print(", ".join(reversed(stack)))
