import csv
import random

def exract(csv_file, numbers):
    csv_file.seek(0)
    reader = csv.DictReader(csv_file, delimiter=";")
    strings = []
    n = 1
    m = max(nums)
    for i, data in enumerate(reader):
        if i+1 in numbers:
            s = f"{n}) {data['Book-Author']}. {data['Book-Title']} - {data['Year-Of-Publication']} \n"
            n += 1
            strings.append(s)
        if i + 1 > m:
            break
    return strings


if __name__ == "__main__":
    with open("books-en.csv") as books_csv:
        nums = [random.randint(1, 9400) for _ in range(20)]

        strings = exract(books_csv, nums)
        with open('result.txt', 'w') as res:
            for s in strings:
                res.write(s)
