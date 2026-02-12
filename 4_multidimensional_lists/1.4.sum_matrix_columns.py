rows, cols = [int(x) for x in input().split(", ")]
matrix = []
sum_of_columns = []

for i in range(rows):
    matrix.append(list((int(x) for x in input().split())))

for i in range(cols):
    sum_of_current_column = 0
    for j in range(rows):
        sum_of_current_column += matrix[j][i]
    sum_of_columns.append(sum_of_current_column)

print("\n".join(str(x) for x in sum_of_columns))

