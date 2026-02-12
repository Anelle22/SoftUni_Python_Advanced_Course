rows = int(input())
matrix = []


for i in range(rows):
    line = str(input())
    matrix.append(list(ch for ch in line))

given_symbol = input()
symbol_occurrence = []

for i in range(rows):
    for j in range(rows):
        if matrix[i][j] == given_symbol:
            symbol_occurrence.append(str(i))
            symbol_occurrence.append(str(j))
            break

if symbol_occurrence:
    print(f"({', '.join(symbol_occurrence)})")
else:
    print(f"{given_symbol} does not occur in the matrix")
