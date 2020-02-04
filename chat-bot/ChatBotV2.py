# ChatBot v1
# By Tejaswi Hegde - 03/02/2020
# Creates random sentences from input chat files.
#          WARNING - MIGHT BE NSFW !!
#          CAN CONTAIN STRONG LANGUAGE

# --------------------------------------------------
# Comments are for V1.
# V1 used 2 word keys
# V2 uses 3 word keys
# --------------------------------------------------

# Uses Markow chains
# No puncuation marks. But each line is meant to be a single sentence
# So add your own puncuation when you are reading

import random

# Graph contaions our virtual graph of nodes linking to each other.
# Key is two consecutive words. The value is a set of possible continuations
# of the sentence.
# openers contains opening sentences to start with - might slow program.
graph = {}
openers = []

file = open("file.txt", 'r')

for line in file.readlines():
    words = line.strip().replace('  ', ' ').split(' ')

    # If length of words > 3, only then add it to openings.
    # Used to make sure we get some good starting sentences.
    # Also prevents one words like 'Yes' or 'No'.
    # and prevents two words like 'Why not?'
    #  -- increase for better starting words but less of them.
    # (Might reduce variety - needs research)

    if len(words) > 4:
        openers.append((words[0], words[1], words[2]))

    # A couple is a tuple of two consecutive words that are used to
    # find the next word in the sentence.

    for i in range(3, len(words)):
        triple = (words[i-3],  words[i-2], words[i-1])

        # If that key is already present add a new possibility of continuation
        # to it. Also if one type of continuation is more common, it gets
        # repeated. When we use a random number to choose a continuation, we
        # have a higher chance of getting a more common/more used continuation.

        v = graph.get(triple)
        if v is not None:
            v.append(words[i])
        else:
            graph[triple] = [words[i]]

file.close()

# DO NOT UNCOMMENT THIS UNLESS YOU KNOW WHAT YOU ARE DOING
# (WHICH YOU PROBABLY DON'T)
# This is used to write the generated graph to a file so that we won't
# have to generate the graphs once again when the program is run,
# but just have to read it in. (Which is not included in this code)
# Just remove the above code to genrate a garph and enter your own code
# to read in the built_graph file which is hosted on my github.
# Saves time if the input set is huge.
"""
with open("built_graph.txt", 'w') as f:
    for key, value in graph.items():
        f.write(str(key)+" : "+str(value) + "\n")
"""

# This is just for generating multiple sentences
# This code generates 50 sentences at a time. Increase this if you want to

for zzz in range(50):
    # First time setup for each sentence
    # Get an opening word
    # (or two words rather, since they are stored as tuples)
    # Print them
    # pp - previous part (the word we ended on)
    # np - next part (the part that is the continuation of the sentence)
    # Note that np is actually the set of all continuations
    # So we generate a random number (num) to select one of the items
    # in the list to display
    # time is a variable used to limit the length of the senteces
    # the max length of sentence = max time + 2
    # (since 2 are already printed at start)

    index = random.randint(0, len(openers)-1)
    print(openers[index][0] + " " + openers[index][1]
          + " " + openers[index][2], end=' ')

    p1 = openers[index][1]
    p2 = openers[index][2]
    lp = graph[openers[index]]
    time = 0

    # Max time is 20 here
    # Increase this (carefully) if you do not want senteces to cut off.
    # Shorter sentences will not be affected as they terminate early
    # and the loop doesn't contiune.
    # So this does not increase the general length of all senteces,
    # (i.e to forcefully make them of a ceratin length) but only allow
    # bigger sentences to render fully. Don't set this too high because
    # there will be cases where the sentence enters a loop of printing a
    # word repeatedly (because of 3 repeating words in the input file) or
    # the sentence takes a very long path to end and might
    # lag the system (which is much less likely than a single word loop)

    while time < 20:
        try:
            num = random.randint(0, len(lp)-1)
            print(lp[num], end=' ')
            # We get the next continuation set
            temp = graph[p1, p2, lp[num]]
            # Get the key for next comparirion in the graph
            p1 = p2
            p2 = lp[num]
            lp = temp
            # We have printed a word
            time += 1
        except KeyError:
            # If we get a KeyError we can exit the loop
            # A KeyError means that the key does not have any continuations
            # of the sentence. So thats the end of it.
            break
    print('\n')
