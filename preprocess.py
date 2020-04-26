import re
import enchant
import pandas as pd
#from emot.emo_unicode import EMOTICONS, UNICODE_EMO


def urls_csv(df, columns=[]):
    URLPATTERN = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    if columns == []:
        df['urlcount'] = df.apply(lambda x: re.findall(URLPATTERN, x))
    else:
        df['urlcount'] = df.apply(lambda x: re.findall(URLPATTERN, x) if x.name in ['Content', 'Sentiment'] else x)
    return df
def 


def remove_duplicate_chars(text):
    """ 
    remove cac ky tu keo dai vd: "cai ao nay dep quaaaaaa" : "cai ao nay dep qua 
    """
    text = re.sub(r'([A-Z])\1+', lambda m: m.group(1).lower(), text, flags=re.IGNORECASE)
    return text

def remove_tags(text):
    """
    take string input and clean string without tags.
    use regex to remove the html tags.
def remove_emoji(self, string):
    emoji_pattern = re.compile("["
                        u"\U0001F600-\U0001F64F"  # emoticons
        Converted text to lower case as in, converting "Hello" to "hello" or "HELLO" to "hello".
    """
    text = text.lower()
    return text

def remove_numbers(text):
    """
    take string input and return a clean text without numbers.
    Use regex to discard the numbers.
    """
    output = ''.join(c for c in text if not c.isdigit())
    return output

# https://stackoverflow.com/a/49146722/330558
def remove_emoji(string):
    emoji_pattern = re.compile("["
                        u"\U0001F600-\U0001F64F"  # emoticons
                        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                        u"\U00002702-\U000027B0"
                        u"\U000024C2-\U0001F251"
                        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

# Function for removing emoticons
def remove_emoticons(text):
    emoticon_pattern = re.compile(u'(' + u'|'.join(k for k in EMOTICONS) + u')')
    return emoticon_pattern.sub(r'', text)

# Converting emojis to words
def convert_emojis(text):
    for emot in UNICODE_EMO:
        text = text.replace(emot, "_".join(UNICODE_EMO[emot].replace(",","").replace(":","").split()))
        return text

# Converting emoticons to words    
def convert_emoticons(text):
    for emot in EMOTICONS:
        text = re.sub(u'('+emot+')', "_".join(EMOTICONS[emot].replace(",","").split()), text)
        return text

def check_english_csv(text):
    d = enchant.Dict("en-US")
    return d.check(text)

if __name__ == '__main__':

    a = check_english_csv('test')
    print(a)
    df = pd.read_csv('comments_3.csv', encoding='utf-16')
    print(urls_csv(df))
    

# # Test
# if __name__ == "__main__":
#     util = Preprocess()
#     # Example
#     # Example
#     text1 = "Hilarious 😂. The feeling of making a sale 😎, The feeling of actually fulfilling orders 😒"
#     print(util.convert_emojis(text1))
#     print(emoji.demojize('👋'))

#     # Passing both functions to 'text_rare'
#     # df['text_rare'] = df['text_rare'].apply(convert_emoticons)
#     # df['text_rare'] = df['text_rare'].apply(convert_emojis)

#     # rmv = util.remove_duplicate_chars("cai ao nay dep quaaaaaa")
#     # lower = util.to_lower("Hay song laC quaN")
#     # print(rmv)
#     # print(lower)
#     # str= "Hello :-)"
#     # result = util.remove_emoticons(text=str)
#     # # applying remove_emoticons to 'text_rare'
#     # print(result)
