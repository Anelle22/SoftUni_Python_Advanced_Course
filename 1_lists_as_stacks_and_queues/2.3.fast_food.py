from collections import deque
quantity_of_food = int(input())
orders = input().split()
order_queue = deque(orders)

biggest_order = int(order_queue[0])
for i in range(len(order_queue)):
    if int(order_queue[i]) > biggest_order:
        biggest_order = int(order_queue[i])

print(biggest_order)

while order_queue and int(order_queue[0]) <= quantity_of_food:
    quantity_of_food -= int(order_queue[0])
    order_queue.popleft()


if not order_queue:
    print("Orders complete")
else:
    print(f'Orders left: {" ".join(order_queue)}')



