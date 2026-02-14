n = int(input())
matrix = []
pacman = []
health = 100
stars = 0
immune = False

directions = {
    "down": (1, 0),
    "up": (-1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "P":
            pacman = [row, col]
        elif matrix[row][col] == "*":
            stars += 1

while True:
    direction = input()
    if direction == "end":
        break
    move = directions[direction]
    row = (pacman[0] + move[0]) % n
    col = (pacman[1] + move[1]) % n

    matrix[pacman[0]][pacman[1]] = "-"

    if matrix[row][col] == "*":
        stars -= 1
        matrix[row][col] = "-"
    elif matrix[row][col] == "G":
        if not immune:
            health -= 50
        matrix[row][col] = "-"
        immune = False
    elif matrix[row][col] == "F":
        immune = True
        matrix[row][col] = "-"

    pacman = [row, col]
    matrix[row][col] = "P"

    if health <= 0:
        print(f"Game over! Pacman last coordinates [{','.join(list(str(x) for x in pacman))}]")
        break
    if stars == 0:
        print("Pacman wins! All the stars are collected.")
        break

if health > 0 and stars > 0:
    print("Pacman failed to collect all the stars.")

print(f"Health: {health}")
if stars > 0:
    print(f"Uncollected stars: {stars}")

for row in matrix:
    print("".join(row))
