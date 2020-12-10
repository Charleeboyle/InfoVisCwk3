import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fig = plt.figure(figsize = (13,13))
fig.suptitle('Which degree program has the largest cohourt of students obtaining a single degree classification?')

def add_new_plot(plot, inputs, position, title):    
    plot.subplot(2,3,position)
    plot.pie(inputs, labels=label, startangle=90, autopct='%1.1f%%')
    plot.title(title)
    plot.axis('equal')

# plt.legend(title = "Degree Classification")
label = '<40', '40-49', '50-59', '60-69', '>70'
inputs = [
    ([5,22,28,35,15], 1, 'Chart: A,  Degree Program: French'),
    ([13,10,20,44,10], 2, 'Chart: B,  Degree Program: English'),
    ([10, 25, 25, 30, 10], 3, 'Chart: C,  Degree Program: Maths'),
    ([5,22,28,35,15], 4, 'Chart: D,  Degree Program: Biology'),
    ([13, 10, 20, 44, 10], 5, 'Chart: E,  Degree Program: Geology'),
    ([10, 25, 25, 30, 10], 6, 'Chart: F,  Degree Program: CS')
    ]

for input in inputs:
    add_new_plot(plt, input[0], input[1], input[2])

plt.show()

