import csv
import statistics

def slice_file(csv_file, start, end):
    csv_file.seek(0)
    #next(csv_file)
    data = []
    for i, line in enumerate(csv_file):
        if i == 0:
            continue
        if i >= start:
            data_entry = line.split(',')
            data.append(data_entry)
        if i >= end:
            break
    return data


def find_popular(csv_file):
    csv_file.seek(0)
    reader = csv.DictReader(csv_file, delimiter=",")
    drinks = [data['coffee_name'] for data in reader]
    res = statistics.mode(drinks)
    # for data in reader:
    #     drink = data["coffee_name"]
    #     drinks[drink] = drinks.get(drink, 0) + 1 
    # res = max(drinks, key=lambda drink_key: drinks[drink_key])
    return res


def temka(csv_file, month_input):
    csv_file.seek(0)
    reader = csv.DictReader(csv_file, delimiter=",")
    income = 0
    for data in reader:
        money = data["money"]
        month = data["Monthsort"]
        if month == month_input:
            income += float(money)
    return round(income, 2)


if __name__ == '__main__':
    START = 1
    END = 5
    with open("Coffe_sales.csv") as coffe_csv:
        # res = slice_file(coffe_csv, START, END)
        # for line in res:
        #     print(' | '.join(res))

        # res = find_popular(coffe_csv)
        # print(res)
        month = input()
        print(temka(coffe_csv, month))