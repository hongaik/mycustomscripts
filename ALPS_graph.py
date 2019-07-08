#This script outputs one graph per .csv file. Each graph consists of a scatter plot of temperature data, with one plot being the control 
#and the other being the student's data.

import pandas as pd
import matplotlib.pyplot as plt
from os import chdir
chdir('c:\\users\\jeryl\\desktop\\alps_data')
from glob import glob

all_df = []
x=glob('*.csv')
print(x)


for file in glob('*.csv'):
    df = pd.read_csv(file, skiprows=7, names=['Time(s)', 'Temp'])
    all_df.append(df)

for df in all_df:
    df['Control'] = all_df[-1]['Temp']

i=0

for df in all_df:
    df.plot.line(x='Time(s)', y=['Temp','Control'])
    plt.title(str(x[i][:-4]))
    plt.savefig(str(x[i][:-4])+'.jpg')
    i += 1

