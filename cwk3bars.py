import numpy as np
import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt
import csv
from numpy import random
def createSubPlots(df, plt):
    # size outer window
    fig = plt.figure(figsize = (11,8))
    # add title
    fig.suptitle('Which degree program has the largest cohourt of students obtaining a single degree classification?')
    # create multiple subplots
    for i in range (1, len(df.columns.values) + 1):
        # grab degreeProgram from data
        degreeProgram = df.columns.values[i-1]
        # create subplot
        plt.subplot(2, 3, i)
        plt.title('Chart ' + str(i) + '  Degree Program: ' + degreeProgram)
        plt.ylim(ymax=99)
        plt.ylabel("Percentage of students (%)")
        # grab data for degreeProgram & plot
        plt.bar(df.index, df[degreeProgram])
    return fig

def generateRandomData():
    data = []
    numDegreePrograms = 6
    numRanges = 5
    # for each degree program, generate 5 random values that sum to 100
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

    # get max value out of all stats
    maxValue = np.amax(data)
    # find the chart in which the max value is contained == correct answer to question
    # + 1 as charts are labelled from 1, not 0
    correctChart = np.where(data == maxValue)[0][0] + 1
    
    # organise data to be in correct format for csv
    organisedData = []
    for i in range(numRanges):
        temp = []
        for j in range(numDegreePrograms):
            temp.append(data[j][i])
        organisedData.append(temp)
    
    return numRanges, organisedData, correctChart

def createCsv(numRanges, organisedData):
    # Generate CSV file with random data
    with open('RandomData.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Range", "Maths", "English", "Biology", "Economics", "Law", "CS"])
        
        # insert ranges at start of data for index column
        organisedData[0].insert(0, "<40")
        organisedData[1].insert(0, "40-49")
        organisedData[2].insert(0, "50-50")
        organisedData[3].insert(0, "60-69")
        organisedData[4].insert(0, ">70")
        
        # construct csv file
        for i in range(numRanges):
            writer.writerow(organisedData[i])

    return pd.read_csv("RandomData.csv", index_col=0)

# run trial n times
n = 3
user_answers = []
correct_answers = []
for i in range(n):
    # generate random data for trial
    numRanges, organisedData, correctChart = generateRandomData()
    # construct csv to be used as data
    df = createCsv(numRanges, organisedData)
    # collect correct answer for trial
    correct_answers.append(correctChart)
    # construct subplots for each degree program
    fig = createSubPlots(df, plt)
    # draw graph
    plt.draw()
    plt.pause(1)
    # collect user answer
    user_answers.append(int(input("Answer: ")))
    plt.close(fig)

print("Your answers were: " + str(user_answers))
print("The correct answers were: " + str(correct_answers))


