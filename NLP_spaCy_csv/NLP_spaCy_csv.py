# Import libraries:
import pandas as pd
import csv

# Step 01: Load the 4 csv files:
# Creates empty lists for the words and related part-of-speech
wordtype = []
words = []
words_class_type = []

# Creates a functions to load the text information to the dictionary:
def loadtxt(file, wtype):
    with open(file, 'rt', encoding='utf-8') as lines:
        for line in lines:
            line = line.split('|')
            wordtype.append(wtype)
            words.append(line[0])

# Creates a functions to create a csv file:
def csv_writter(filename, fields, rows):
    # writing to csv file
    with open(filename, 'w', newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        
        # writing the fields
        csvwriter.writerow(fields)
        
        # writing the data rows
        csvwriter.writerows(rows)

# Call the 'loadtxt' functions for each of the txt files:
loadtxt('AdjIndex.txt', 'Adj')
loadtxt('AdvIndex.txt', 'Adv')
loadtxt('NounsIndex.txt', 'Noun')
loadtxt('VerbsIndex.txt', 'Verb')

#Step 01: Data entry loop:
while True:
    datafile = input('Enter the name of the data entry file (or "quit" to exit): ')
    filename = 'Lab05_' + datafile + '.csv'
    headers = ['Word', 'Noun', 'Verb', 'Adj', 'Adv', 'Other']
    if datafile == 'quit':
        break
    datafile = datafile + '.txt'
    try:
        with open(datafile, 'rt', encoding='utf-8') as lines:
            file_words = []
            for line in lines:
                line = line.split(' ')
                for i in line:
                    # Code from: https://www.geeksforgeeks.org/python-removing-unwanted-characters-from-string/
                    # Keeps only the alphanumeric characters in each word.
                    i = ''.join(letter for letter in i if letter.isalnum())
                    file_words.append(i)
        
        # Loops through the 'words' and the 'file_words' to find matching values:
        for i in file_words:
            for j in range(len(words)):
                a = words[j]
                if i == a:
                    word_lst = []
                    is_word = ''
                    is_Noun = ''
                    is_Verb = ''
                    is_Adj = ''
                    is_Adv = ''
                    is_Other = ''
                    if wordtype[j] == 'Noun':
                        is_word = i
                        is_Noun = 'X'
                        is_Verb = ''
                        is_Adj = ''
                        is_Adv = ''
                        is_Other = ''
                    elif wordtype[j] == 'Verb':
                        is_word = i
                        is_Noun = ''
                        is_Verb = 'X'
                        is_Adj = ''
                        is_Adv = ''
                        is_Other = ''
                    elif wordtype[j] == 'Adj':
                        is_word = i
                        is_Noun = ''
                        is_Verb = ''
                        is_Adj = 'X'
                        is_Adv = ''
                        is_Other = ''
                    elif wordtype[j] == 'Adv':
                        is_word = i
                        is_Noun = ''
                        is_Verb = ''
                        is_Adj = ''
                        is_Adv = 'X'
                        is_Other = ''
                    else:
                        is_word = i
                        is_Noun = ''
                        is_Verb = ''
                        is_Adj = ''
                        is_Adv = ''
                        is_Other = 'X'
                    word_lst = [is_word, is_Noun, is_Verb, is_Adj, is_Adv, is_Other]
                    words_class_type.append(word_lst)
        
        # Create the 'csv' file:
        csv_writter(filename, headers, words_class_type)
    except:
        print(f'File "{datafile}" not found. Please try again.\n')