count_of_lines = int(input())
unique_chemical_elements = set()

for _ in range(count_of_lines):
    unique_chemical_elements.update(input().split())

print("\n".join(unique_chemical_elements))