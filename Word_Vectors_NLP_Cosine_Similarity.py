# Requirement: 
# The purpose of this lab is to create a Python application that accepts individual words 
# from the “FastText100k.txt” file as keyboard entry and displays the 5 words from the file 
# that “closely correlate” to the entered word, based on their cosine similarity calculation. 

import math 

####################################################### 
# Functions reference: INFO6143 Python - Lab #3
# These 3 functions calculate the cosine similarity for any 2 word vectors  
def dot_product(vec_a, vec_b): 
    dot_prod = 0.0; 
    for i in range(len(vec_a)): 
        dot_prod += vec_a[i] * vec_b[i] 
    return dot_prod 

def magnitude(vector): 
    return math.sqrt(dot_product(vector, vector)) 

# The entry point function  
def cosine_similarity(vec_a, vec_b): 
    dot_prod = dot_product(vec_a, vec_b) 
    magnitude_a = magnitude(vec_a) 
    magnitude_b = magnitude(vec_b) 
    return dot_prod / (magnitude_a * magnitude_b)
####################################################### 

# Inputs the word to find the similarities.
word = input('Enter search word: ')

# Create the empty dictionarie that will store the word vectors.
v = {} # Dictionarie to store the words and vectors from 'FastText100K.txt'
dict_cos_sim = {}

with open('FastText100K.txt', 'rt', encoding="utf-8") as lines:
    # Removes the first line of the file.
    rows = lines.readlines()[1:]

    # Loops through the lines and create a dictionarie, where the key is the word and the value
    # is the list of values of the vector.
    for line in rows:
        line = line.strip('\n')
        x = line.find(' ')
        v[line[0:(x)]] = str(line[(x+1)::]).split(' ')

    # Converts the vector from str to float.
    for i in v:
        for j in range(len(v[i])):
            v[i][j] = float(v[i][j])

# Loops through the dictionarie to calculate the cosine similarity
# between the input word and all other words at the dictionarie.

for i in v:
    if i != word:
        cos_sim = cosine_similarity(v[i], v[word])
        dict_cos_sim[cos_sim] = i
    else:
        pass

cos_lst = list(dict_cos_sim.keys())
cos_lst.sort(reverse = True)

for i in range(5):
    print(cos_lst[i], ' ', dict_cos_sim[cos_lst[i]])