import random

# my_random_nummber = random.random() * 10
# print(my_random_nummber)

head_tails = random.randint(1, 2)
if head_tails == 1:
    print("heads")
else:
    print("tails")
print(head_tails)