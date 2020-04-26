import csv
import pandas as pd

comments = pd.read_csv('comments.csv', encoding='utf-16')
print(comments)
# Check how many null values are in a specific column
print(comments.isnull().sum())
# Drop all rows that contain null values
modifiedComments = comments.dropna()
# Verify that you no longer have any null values by running
print(modifiedComments.isnull().sum())
# Drop Index column 
# modifiedComments.drop(modifiedComments.columns[[0]], axis=1, inplace=True)

print(modifiedComments.shape)
#print(modifiedComments)
i = 1
for ind in modifiedComments.index:
    modifiedComments.at[ind, 'Index'] = i
    i += 1

print(modifiedComments)

# Save your modified dataset to a new CSV
modifiedComments.to_csv('comments_1.csv', encoding='utf-16', header=True, index=False)
print('Done')

def remove_null_csv()