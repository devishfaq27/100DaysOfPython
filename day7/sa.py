import random
word_list = ["aardvark", "babbon", "camel"]

chose_word = random.choice(word_list)
print(chose_word)

word_length = len(chose_word)
placeholder = ""
for position in range(word_length):
    placeholder += "_"
print(placeholder)
