number_of_petrol_pumps = int(input())
stack = []
tank = 0
petrol_station_count = 0

for i in range(number_of_petrol_pumps):
    petrol_details = input().split()
    amount_of_petrol = int(petrol_details[0])
    distance_from_petrol_pump = int(petrol_details[1])
    stack.append(amount_of_petrol)
    stack.append(distance_from_petrol_pump)

for i in range(0, len(stack), 2):
    tank = tank + stack[i] - stack[i+1]
    if tank < 0:
        petrol_station_count = (i + 2) / 2
        tank = 0

print(int(petrol_station_count))



