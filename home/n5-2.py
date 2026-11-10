import csv

def top_popular(csv_file, n):
    csv_file.seek(0)
    reader = csv.DictReader(csv_file, delimiter=";")
    top = []

    for data in reader:
        title = data['Book-Title']
        author = data['Book-Author']
        downloads = int(data['Downloads'])

        top.append([downloads, title, author])
        top = sorted(top, key=lambda x: -x[0])
        top = top[:n]

    return top


if __name__ == "__main__":
    with open("books-en.csv") as books_csv:
        n = 20
        res = top_popular(books_csv, n)

        for i in res:
            print(f"{i[2]}. {i[1]} - {i[0]}")