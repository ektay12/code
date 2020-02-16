import csv
from difflib import get_close_matches
a=[]
wordList = []
string = str(input())
wrd = str(input())

def closeMatches(wordList, wrd): 
     print(get_close_matches(wrd, wordList)) 

with open(string, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        #print(row)
        a.append(row)

arr_len = len(a)
i = 0
while i < arr_len:
    wordList.append(a[i][0])
    #print(i)
    i += 1


closeMatches(wordList, wrd)
