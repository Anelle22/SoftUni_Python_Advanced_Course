def classify_books(*args, **kwargs):
    fiction_books = {}
    non_fiction_books = {}

    for item in args:
        if item[0] == "fiction":
            fiction_books[item[1]] = None
        else:
            non_fiction_books[item[1]] = None
    for isbn, title in kwargs.items():
        if title in fiction_books:
            fiction_books[title] = isbn
        elif title in non_fiction_books:
            non_fiction_books[title] = isbn

    output = []

    if fiction_books:
        output.append("Fiction Books:")
        for title, isbn in sorted(fiction_books.items(), key=lambda x: x[1]):
            output.append(f"~~~{isbn}#{title}")

    if non_fiction_books:
        output.append("Non-Fiction Books:")
        for title, isbn in sorted(non_fiction_books.items(), key=lambda x: x[1], reverse=True):
            output.append(f"***{isbn}#{title}")

    return "\n".join(output)

print(classify_books(
    ("fiction", "Brave New World"),
    ("non_fiction", "The Art of War"),
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))
