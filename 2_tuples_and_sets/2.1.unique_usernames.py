username_number = int(input())
unique_usernames = set()

for _ in range(username_number):
    unique_usernames.add(input())

print("\n".join(unique_usernames))