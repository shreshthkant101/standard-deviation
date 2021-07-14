import math
import csv

with open("class1.csv") as c1:
    data = csv.reader(c1)

    datalist = list(data)

    datalist.pop(0)


def mean(dl):
    length = len(dl)
    sum = 0
    for i in dl:
        sum += int(i[1])
    
    mean = sum/length
    return mean


meanValue = mean(datalist)

array = []

for j in range(len(datalist)):
    value = int(datalist[j][1])

    diff = value - meanValue

    diff = diff ** 2

    array.append(diff)

sum = 0

for k in array:
    sum += array[j]

res = sum / (len(datalist) - 1)

std = math.sqrt(res)

print(std)
