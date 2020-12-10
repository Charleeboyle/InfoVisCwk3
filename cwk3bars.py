import numpy as np
import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt

# initialise dataframe for reading in data, index the first column
df = pd.read_csv('DegreeClassificationData.csv',index_col=0)
chart = ['A','B','C','D','E','F']

# size outer window
plt.figure(figsize = (11,8))
# title doesn't work
# plt.title('Which degree program has the largest cohourt of students obtaining a single degree classification?')

for i in range (1, len(df.columns.values) + 1):
    # grab degreeProgram from data
    degreeProgram = df.columns.values[i-1]
    # create subplot
    plt.subplot(2, 3, i)
    plt.title('Chart: ' + chart[i-1] + '  Degree Program: ' + degreeProgram)
    plt.ylabel("Percentage of students (%)")
    # grab data for degreeProgram & plot
    plt.bar(df.index, df[degreeProgram])

# show overall plot
plt.show()