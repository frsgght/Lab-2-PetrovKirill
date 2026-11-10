import csv

def pub_list(csv_file):
    reader = csv.DictReader(csv_file, delimiter=";")
    res = set()
    for data in reader:
        res.add(data['Publisher'])
    return res


if __name__ == "__main__":
    with open("books-en.csv") as books_csv:
        publishers = pub_list(books_csv)
        with open("publisher_list.txt", 'w') as res:
            for p in publishers:
                res.write(str(p)+'\n')