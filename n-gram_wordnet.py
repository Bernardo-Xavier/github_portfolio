# Requirement #1 – Identify the longest n-gram in the NounsIndex.txt file:
print('Requirement #1:' + '\n')
# Creates empty lists
list = []
indexlist = []
indexlist2 = []
countermax = []

# Open, reads, writes and clores the file "NounsIndex.txt file"
with open('NounsIndex.txt', 'rt') as lines:

    # Loop to exclude the text from the character '|' to the end of each line e re-write the lines.
    for line in lines:
        # Finds the character '|' and stores its position on 'i'.
        i = line.find('|')
        # Replaces the value of 'line' excludent everything from '|' to the end.
        line = line[0:i]
        # Count the number of '_' to define the size of each n-gram word.
        counter = line.count('_') + 1
        countermax.append(counter)
        counterstr = str(counter)
        # Adds the n-gram number into each text.
        line = (counterstr + ' ' + line)
        # Updates 'list' with all elements added its n-gram number.
        list.append(line)
    # Discovers the biggest n-gram number and stores it at 'max', converts to a string and stores it at 'maxstr'
    max = max(countermax)
    maxstr = str(max)
    # Loop to find the first biggest n-gram and print it.
    for j in list:
        if j[0] == maxstr:
            print(j)
            # Exits the if loop after the first True occurance.
            break
print('\n' + 'End of Requirement #1.' + '\n')
# END OF REQUIREMENT #1
###########################################################################################################################################

# Requirement #2 – Identify the index entry from NounsIndex.txt with the largest number of definitions in the NounsData.txt file:

print('Requirement #2:' + '\n')

# Open, reads, writes and clores the file "NounsIndex.txt file"
with open('NounsIndex.txt', 'rt') as lines:

    # Loop to count how many ',' there is in each line.
    for line in lines:
        counter = line.count(',') + 1
        countermax.append(counter)
        list.append(line)
    
    # Sort the list in descending order.
    countermax.sort(reverse = True)
    
    for j in list:
        x = j.count(',') + 1
        #print(x)
        if x == countermax[0]:
            i = j.find('|')
            word = j[0:i]
            index = j[i+1:]
            indexlist = index.split(',')
            for i in indexlist:
                i = i.strip('\n')
                indexlist2.append(i)
            print(str(countermax[0]) + ' ' + word + ' ' + str(indexlist2))

print('\n' + 'End of Requirement #2.')

# END OF REQUIREMENT #2
###########################################################################################################################################

# Requirement #3 – Print out all the definitions for the index entry found in requirement #2:

print('Requirement #3:' + '\n')

with open('NounsData.txt', 'rt') as lines:
    # Loop through all lines of 'NounsData.txt' to lookup to any matches in the list 'indexlist2':
    for line in lines:
        line = line.strip('\n')
        for i in indexlist2:
            if line[0:8] == i:
                print(line)               
print('\n' + 'End of Requirement #3.')

# END OF REQUIREMENT #3
###########################################################################################################################################



