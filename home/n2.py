import csv

def search_by_author(csv_file, author_in):
    csv_file.seek(0)
    reader = csv.DictReader(csv_file, delimiter=";")

    res = []
    author_in = author_in.strip().replace('.', '').lower()

    for data in reader:
        auth = data['Book-Author'].strip().replace('.', '').lower()
        title = data['Book-Title']

        try:
            release = int(data['Year-Of-Publication'])
        except (ValueError, TypeError):
            continue

        if auth == author_in and 1997 <= release <= 2000:
            res.append([title, release])

    return res


if __name__ == "__main__":
    with open("books-en.csv") as books_csv:
        author = input()
        res = search_by_author(books_csv, author)

        if not res:
            print('Nonn')
        else:
            for i in res:
                print(*i)

#John Grisham