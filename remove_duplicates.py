import csv
import pandas as pd

comments = pd.read_csv('comments_1.csv', encoding='utf-16')
print(comments)

# Drop all rows that duplicate
modifiedComments = comments.drop_duplicates(subset=['Content'])
# Verify that you no longer have any null values by running
print(modifiedComments)
print(modifiedComments.shape)

# Re indexing
i = 1
for ind in modifiedComments.index:
    modifiedComments.at[ind, 'Index'] = i
    i += 1
print(modifiedComments)

# Save your modified dataset to a new CSV
modifiedComments.to_csv('comments_2.csv', encoding='utf-16', header=True, index=False)
print('Done')
