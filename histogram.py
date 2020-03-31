import csv
import os, os.path
import pandas
import numpy as np
from collections import Counter
from matplotlib.ticker import StrMethodFormatter
import matplotlib.pyplot as plt

# 883510, very slow
def count_number_of_file(FOLDER_DIR):
    print(len([name for name in os.listdir(FOLDER_DIR) if os.path.isfile(os.path.join(FOLDER_DIR, name))]))

# fastS
def count_files(in_directory):
    joiner= (in_directory + os.path.sep).__add__
    return sum(
        os.path.isfile(filename)
        for filename
        in map(joiner, os.listdir(in_directory))
    )

# fastest    
def count_em(valid_path):
    x = 0
    for root, dirs, files in os.walk(valid_path):
        for f in files:
            x = x+1
    print("There are", x, "files in this directory.")
    return x


# 1698
def get_max_words_in_txt(valid_path):
    max_length = 0
    for root, dirs, files in os.walk(valid_path):
        for f in files:
            numLines = 0
            numWords = 0
            # Need rb mode to avoid UnicodeDecodeError
            with open(os.path.join(root, f), 'rb') as fo:
                for line in fo:
                    # Let's create a list for words
                    wordsList = line.split()
                    #numLines += 1
                    numWords += len(wordsList)
            max_length_temp = numWords
            if max_length_temp > max_length:
                max_length = max_length_temp
                print(max_length, "-----------------", os.path.join(root, f))
    return max_length

# -----------------------------------------
def get_length_list(valid_path):
    length_list = []
    for root, dirs, files in os.walk(valid_path):
        for f in files:
            numLines = 0
            numWords = 0
            # Need rb mode to avoid UnicodeDecodeError
            with open(os.path.join(root, f), 'r+') as fo:
                for line in fo:
                    # Let's create a list for words
                    wordsList = line.split()
                    #numLines += 1
                    numWords += len(wordsList)
            ''' if numWords == 5:
                print(f) '''
            #print(numWords)
            length_list.append(numWords)
    return length_list


if __name__ == "__main__":
    #count_files("Data")
    #count_em("Data")
    #print(get_max_words_in_txt("Data"))
    #count_number_of_file("Data")



    list = get_length_list("Data")
    #df = pandas.DataFrame._from_arrays(list, 1)
    """ words_counts = Counter(list)
    print(words_counts)
    df = pandas.DataFrame.from_dict(words_counts, orient='index')
    df.to_csv(r'export_dataframe.csv', index=True, header=None)
    df = pandas.read_csv('export_dataframe.csv', names=['length', 'count'])
    print(df)
    df.plot(kind='bar')
    lengths = df['length'].tolist()
    print(lengths)
    count = df['count'].tolist()

    # plt.hist(tr_sent_len, bins=range(min(tr_sent_len), max(tr_sent_len) + 1, 1), 
    #           alpha=0.4, color="red", normed=True) """

    hist, edges = np.histogram(list ,bins=range(1698))
    plt.bar(edges[:-1], hist, width = 0.8, color='#0504aa')
    plt.xlim(min(edges), max(edges))
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Value',fontsize=15)
    plt.ylabel('Frequency',fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.ylabel('Frequency',fontsize=15)
    plt.title('Document Image Histogram',fontsize=15)
    plt.show()

    

