import csv
import pandas as pd
import numpy as np

# comments = pd.read_csv('comments.csv', encoding='utf-16')
# print(comments)
# # Check how many null values are in a specific column
# print(comments.isnull().sum())
# # Drop all rows that contain null values
# modifiedComments = comments.dropna()
# # Verify that you no longer have any null values by running
# print(modifiedComments.isnull().sum())
# # Drop Index column 
# # modifiedComments.drop(modifiedComments.columns[[0]], axis=1, inplace=True)

# print(modifiedComments.shape)
# #print(modifiedComments)
# i = 1
# for ind in modifiedComments.index:
#     modifiedComments.at[ind, 'Index'] = i
#     i += 1

# print(modifiedComments)

# # Save your modified dataset to a new CSV
# modifiedComments.to_csv('comments_1.csv', encoding='utf-16', header=True, index=False)
# print('Done')
def remove_space(string):
    return " ".join(string.split())

def remove_null_csv(csv_file, dest_file, encoding='utf-16'):
    df = pd.read_csv(csv_file, encoding=encoding)
    # Strip all spaces
    #df['Content'] = df['Content'].astype(str)
    df['Content'] = df['Content'].str.strip()
    # Convert empty to NaN
    nan_value = float("NaN")
    df.replace("", nan_value, inplace=True) # inplace: all changes will be applied to Dataframe itself
    print(df.head)
    # Check how many null values are in a specific column
    print(df.isnull().sum())
    # Drop all rows that contain null values at Content column
    df = df.dropna(subset=['Content'])
    # Verify that you no longer have any null values by running
    print("\nNumber of null object after processing:")
    print(df.isnull().sum())
    # Re-index
    i = 1
    for ind in df.index:
        df.at[ind, 'Index'] = i
        i += 1
    # Save your modified dataset to a new CSV
    df.to_csv(dest_file, encoding='utf-16', header=True, index=False)

if __name__ == '__main__':
    remove_null_csv('../data/comments_5.csv', dest_file='../data/comments_6.csv')