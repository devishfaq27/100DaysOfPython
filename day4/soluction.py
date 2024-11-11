import random
friends = ["Ifti", "M.Deen", "Niaz", "rasheed"]

# Solution 1
print(random.choice(friends))

# Solution 2
random_choice = random.randint(0,3)
print(friends[random_choice])