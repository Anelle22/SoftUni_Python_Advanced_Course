n = int(input())
mat = [[int(x) for x in input().split(", ")] for _ in range(n)]

primary_diagonal = [mat[i][i] for i in range(n)]
secondary_diagonal = [mat[i][-1 - i] for i in range(n)]
print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
