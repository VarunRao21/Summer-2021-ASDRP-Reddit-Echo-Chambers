# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 19:20:32 2021

@author: varun
"""

import pandas as pd
from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import multidict as multidict

subreddits = ["republicans", "democrats", "liberal", "conservative"]
remove_words = ["that", "with", "from", "this", "about", "This", "will", "after", "What", "they", "With", "have", "would", "says", "Will", "more", "what", "your", "their", "That", "just", "After", "&amp", "Just", "From", "They", "about", "Against", "against", "like", 'there', 'being', 'back', 'think', 'most', 'More', 'were', 'Have', 'want', 'Should', 'when']

for s in subreddits:
    word_count = {}
    x = {}
    counts = []
    df = pd.read_csv("C:/Users/varun/Python/Summer-2021-ASDRP-Reddit-Echo-Chambers/" + s + "Titles.csv") 
    for i in range(0, len(df.index)):
        x = df['titles'][i]
        words = x.split()
        for a in words:
            if a[0] in '"' or a[0] in "'(":
                b = a[1:]
            else:
                b = a
            if len(b) != 0 and b[len(b) - 1] in ".,?;!'":
                c = b[:len(b)-1]
            else:
                c = b
            if len(c) > 1 and c[len(c) - 2:] == "'s":
                d = c[:len(c)-2]
            else:
                d = c
            if len(d) > 3 and d.lower() not in remove_words:
                if d.lower() in word_count:
                    word_count[d.lower()] += 1.0
                else:
                    word_count[d.lower()] = 1.0
    x = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    arr = []
    for pair in x:
        arr.append(pair)
    realdict = multidict.MultiDict(arr)
    wc = WordCloud(background_color="white",width=2000,height=2000, max_words=200,relative_scaling=0.5,normalize_plurals=True).generate_from_frequencies(realdict)
    wc.to_file("C:/Users/varun/Python/Summer-2021-ASDRP-Reddit-Echo-Chambers/" + s + "Titles_cloud.png")