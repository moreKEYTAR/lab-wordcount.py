# # put your code here.
#version 1
# my_file = open("twain.txt")

# dict_word_count = {}

# for line in my_file:
#     word_list = line.strip().split(" ")
#     for word in word_list:
#         if word in dict_word_count:
#             dict_word_count[word] += 1
#         else:
#             dict_word_count[word] = 1


# for word, count in dict_word_count.items():
#     print word, count


# my_file.close()


#version2
# import sys


# def find_wordcount(file_name):
    
#     my_file = open(file_name)

#     dict_word_count = {}

#     for line in my_file:
#         word_list = line.strip().split(" ")
#         for word in word_list:
#             word = word.lower().strip('"').strip(",").strip(".").strip("?")\
#             .strip(":").strip(";").strip("!")
#             dict_word_count[word] = dict_word_count.get(word, 0) + 1


#     for word, count in dict_word_count.items():
#         print word, count


#     my_file.close()

# find_wordcount(sys.argv[1])


import sys
from collections import Counter

counter = Counter()  # makes empty counter dictionary


def find_wordcount(file_name):
    my_file = open(file_name)

    for line in my_file:
        word_list = line.strip().split(" ")
        counter.update(word_list)
    # print counter
        # for word in word_list:
        #     word = word.lower().strip('"').strip(",").strip(".").strip("?")\
        #     .strip(":").strip(";").strip("!")
        #     dict_word_count[word] = dict_word_count.get(word, 0) + 1

    for word, count in counter.items():
        print word, count

    my_file.close()

find_wordcount(sys.argv[1])
