import pandas as pd
from emot.emo_unicode import UNICODE_EMO, EMOTICONS
import re

# comments = pd.read_csv('comments_3.csv', encoding='utf-16')
# print(comments)

# def is_emoji(s):
#     return s in UNICODE_EMOJI

def convert_emojis(text):
    for emot in UNICODE_EMO:
        text = text.replace(emot, "_".join(UNICODE_EMO[emot].replace(",","").replace(":","").split()))
    return text

# Function for converting emoticons into word
def convert_emoticons(text):
    for emot in EMOTICONS:
        text = re.sub(u'('+emot+')', "_".join(EMOTICONS[emot].replace(",","").split()), text)
    return text

    

# Example
text1 = "Hilarious 😂. :) The feeling of making a sale 😎, The feeling of actually fulfilling orders 😒"
text2 = convert_emojis(text1)
print(text2)
text3 = convert_emoticons(text2)
print(text3)