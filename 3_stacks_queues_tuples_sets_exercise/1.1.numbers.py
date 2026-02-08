sequence_one = set(map(int, input().split()))
sequence_two = set(map(int, input().split()))

number_of_lines = int(input())

for i in range(number_of_lines):
    command = input().split()
    action = command[0]

    if action == "Add":
        sequence = command[1]
        numbers = list(map(int, command[2:]))
        if sequence == "First":
            sequence_one.update(numbers)
        elif sequence == "Second":
            sequence_two.update(numbers)

    elif action == "Remove":
        sequence = command[1]
        numbers = list(map(int, command[2:]))
        if sequence == "First":
            for item in numbers:
                if item in sequence_one:
                    sequence_one.remove(item)
        elif sequence == "Second":
            for item in numbers:
                if item in sequence_two:
                    sequence_two.remove(item)

    elif action == "Check":
        if sequence_one <= sequence_two or sequence_two <= sequence_one:
            print("True")
        else:
            print("False")

print(", ".join(map(str, sorted(sequence_one))))
print(", ".join(map(str, sorted(sequence_two))))

