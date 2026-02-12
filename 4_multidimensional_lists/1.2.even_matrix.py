rows = int(input())
matrix = []
matrix_even_numbers = []

for i in range(rows):
    matrix.append((list(int(x) for x in input().split(", ") if int(x) % 2 == 0)))

print(matrix)