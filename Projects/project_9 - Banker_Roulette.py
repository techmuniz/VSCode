
import random
from random import randint

# ๐จ Don't change the code below ๐
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# ๐จ Don't change the code above ๐


#Write your code below this line ๐

# Goal: Whoever's name is print, pays the bill.

# 1ยบ Step - Create a variable with the lenght of the variable with the names
a1 = len(names)

# 2ยบ - Step - Shuffle those numbers
randomchoise = randint(0, a1 -1)

# 3ยบ Step - Create a variable that will use that random number generated before
paying_name = names[randomchoise]

# 4ยบ Step - Print the number of the lucky one
print (f"The lucky one this time is {paying_name}")