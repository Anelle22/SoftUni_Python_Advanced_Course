number_of_commands = int(input())
parking_garage = set()

for _ in range(number_of_commands):
    command = input().split(", ")
    direction = command[0]
    car_number = command[1]
    if direction == "IN":
        parking_garage.add(car_number)
    else:
        parking_garage.remove(car_number)

if parking_garage:
    print("\n".join(parking_garage))
else:
    print("Parking Lot is Empty")