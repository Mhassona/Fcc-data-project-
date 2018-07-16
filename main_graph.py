# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 14:00:25 2018

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

jobLabels = ["Front-End Web Developer", "Mobile Developer",  "Data Scientist / Data Engineer",
             "User Experience Designer", "Back-End Web Developer", "Full-Stack Web Developer",
             "Quality Assurance Engineer", "Product Manager", "DevOps / SysAdmin", "Other/NA"]
jobValues = [0,0,0,0,0,0,0,0,0,0]
for x in df.loc[:, "JobRoleInterest"]:
    if x == "  Front-End Web Developer":
        jobValues[0] += 1
    elif x == "  Mobile Developer":
        jobValues[1] += 1
    elif x == "  Data Scientist / Data Engineer":
        jobValues[2] += 1
    elif x == "  User Experience Designer":
        jobValues[3] += 1
    elif x == "Back-End Web Developer":
        jobValues[4] += 1
    elif x == "Full-Stack Web Developer":
        jobValues[5] += 1
    elif x == "  Quality Assurance Engineer":
        jobValues[6] += 1
    elif x == "  Product Manager":
        jobValues[7] += 1
    elif x == "  DevOps / SysAdmin":
        jobValues[8] += 1
    else:
        jobValues[9] +=1
tupJob = sorted(zip(jobValues, jobLabels))      
jobValues, jobLabels = zip(*tupJob)  



jobLabelsB = jobLabels[:-1]
jobValuesB = jobValues[:-1]
color_list = ["green", "navy", "red", "blue", "gold", "limegreen", "maroon", "slateblue", "orange"]


jobXB = [i for i, _ in enumerate(jobLabelsB)]
barChart = plt.bar(jobXB, jobValuesB, color = "blue")
for i in range (0,9):
    barChart[i].set_color(color_list[i])
    barChart[i].set_label(jobLabelsB[i])

for i, y in enumerate(jobValuesB):    
    plt.text(jobXB[i] - 0.33, y-120, y, color = "white", fontsize = 15)

plt.title("Which one of these roles are you most interested in?", fontsize=20)
plt.legend()
plt.xlabel("Role")
plt.ylabel("No. of People")
plt.xticks(jobXB, "", rotation='vertical')
plt.show()
