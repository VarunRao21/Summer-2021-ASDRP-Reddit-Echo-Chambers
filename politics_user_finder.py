import requests
import pandas as pd

def fix(a):
    y = ""
    c = []
    for x in a:
        if (x == ','):
            c.append(int(y))
            y = ""
        else:
            y += x
    if (len(c) == 0):
        c.append(int(y))
    return c

inp = pd.read_csv("C:/Users/varun/Python/Summer-2021-ASDRP-Reddit-Echo-Chambers/politics_users.csv")
d = {}

for row in inp.iterrows():
    d[row[1][1]] = fix(row[1][2][1:len(row[1][2])-1])


# started on 7/28, so 4700 days before 7/28    
for i in range(3602, 4700):
    print("i = " + str(i))
    url = "https://api.pushshift.io/reddit/search/comment/?subreddit=politics&size=100&sort_type=score&after="+ str(i+1) +"d&before="+ str(i) + "d"
    request = requests.get(url)
    json_data = request.json()
    data = json_data["data"]
    if (data == []):
        continue
    df = pd.DataFrame(data)
    for p in df["author"]:
        if p in d:
            d[p].append(i)
        else:
            d[p] = [i]
    peopleframe = pd.DataFrame(d.items())
    peopleframe.to_csv("C:/Users/varun/Python/Summer-2021-ASDRP-Reddit-Echo-Chambers/politics_users.csv")



