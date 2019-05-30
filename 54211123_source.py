# -*- coding: utf-8 -*-
"""
Created on Thu May 30 20:55:15 2019

@author: Chuma
"""

"Q1.1"
import re

sentence = "aaa---: 1 abc"

if re.match(r"^(\+\+\+)(-{2,3})(\:{1})\s[0-9_]+\sabc$",sentence):
    print ("Match")
else:
    print ("No Match")
    
"-------------------------------------------------------------------"

"Q1.2"
import re

sentence4 = "abc"

if re.match(r"[^0-9][a-zA-Z]+",sentence4):
    print ("Match")
else:
    print("Not Match")


sentence1 = "Chuma of life"

if re.match(r"[a-zA-Z]+\s(of)+\s[a-zA-Z]+",sentence1):
    print ("Match")
else:
    print ("No Match")
    
"-----------------------------------------------------------------"

"Q1.4"
f=open("training.txt", "r")
if f.mode == 'r':
    contents = f.readlines()
    count = 0
    for x in contents:
        
        if re.search(r"\w+@[a-zA-Z]+\.[a-zA-Z]+\.?[a-zA-Z]?",x):
            """print ("Match")
            """
            print (x)
            count = count + 1
    
print(count)

f=open("test.txt", "r")
if f.mode == 'r':
    contents = f.readlines()
    count = 0
    for x in contents:
        
        if re.search(r"\w+@[a-zA-Z]+\.[a-zA-Z]+\.?[a-zA-Z]?",x):
            """print ("Match")
            """
            print (x)
            count = count + 1
    
print(count)

"---------------------------------------------------------------------"

"Q3.2"
def edit_distance(string1, string2,ins_cost,del_cost,sub_cost):
    m=len(string1)+1
    n=len(string2)+1

    table = {}
    for i in range(m): table[i,0]=i
    for j in range(n): table[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if string1[i-1] == string2[j-1] else sub_cost
            table[i,j] = min(table[i, j-1]+ins_cost, table[i-1, j]+del_cost, table[i-1, j-1]+cost)
            
    return table[i,j]

print(edit_distance("Connect", "Commute",1,1,2))

"Q3.3"
def chatbot(string1):
    
    if re.match(r"\b[Hh]ello.*",string1):
        name = input("Hello what is your name?")
        greeting_name = input("How are you doing, " + name + "?")
        if re.match(r".*(fine|good|well|great).*",greeting_name):
            print("I am glad you are " + greeting_name)
        else:
            yesno = input("Does that make you feel bad?")
            if(yesno == "yes" or yesno == "Yes" or yesno == "YES"):
                print("I am sorry to hear you are " + greeting_name)
            else:
                print("Well at least that is better")
    else:
        print("Please greet me first with a hello.")
chatbot("Hello")

"Q4.1"
import csv
import nltk
from collections import Counter
fo = open("test2.txt")
fo1 = fo.readlines()
counter_sum = Counter()
for line in fo1:
       tokens = nltk.word_tokenize(line)
       bigrams = list(nltk.bigrams(line.split()))
       bigramsC = Counter(bigrams)
       tokensC = Counter(tokens)
       both_counters = bigramsC + tokensC
       counter_sum += both_counters

with open('unibigrams.csv', 'w', newline='') as csvfile:
    header = sorted(counter_sum, key=lambda x: str(type(x)))
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    for line in fo1:
          tokens = nltk.word_tokenize(line)
          bigrams = list(nltk.bigrams(line.split()))
          bigramsC = Counter(bigrams)
          tokensC = Counter(tokens)
          both_counters = bigramsC + tokensC
          cs = dict(counter_sum)
          bc = dict(both_counters)
          row = {}
          for element in list(cs):
                if element in list(bc):
                  row[element] = bc[element]
                else:
                  row[element] = 0
          writer.writerow(row)

"Q4.2"
def _contents(items, laplace=False):
    counts = {}
    for item in items:
        counts[item] = counts.get(item,0) + 1.0
    for k in counts:
        if laplace:
            counts[k] += 1.0
            counts[k] /= (len(items)+len(counts))
        else:
            counts[k] /= len(items)
    return counts

print(_contents(['Chuma','Dyasi','Bulembu']))