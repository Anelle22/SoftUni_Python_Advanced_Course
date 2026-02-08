box_of_clothes = input().split()
total_rack_capacity = int(input())
stack_of_clothes = []
racks_used = 1

for i in range(len(box_of_clothes)):
    stack_of_clothes.append(box_of_clothes[i])

current_rack_capacity = total_rack_capacity
while stack_of_clothes:
    current_clothing = int(stack_of_clothes.pop())
    if current_clothing <= current_rack_capacity:
        current_rack_capacity -= current_clothing
    else:
        stack_of_clothes.append(current_clothing)
        racks_used += 1
        current_rack_capacity = total_rack_capacity

print(racks_used)






