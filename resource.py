# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 22:43:30 2018

@author: teaca
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from urllib import urlretrieve

def countTrue(data):
    isTrue = 0
    isFalse = 0
    for isT in data:
        if isT == "1":
            isTrue += 1
        else:
            isFalse += 1
            
    return [isTrue, isFalse]






urlretrieve('https://raw.githubusercontent.com/freeCodeCamp/2016-new-coder-survey/master/clean-data/2016-FCC-New-Coders-Survey-Data.csv', "sheet.csv")
df = pd.read_csv('sheet.csv', sep=',', dtype = str)



isSoftTrue = df["IsSoftwareDev"] == "1"
isSoftfalse = df["IsSoftwareDev"] != "1"
softTrueDf = df[isSoftTrue]
softFalseDf = df[isSoftfalse]

topLabels = ["ResourceUdacity", "ResourceEdX", "ResourcePluralSight", "ResourceKhanAcademy", "ResourceUdemy", "ResourceCoursera", "ResourceCodecademy"]
topValuesTrue = []
topValuesFalse = []
for label in topLabels:
    ansT = countTrue(softTrueDf.loc[:,label])
    topValuesTrue.append(ansT[0])
    ansF = countTrue(softFalseDf.loc[:,label])
    topValuesFalse.append(ansF[0])
truePercent = []
falsePercent = []
for i, value in enumerate(topValuesTrue):
    truePercent.append((100*value)/ 4303)
    truePercent[i] = str(truePercent[i]) + "%"
for i, value in enumerate(topValuesFalse):
    falsePercent.append((100*value)/ 11317)
    falsePercent[i] =str(falsePercent[i]) + "%"
    
    
    

topLabels=[s.replace('Resource', '') for s in topLabels]

XTop = np.arange(7)
for i, y in enumerate(topValuesTrue):    
    plt.text(XTop[i] - 0.33, y+100, truePercent[i], color = "blue")
for i , y in enumerate(topValuesFalse):
    plt.text(XTop[i] + 0.125, y+100, falsePercent[i], color = "green")
    
    
plt.bar(XTop + 0.00, topValuesTrue, color = 'b', width = 0.25, label="Software Developer", tick_label = topValuesTrue)
plt.bar(XTop + 0.25, topValuesFalse, color = 'g', width = 0.25, label="not a Software Developer")
plt.title("Top 7 Resources Ordered by if they are a Software Developer")
plt.xlabel("Resource")
plt.ylabel("No. of People")
plt.xticks(XTop + 0.125, topLabels, rotation='vertical')
plt.legend()
plt.show()
plt.close()
