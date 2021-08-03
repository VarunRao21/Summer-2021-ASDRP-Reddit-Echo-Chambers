import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('newsCommentScores.csv')

ax1 = df.plot.scatter(x = 'date', y = 'score')

plt.show()

