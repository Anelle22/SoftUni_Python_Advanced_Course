numbers = [int(x) for x in input().split()]
positive_numbers = []
negative_numbers = []

for number in numbers:
    if number > 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)

print(sum(negative_numbers))
print(sum(positive_numbers))
if abs(sum(negative_numbers)) > abs(sum(positive_numbers)):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
