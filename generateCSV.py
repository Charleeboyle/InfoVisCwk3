import csv
import pandas
from numpy import random

data = []
numDegreePrograms = 6
numRanges = 5
for i in range(numDegreePrograms):
    i = 0
    parameters = [34,29,19,14]
    entry = []
    total = 0
    for parameter in parameters:
        temp = random.randint(parameter)
        total += temp
        entry.append(temp)
    # add final value to make total 100
    entry.append(100-total)
    random.shuffle(entry)
    data.append(entry)
# print(data)

organisedData = []
for i in range(numRanges):
    temp = []
    for j in range(numDegreePrograms):
        temp.append(data[j][i])
    organisedData.append(temp)
# print(organisedData)

with open('RandomData.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Range", "Maths", "English", "Biology", "Economics", "Law", "CS"])
    organisedData[0].insert(0, "<40")
    organisedData[1].insert(0, "40-49")
    organisedData[2].insert(0, "50-50")
    organisedData[3].insert(0, "60-69")
    organisedData[4].insert(0, ">70")
    for i in range(numRanges):
        writer.writerow(organisedData[i])

return pandas.read_csv("RandomData.csv", index_col=0)
print(df)
