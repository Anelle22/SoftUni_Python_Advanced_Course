def summing_set_elements(some_set: set):
    sum_of_set_elements = 0
    for element in some_set:
        sum_of_set_elements += float(element)
    return sum_of_set_elements

number_of_lines = int(input())
asci_sum = 0
odd_set = set()
even_set = set()

for i in range(number_of_lines):
    name = input()
    for character in name:
        character_asci = ord(character)
        asci_sum += character_asci
    asci_sum = asci_sum // (i + 1)
    if asci_sum % 2 == 0:
        even_set.add(asci_sum)
    else:
        odd_set.add(asci_sum)
    asci_sum = 0

odd_set_sum = summing_set_elements(odd_set)
even_set_sum = summing_set_elements(even_set)

if odd_set_sum == even_set_sum:
    result = odd_set | even_set
elif odd_set_sum > even_set_sum:
    result = odd_set - even_set
else:
    result = odd_set ^ even_set

print(", ".join(map(str, result)))






