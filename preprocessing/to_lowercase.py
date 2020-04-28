import pandas as pd

comments = pd.read_csv('comments_2.csv', encoding='utf-16')
print(comments)

comments['Content'] = comments['Content'].str.lower()
print(comments)

# Save your modified dataset to a new CSV
comments.to_csv('comments_3.csv', encoding='utf-16', header=True, index=False)
print('Done')