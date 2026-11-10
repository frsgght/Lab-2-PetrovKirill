coffe_csv = open("Coffe_sales.csv")
data = coffe_csv.readline()

print(type(data))
print(data)

for line in coffe_csv:
    print(line)

coffe_csv.close()

with open('Coffe_sales.csv') as coffe_csv:
    for line in coffe_csv:
        print(line)