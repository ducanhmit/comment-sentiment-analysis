import re
import pandas as pd

def remove_urls(string):
    url_pattern = re.compile(r'(http[s]?:\/\/)?[^\s(["<,>]*\.[^\s[",><]*')
    return url_pattern.sub(r'', string)

if __name__ == '__main__':

    df = pd.read_csv("comments_4.csv", encoding='utf-16') # read csv file
    df[u'Content'] = df['Content'].astype(str)
    df[u'Content'] = df[u'Content'].apply(remove_urls)
    df.to_csv('comments_5.csv', encoding='utf-16', header=True, index=False)