from collections import deque
water_quantity = int(input())
queue = deque()

while True:
    command = input()
    if command == "Start":
        break
    else:
        queue.append(command)

while True:
    command = input()
    if command == "End":
        print(f"{water_quantity} liters left")
        break
    elif "refill" in command:
        command_as_list = command.split()
        liters = command_as_list[1]
        water_quantity += int(liters)
    else:
        liters = int(command)
        if liters <= water_quantity:
            person_who_got_water = queue.popleft()
            print(f"{person_who_got_water} got water")
            water_quantity -= liters
        else:
            person_no_water = queue.popleft()
            print(f"{person_no_water} must wait")


