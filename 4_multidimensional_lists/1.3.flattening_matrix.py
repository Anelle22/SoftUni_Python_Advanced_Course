rows = int(input())
matrix = []

for i in range(rows):
    matrix.append(list(int(x) for x in input().split(", ")))

new_matrix = [num for sublist in matrix for num in sublist]

print(new_matrix)