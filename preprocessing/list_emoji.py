import pandas as pd
from emot.emo_unicode import UNICODE_EMO, EMOTICONS

def convert_emojis(text):
    for emot in UNICODE_EMO:
        text = text.replace(emot, "_".join(UNICODE_EMO[emot].replace(",","").replace(":","").split()))
    return text

# Function for converting emoticons into word
def convert_emoticons(text):
    for emot in EMOTICONS:
        text = re.sub(u'('+emot+')', "_".join(EMOTICONS[emot].replace(",","").split()), text)
    return text

comments = pd.read_csv('comments_3.csv', encoding='utf-16')
print(comments)

for ind in comments.index:
    a = convert_emojis(comments.at[ind, 'Content'])
    print(a)
