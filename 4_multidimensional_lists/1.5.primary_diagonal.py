rows = int(input())
matrix = []
sum_of_diagonals = 0

for i in range(rows):
    line = [int(x) for x in input().split()]
    matrix.append(line)

for i in range(rows):
    sum_of_diagonals += matrix[i][i]

print(sum_of_diagonals)