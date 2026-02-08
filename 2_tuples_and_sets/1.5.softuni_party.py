number_of_guests = int(input())
list_of_guests = set()

for _ in range(number_of_guests):
    reservation_code = input()
    list_of_guests.add(reservation_code)

present_guest = input()
while present_guest != "END":
    list_of_guests.remove(present_guest)
    present_guest = input()

print(len(list_of_guests))
print("\n".join(sorted(list_of_guests)))

