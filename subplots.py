import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import pandas as pd

df = pd.read_csv('iris.csv')
df.head(2)
plt.figure(figsize = (8,4))
for i in range (1, 7):
    plt.subplot(2, 3, i)
    plt.tight_layout()
    plt.scatter('SepalLengthCm', 'SepalWidthCm', data = df )
plt.show()