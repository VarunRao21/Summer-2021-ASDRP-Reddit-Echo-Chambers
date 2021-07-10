# -*- coding: utf-8 -*-

import requests
import pandas as pd

subreddits = ["republicans", "conservative", "democrats", "liberal"] 

for s in subreddits:
    url = f"https://api.pushshift.io/reddit/search/comment/?subreddit={s}&size=500&sort_type=score"
    request = requests.get(url)
    json_data = request.json()
    data = json_data["data"]
    df = pd.DataFrame(data)
    print(df)
    df.to_csv('r_' + s + '_comments.csv')
        
    


    


