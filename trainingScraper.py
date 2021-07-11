import json
import csv
import pandas as pd
from pandas.io.json import json_normalize
import requests
import re

pd.set_option('display.max_colwidth',None)
query="seo" #Define Your Query
url = f"https://api.pushshift.io/reddit/search/submission/?q={query}"
request = requests.get(url)
json_response = request.json()
json_response

#For getting data from Pushshift API

def get_pushshift_data(data_type, **kwargs):
    """
    Gets data from the pushshift api.
 
    data_type can be 'comment' or 'submission'
    The rest of the args are interpreted as payload.
 
    Read more: https://github.com/pushshift/api
    """
 
    base_url = f"https://api.pushshift.io/reddit/search/{data_type}/"
    payload = kwargs
    request = requests.get(base_url, params=payload)
    return request.json()

dataFile = open("republicansTitles.csv", "w", newline = "")
dataWriter = csv.writer(dataFile)

for j in range(0, 400):

    #Parameters
    
    
    data_type = "submission" #returns submissions
    after = str(j + 1) + "d" #returns results after this date (e.g. after 30 days ago)
    before = str(j) + "d" #returns results before this date (e.g. before 29 days ago)
    sort = "desc" #restrict results based on score (desc puts most upvoted posts first)
    sort_type = "score" #sets sorting to sort by upvotes
    subreddit = "republicans" #sets subreddit to scrape from


    try:
        output = get_pushshift_data(data_type = data_type,
                                    after = after,
                                    before = before,
                                    sort = sort,
                                    sort_type = sort_type,
                                    subreddit = subreddit)
    except:
        print(j)

    
    with open("data.json", "w") as outfile:
        json.dump(output, outfile)

    dataFrame = pd.read_json (r'data.json')
    #print(dataFrame)
    postsPerDay = 5


    for i in range(0,postsPerDay):
        try:
            postInfo = dataFrame.iloc[i, :]
            postStr = pd.Series.to_string(postInfo)
            postStr.encode('unicode_escape')
            titleRegex = re.compile(r'\'title\': \'(.*?)\', \'')
            titleMo = titleRegex.search(postStr)
            title = titleMo.group(1)
            dataWriter.writerow([title])
        except:
            n = 2
    print(j)
            

dataFile.close()
        
        
    
