import pandas as pd
from emot.emo_unicode import UNICODE_EMO, EMOTICONS
import emot
from collections import Counter

df = pd.read_csv('comments_3.csv', encoding='utf-16')
print(df)

def char_is_emoji(character):
    return character in UNICODE_EMO


def text_has_emoji(text):
    for character in text:
        if character in UNICODE_EMO:
            return True
    return False

list = []

#def list_emoji(text):
    
    


# iterate through each row and select  
# 'Content' column
i = 1
for ind in df.index:
    a = emot.emoji(df['Content'][ind])
    #print(a)
    if a['mean'] != []:
        for i in a['mean']:
            list.append(i)

b = emot.emoji(df['Content'][489704])
print(b)
#print(list)
counter = Counter(list)
print(counter)