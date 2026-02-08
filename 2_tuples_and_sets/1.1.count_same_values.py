numbers = tuple(map(float, input().split()))
nums_and_occurrences = {}

for number in numbers:
    if number not in nums_and_occurrences:
        nums_and_occurrences[number] = 0

    nums_and_occurrences[number] += 1

[print(f"{key} - {value} times") for key, value in nums_and_occurrences.items()]