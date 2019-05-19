import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  
from scipy import stats
import csv

# read flash.dat to a list of lists
datContent = [i.strip('|').split('|') for i in open("dataset.dat").readlines()]

# write it as a new CSV file
with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(datContent)
def your_func(row):
    return row['Sentiments'] / row['Review']



data = pd.read_csv('output.csv')

f2 = pd.to_numeric(data['fluence_2 '], errors='coerce')
f3 = pd.to_numeric(data['fluence_3 '], errors='coerce')

H32 = f3/f2
print(H32)
