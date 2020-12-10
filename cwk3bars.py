import numpy as np
import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt
import csv
from numpy import random

def createSubPlots(df, trialNum):
    '''
    Create plot with n subplots, n being the number of columns in 
    the dataframe

    Parameters:
        df (TextFileReader) -- the dataframe containing degree 
                               classification data (csv)
        plt (matplotlib.pylot) -- the parent plot in which subplots
                                  are contained
        trialNum (int) -- the current trial number

    Returns:
        fig -- the figure containing the plots
    '''
    # size outer window  & add title
    fig = plt.figure(figsize = (11,8))
    fig.suptitle('Trial ' + str(trialNum) + ' -- Which degree program has the largest cohourt of students obtaining a single degree classification?')
    
    # generate multiple subplots
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

def generateTrialData():
    '''
    Generates set of random degree classification data for the number
    of degree programs

    Returns:
        numRanges (str) -- the number of ways degree classifications 
                           are split up in the dataset
        organisedData (list) -- random data ready to be fed into the csv
        correctChart (int) -- the chart for the dataset which contains 
                              the correct answer
    '''
    unorganisedData = []
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
        unorganisedData.append(entry)

    # get max value out of all degree classification results 
    maxValue = np.amax(unorganisedData)
    # find the chart that the max value corresponds to (correct trial answer)
    # + 1 as charts are labelled from 1, not 0
    correctChart = np.where(unorganisedData == maxValue)[0][0] + 1
    
    # organise data to be in correct format for csv
    organisedData = []
    for i in range(numRanges):
        temp = []
        for j in range(numDegreePrograms):
            temp.append(unorganisedData[j][i])
        organisedData.append(temp)
    
    return numRanges, organisedData, correctChart

def createCsv(numRanges, organisedData):
    '''
    Constructs a csv file from the organisedData, representing degree 
    classification data for a number of degree programs, split up into 
    ranges.

    Parameters:
        numRanges (str) -- the number of ways degree classifications 
                           are split up in the dataset
        organisedData (list) -- random data ready to be fed into the csv
    
    Returns:
        a dataframe containing the degree classification data (Trial Data)
    '''

    # Generate CSV file with random data
    with open('TrialData.csv', 'w', newline='') as file:
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
    
    return pd.read_csv("TrialData.csv", index_col=0)

# run trial n times
def runBarChartTrials(numTrials):
    '''
    Runs a number of trials (numTrials) for the chart type: bar chart. 
    User is prompted to answer a question via keyboard input.
    Users' response time and answers are collected and stored.
    Correct answers are collected and stored.

    Parameters:
        numTrials (int) -- number of times the trial will run (default 10)
    
    Returns:
        user_answers (list) -- list of user answers (int) for each trial
        correct_answers (list) -- list of correct answers (int) for each trial
    '''
    user_answers = []
    correct_answers = []
    for i in range(numTrials):
        # generate random data for trial
        numRanges, organisedData, correctChart = generateTrialData()
        # construct csv to be used as data
        df = createCsv(numRanges, organisedData)
        # collect correct answer for trial
        correct_answers.append(correctChart)
        # construct subplots for each degree program
        fig = createSubPlots(df, i)
        # draw graph
        plt.draw()
        plt.pause(1)
        # collect user answer
        user_answers.append(int(input("Answer: ")))
        plt.close(fig)
    return user_answers, correct_answers

if __name__ == "__main__":
    user_answers, correct_answers = runBarChartTrials(3)
    print("Your answers were: " + str(user_answers))
    print("The correct answers were: " + str(correct_answers))