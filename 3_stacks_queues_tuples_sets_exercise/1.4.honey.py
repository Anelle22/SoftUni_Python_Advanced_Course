from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(x for x in input().split())
total_honey = 0

operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y !=0 else 0
}

while working_bees and nectar:
    if working_bees[0] <= nectar[-1]:
        honey_made = operators[symbols[0]](working_bees[0], nectar[-1])
        total_honey += abs(honey_made)
        working_bees.popleft()
        nectar.pop()
        symbols.popleft()
    else:
        nectar.pop()

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f'Bees left: {", ".join(str(el) for el in working_bees)}')
if nectar:
    print(f'Nectar left: {", ".join(str(el) for el in nectar)}')