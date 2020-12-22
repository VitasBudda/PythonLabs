import re

def input_words():
    return re.split(', |_|-|!| ', input())

words1, words2 = input_words(), input_words()
new_words = list(filter(lambda w: not w in words1, words2))

print(new_words)