from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

points = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
toys = {}

while materials and magic_levels:
    current_magic_level = materials[-1] * magic_levels[0]
    if current_magic_level in points:
        materials.pop()
        magic_levels.popleft()
        new_toy = points[current_magic_level]
        if new_toy not in toys:
            toys[new_toy] = 0
        toys[new_toy] += 1
    elif current_magic_level < 0:
        materials.append(materials.pop() + magic_levels.popleft())
    elif current_magic_level > 0:
        magic_levels.popleft()
        materials[-1] += 15
    else:
        if materials[-1] == 0:
            materials.pop()
        if magic_levels[0] == 0:
            magic_levels.popleft()

if ("Doll" in toys and "Train" in toys) or ("Teddy bear" in toys and "Bicycle" in toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for key, value in sorted(toys.items()):
    print(f"{key}: {value}")

