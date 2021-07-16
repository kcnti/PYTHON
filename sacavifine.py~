#pearl's work


import os

import statsmodels.api as sm
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import pandas as pd
import numpy as np

def prepareData():
    df = sm.datasets.get_rdataset("USArrests").data
    df = pd.DataFrame(df)

    print(df.memory_usage())
prepareData()


df = sm.datasets.get_rdataset("USArrests").data
df=df[["Murder","Assault"]].loc[[
"Pennsylvania",
"Ohio",
"New York",
"West Virginia",
"Virginia",
"Maryland",
"New Jersey",
"Delaware",
"Michigan",
"North Carolina"]]
print(df)
print(df.index.values)
print(df['Murder'].values)
print(df['Assault'].values)

labels = df.index.values
murder = df['Murder'].values
assault = df['Assault'].values


# Barchart
x = np.arange(len(labels)) # the label locations
width = 0.35 # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, murder, width,)
ax.set_xlabel('States')
ax.set_ylabel('arrests (per 100,000)')
ax.set_title('Murder scores')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


fig.tight_layout()

plt.show()


# PieChart
for data in [murder]:
    fig, ax = plt.subplots()
    ax.axis('equal')
    ax.set_title("Murder")
    ax.pie(data, labels = labels,autopct='%1.2f%%')
    plt.show()

for data in [assault]:
    fig, ax = plt.subplots()
    ax.axis('equal')
    ax.set_title("Assault")
    ax.pie(data, labels = labels,autopct='%1.2f%%')
    plt.show()

#Scatter
state_ = ["Pennsylvania",
"Ohio",
"New York",
"West Virginia",
"Virginia",
"Maryland",
"New Jersey",
"Delaware",
"Michigan",
"North Carolina"]
plt.scatter(state_,assault)
plt.scatter(state_,murder)
plt.title('US arrests scatter plot')
plt.xlabel('States')
plt.ylabel('Arrests (per 100,000)')
plt.show()


#Box
plt.boxplot(df["Assault"])
plt.title('US arrests box plot')
plt.xlabel('States')
plt.ylabel('Arrests (per 100,000)')
plt.show()

# Table

def calcStatInfo():
    df = sm.datasets.get_rdataset("USArrests").data
    df = pd.DataFrame(df)

    state = ["Pennsylvania",
    "Ohio",
    "New York",
    "West Virginia",
    "Virginia",
    "Maryland",
    "New Jersey",
    "Delaware",
    "Michigan",
    "North Carolina"]
    
    df = df[df.index.isin(state)]


labels = df.index.values
murder = df['Murder'].values
assault = df['Assault'].values
print("Min of Murder is ", df['Murder'].min())
print("Max of Murder is ", df['Murder'].max())
print("Mean of Murder is ", df['Murder'].mean())
print("Range of Murder is ", df['Murder'].max() - df['Murder'].min())
print("Standard Deviation of Murder is ", df['Murder'].std())
print("Q1 of Murder is ", df['Murder'].quantile(0.25))
print("Q2(Median) of Murder is ", df['Murder'].quantile(0.5))
print("Q3 of Murder is ", df['Murder'].quantile(0.75))
print("Interquatile Range of Murder is ", df['Murder'].quantile(0.75) - df['Murder'].quantile(0.25))
print()
print()
print("Min of Assault is ", df['Assault'].min())
print("Max of Assault is ", df['Assault'].max())
print("Mean of Assault is ", df['Assault'].mean())
print("Range of Assault is ", df['Assault'].max() - df['Assault'].min())
print("Standard Deviation of Assault is ", df['Assault'].std())
print("Q1 of Assault is ", df['Assault'].quantile(0.25))
print("Q2(Median) of Assault is ", df['Assault'].quantile(0.5))
print("Q3 of Assault is ", df['Assault'].quantile(0.75))
print("Interquatile Range of Assault is ", df['Assault'].quantile(0.75) - df['Assault'].quantile(0.25))

print("Min of Murder is ", df['Murder'].min())
print("Max of Murder is ", df['Murder'].max())
print("Mean of Murder is ", df['Murder'].mean())
print("Range of Murder is ", df['Murder'].max() - df['Murder'].min())
print("Standard Deviation of Murder is ", df['Murder'].std())
