import re
import pandas as pd


def urls_csv(df, columns=[]):
    URLPATTERN = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    if columns == []:
        df['urlcount'] = df.apply(lambda x: re.findall(URLPATTERN, x))
    else:
        df['urlcount'] = df[columns].apply(lambda x: re.findall(URLPATTERN, x))
    return df


#print(df.loc[212186,:])
#.str.len()