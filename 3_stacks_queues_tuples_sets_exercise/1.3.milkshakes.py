from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milk_cups = deque(int(x) for x in input().split(", "))

milkshakes_count = 0

while milkshakes_count < 5 and chocolates and milk_cups:
    if chocolates[-1] <= 0 and milk_cups[0] <= 0:
        chocolates.pop()
        milk_cups.popleft()
        continue
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if milk_cups[0] <= 0:
        milk_cups.popleft()
        continue

    if chocolates[-1] == milk_cups[0]:
        milkshakes_count += 1
        chocolates.pop()
        milk_cups.popleft()
    else:
        milk_cups.rotate(-1)
        chocolates[-1] -= 5

if milkshakes_count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(el) for el in chocolates) if chocolates else 'empty'}")
print(f"Milk: {', '.join(str(el) for el in milk_cups) if milk_cups else 'empty'}")

