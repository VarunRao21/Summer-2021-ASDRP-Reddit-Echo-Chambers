import pandas as pd
import requests
import csv
import re

def getBias(text):
    r = requests.post('https://api.thebipartisanpress.com/api/endpoints/beta/robert', data = {'API':'gAAAAABeVpQJKRM5BqPX91XW2AKfz8pJosk182maAweJcm5ORAkkBFj__d2feG4H5KIeOKFyhUVSY_uGImiaSBCwy2L6nWxx4g==', 'Text':text})
    return r.content


df = pd.read_csv('news_comments.csv')

dataFile = open("newsCommentScores.csv", "w", newline = "")
dataWriter = csv.writer(dataFile)

numLines = 54608
i = 0


#4719
for j in range(0, 4567):

    commentPara = ""
    try:
        while df.loc[i].at["date"] == j:
            commentPara = commentPara + " " + str(df.loc[i].at["comment"])
            i += 1
    except:
        n = 2
    biasStr = str(getBias(commentPara))
    biasRegex = re.compile(r'b\'(.*?)\'')
    biasMo = biasRegex.search(biasStr)
    bias = biasMo.group(1)
    dataWriter.writerow([j, bias])
    print(str(j) + " " + bias)

dataFile.close()
