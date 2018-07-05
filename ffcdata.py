# -*- coding: utf-8 -*-
"""

@author: Mohamed Hassona
"""
import matplotlib.pyplot as plt
import pandas as pd
from urllib.request import urlretrieve

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


#Are you Currently a software dev pie chart
pieLabels = "Yes", "No"
pieSizes =countTrue(df["IsSoftwareDev"])
pieColors = ['gold', 'yellowgreen']
pieExplode = (0.1, 0)
plt.title('Are you Currently a Software Developer?')
plt.pie(pieSizes, explode=pieExplode, labels=pieLabels, colors=pieColors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()
plt.close()

valueList = []
for i in range(84,110):
    ans = countTrue(df.iloc[:,i])
    valueList.append(ans[0])

nameList = df.columns.values.tolist()
nameList = nameList[84:110]
nameList = [s.replace('Resource', '') for s in nameList]
tupList = sorted(zip(valueList, nameList))
valueList, nameList = zip(*tupList)




#Which learning resources have you found helpful bar chart
x_pos = [i for i, _ in enumerate(nameList)]
plt.bar(x_pos, valueList, color='red')
plt.xlabel("Resource")
plt.ylabel("No. of People")
plt.title("Which Learning Resources have you Found Helpful?")
plt.xticks(x_pos, nameList, rotation='vertical')
plt.show()
plt.close()

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

jobX = [i for i, _ in enumerate(jobLabels)]
#Which one of these roles are you most interested in? with Other/NA data
barChart = plt.bar(jobX, jobValues, color = "blue")
barChart[9].set_color("gray")
barChart[9].set_alpha(0.4)
plt.title("Which one of these roles are you most interested in?")
plt.xlabel("Role")
plt.ylabel("No. of People")
plt.xticks(jobX, jobLabels, rotation='vertical')
plt.show()
plt.close()

jobLabelsB = jobLabels[:-1]
jobValuesB = jobValues[:-1]
#Which one of these roles are you most interested in? without Other/NA data
jobXB = [i for i, _ in enumerate(jobLabelsB)]
barChart = plt.bar(jobXB, jobValuesB, color = "blue")
plt.title("Which one of these roles are you most interested in?")
plt.xlabel("Role")
plt.ylabel("No. of People")
plt.xticks(jobXB, jobLabelsB, rotation='vertical')
plt.show()
plt.close()

    
    

