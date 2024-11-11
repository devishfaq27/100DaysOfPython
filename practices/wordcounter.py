#                              Project: Word Counter

#TODO- Create a function count_words() that:
# Asks the user to type a sentence.
# Splits the sentence into a list of words.
# Returns the number of words in the sentence.
#TODO- Create another function main() that:
#TODO- Calls count_words() to get the word count.
#TODO- Prints the word count result.
#TODO- Add a loop in main() so the program keeps asking for new sentences until the user types "quit".

def count_word():
    sentence = input("type of sentence: ")
    split_sentence = sentence.split()
    # i = 0
    # for _ in split_sentence:
    #     i += 1
    # return i
    return len(split_sentence)

def main():
    while input("do you want to count a number of words in sentence, type yes or no:\n ").lower() == "yes":
        print(f"words in sentence = {count_word()}")

main()

























