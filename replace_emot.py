import pandas as pd
from emot.emo_unicode import UNICODE_EMO, EMOTICONS
import re
import sys

# comments = pd.read_csv('comments_3.csv', encoding='utf-16')
# print(comments)

def convert_emojis(text):
    for emot in UNICODE_EMO:
        text = text.replace(emot, "_".join(UNICODE_EMO[emot].replace(",","").replace(":","").split()))
    return text

# Function for converting emoticons into word
def convert_emoticons(text):
    for emot in EMOTICONS:
        text = re.sub(u'('+emot+')', "_".join(EMOTICONS[emot].replace(",","").split()), text)
    return text

# Function to remove emoji.
def remove_emoji(string):
    # emoji_pattern = re.compile("["
    #                        u"\U0001F600-\U0001F64F"  # emoticons
    #                        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
    #                        u"\U0001F680-\U0001F6FF"  # transport & map symbols
    #                        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
    #                        u"\U00002702-\U000027B0"
    #                        u"\U000024C2-\U0001F251"
    #                        "]+", flags=re.UNICODE)
    emoji_pattern = re.compile("["
                            "\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "\U0001F300-\U0001F5FF"  # symbols & pictographs
                            "\U0001F600-\U0001F64F"  # emoticons
                            "\U0001F680-\U0001F6FF"  # transport & map symbols
                            "\U0001F700-\U0001F77F"  # alchemical symbols
                            "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                            "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                            "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                            "\U0001FA00-\U0001FA6F"  # Chess Symbols
                            "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                            "\U00002702-\U000027B0"  # Dingbats
                            "\U000024C2-\U0001F251" 
                            "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

# Function for removing emoticons
def remove_emoticons(text):
    emoticon_pattern = re.compile(u'(' + u'|'.join(k for k in EMOTICONS) + u')')    # OR
    return emoticon_pattern.sub(r'', text)


# # Example
# text1 = "Hilarious 😂. :) The feeling of making a sale 😎, The feeling of actually fulfilling orders 😒"
# text2 = convert_emojis(text1)
# print(text2)
# text3 = convert_emoticons(text2)
# print(text3)


if __name__ == '__main__':
    text = open(sys.argv[1]).read()
    text = remove_emoji(text)
    print(text)
    print(remove_emoticons("Hello :-)"))

    df = pd.read_csv("comments_3.csv", encoding='utf-16') # read csv file
    df[u'Content'] = df['Content'].astype(str)
    df[u'Content'] = df[u'Content'].apply(remove_emoji)
    df[u'Content'] = df[u'Content'].apply(remove_emoticons)
    df.to_csv('comments_4.csv', encoding='utf-16', header=True, index=False)

