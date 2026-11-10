import csv

def count_longer(csv_file, l):
    csv_file.seek(0)
    reader = csv.DictReader(csv_file, delimiter=";")
    books = set([data['Book-Title'] for data in reader])
    cnt = 0
    for title in books:
        if len(title) > l:
            cnt +=1
    return cnt

if __name__ == "__main__":
    with open("books-en.csv") as books_csv:
        ans1 = count_longer(books_csv, 30)
        print(ans1)

        