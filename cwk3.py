import numpy as np
import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt
import csv
from numpy import random
import time
import sys

def createBarChartSubPlots(df, trialNum):
    '''
    Create plot with n bar chart subplots, n being the number of 
    columns in the dataframe

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
    fig.suptitle('[Trial ' + str(trialNum + 1) + '] - Which degree program has the largest cohourt of students obtaining a single degree classification?',fontweight='bold')
    
    # generate multiple subplots
    for i in range (1, len(df.columns.values) + 1):
        # grab degreeProgram from data
        degreeProgram = df.columns.values[i-1]
        # create subplot
        plt.subplot(2, 3, i)
        plt.title('[Chart: ' + str(i) + '],  Degree Program: ' + degreeProgram)
        plt.ylim(ymax=99)
        plt.ylabel("Percentage of students (%)")
        # grab data for degreeProgram & plot
        plt.bar(df.index, df[degreeProgram])
        plt.tight_layout()
    return fig

def createPieChartSubPlots(df, trialNum):
    '''
    Create plot with n pie chart subplots, n being the number of 
    columns in the dataframe

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
    fig.suptitle('[Trial ' + str(trialNum + 1) + '] - Which degree program has the largest cohourt of students obtaining a single degree classification?',fontweight='bold')
    
    # generate multiple subplots
    for i in range (1, len(df.columns.values) + 1):
        # grab degreeProgram from data
        degreeProgram = df.columns.values[i-1]
        # create subplot
        plt.subplot(2,3,i)
        plt.title('[Chart: ' + str(i) + '],  Degree Program: ' + degreeProgram)
        plt.axis('equal')
        plt.pie(df[degreeProgram], labels=df.index, startangle=90, autopct='%1.1f%%', explode=(0.025,0.025,0.025,0.025,0.025))
        plt.tight_layout()

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
            temp = random.randint(4,parameter)
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

def createResultDataCsv(user, correct, response_times, chartType, numTrials):
    '''
    Constructs a csv file from the participants trial results, organised into Bar
    and Pie chart segments

    Parameters:
        user (list) -- The participants answers to each trial
        correct (list) -- The correct answeres for each trial
        response_times(list) -- The participants response times to answer each trial
        chartType (string) -- bar or pie charts
    '''

    # Generate CSV file with random data
    with open(chartType + '_TrialResults.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([chartType])
        
        # construct csv file
        writer.writerow(user)
        writer.writerow(correct)
        writer.writerow(response_times)

def createTrialDataCsv(numRanges, organisedData):
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
        writer.writerow(["Range", "Maths", "English", "Biology", \
            "Economics", "Law", "CS"])
        
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

def runChartTrials(numTrials, chartType):
    '''
    Runs a number of trials (numTrials) for the chart type: bar chart. 
    User is prompted to answer a question via keyboard input.
    Users' response time and answers are collected and stored.
    Correct answers are collected and stored.

    Parameters:
        numTrials (int) -- number of times the trial will run (default 10)
        chartType (string) -- bar or pie charts

    Returns:
        user_answers (list) -- list of user answers (int) for each trial
        correct_answers (list) -- list of correct answers (int) for each trial
        response_times (list) -- list of seconds (float) that it took for the 
                                 user to answer each trial question
    '''
    user_answers = []
    correct_answers = []
    response_times = []
    for i in range(numTrials):
        # generate random data for trial
        numRanges, organisedData, correctChart = generateTrialData()
        # construct csv to be used as data
        df = createTrialDataCsv(numRanges, organisedData)
        # collect correct answer for trial
        correct_answers.append(correctChart)
        
        # construct subplots for each degree program
        if chartType == "bar":
            fig = createBarChartSubPlots(df, i)
        else:
            fig = createPieChartSubPlots(df, i)

        # draw graph
        plt.draw()
        # record start time from when the user see's the graph
        start_time = time.time()
        plt.pause(0.5)
        # collect user answer
        user_answers.append(int(input("Answer: ")))
        # calculate response time of user for current trial
        response_times.append(time.time() - start_time)
        plt.close(fig)

        # wait 1s as requested
        time.sleep(1)
    
    # generate csv to show results of experiment for current participant
    createResultDataCsv(user_answers, correct_answers, response_times, chartType, numTrials)

    return user_answers, correct_answers, response_times

def calculateResults(n, user, correct):
    '''
    Calculates the number of times the user answered correctly.

    Parameters:
        n (int) -- the number of trials
        user (list) -- list of the user answers
        correct (list) -- list of the correct answers
    
    Returns:
        numCorrect (int) -- the number of times the user answered correct.
    '''
    numCorrect = 0
    for i in range(n):
        # if the values at index i are the same
        if user[i] == correct[i]:
            numCorrect +=1
    
    return numCorrect

if __name__ == "__main__":
    # take numTrials as argument
    numTrials = int(sys.argv[1])

    """
    run bar chart trials, and return results to std.out
    """
    print("Running bar chart trials")
    user_answers, correct_answers, response_times = runChartTrials(numTrials, "bar")
    # return results
    print("\nYour answers were: " + str(user_answers))
    print("The correct answers were: " + str(correct_answers))
    print("Your response times: " + str(response_times))
    numCorrect = calculateResults(numTrials, user_answers, correct_answers)
    print("You got " + str(numCorrect) + "/"+ str(numTrials) + " answers correct.")

    '''
    run pie chart trials, and return results to std.out
    '''
    print("\nRunning pie chart trials")
    user_answers, correct_answers, response_times = runChartTrials(numTrials, "pie")
    # return results
    print("\nYour answers were: " + str(user_answers))
    print("The correct answers were: " + str(correct_answers))
    print("Your response times: " + str(response_times))
    numCorrect = calculateResults(numTrials, user_answers, correct_answers)
    print("You got " + str(numCorrect) + "/"+ str(numTrials) + " answers correct.")