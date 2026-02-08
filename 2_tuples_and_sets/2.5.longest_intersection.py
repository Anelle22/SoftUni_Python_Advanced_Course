number_of_lines = int(input())
max_intersection = 0
max_intersection_value = 0
max_intersection_start = 0
max_intersection_end = 0

for i in range(number_of_lines):
    first_range, second_range = input().split("-")
    first_range_start, first_range_end = first_range.split(",")
    second_range_start, second_range_end = second_range.split(",")

    if int(first_range_start) > int(second_range_start):
        intersection_start = int(first_range_start)
    else:
        intersection_start = int(second_range_start)

    if int(first_range_end) < int(second_range_end):
        intersection_end = int(first_range_end)
    else:
        intersection_end = int(second_range_end)

    intersection_value = intersection_end - intersection_start + 1

    if intersection_value > max_intersection:
        max_intersection = intersection_value
        max_intersection_start = intersection_start
        max_intersection_end = intersection_end

final_intersection_list = []

for _ in range(max_intersection_start, max_intersection_end + 1):
    final_intersection_list.append(_)

print(f"Longest intersection is {final_intersection_list} with length {len(final_intersection_list)}")
