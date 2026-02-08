command = input().split()
set_one_length = int(command[0])
set_two_length = int(command[1])

original_numbers_set = set()
updated_numbers_set = set()

for _ in range(set_one_length):
    new_number = input()
    original_numbers_set.add(new_number)

for _ in range(set_two_length):
    new_number = input()
    if new_number in original_numbers_set:
        updated_numbers_set.add(new_number)

print("\n".join(updated_numbers_set))