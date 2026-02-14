def even_odd(*args):
    args = list(args)
    command = args.pop()
    filtered_args = []
    if command == "even":
        for number in args:
            if number % 2 == 0:
                filtered_args.append(number)
    else:
        for number in args:
            if number % 2 != 0:
                filtered_args.append(number)

    return filtered_args

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
