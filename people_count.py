# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 18:12:54 2021

@author: varun
"""

import pandas as pd
import matplotlib.pyplot as plt


subreddits = ["republicans", "democrats", "liberal", "conservative"]


for s in subreddits:
    people = {"trump":0, 
          "biden":0, 
          "mcconnell":0, 
          "harris":0, 
          "pence":0,  
          "obama":0}
    df = pd.read_csv("C:/Users/varun/Python/Summer-2021-ASDRP-Reddit-Echo-Chambers/" + s + "Titles.csv") 
    for i in range(0, len(df.index)):
        x = df['titles'][i]
        words = x.split()
        for a in words:
            for key in people:
                if a.lower() == key:
                    people[key] += 1

    print(people)
    plt.bar(people.keys(), people.values(), 0.8, color=['r','b'])
    plt.savefig("C:/Users/varun/Python/Summer-2021-ASDRP-Reddit-Echo-Chambers/" + s + "Titles_people.png")
    plt.show()
    
