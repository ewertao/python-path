"""
💪 This is a Difficult Challenge 💪
Instructions
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is **z**."
"""

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")

true_total = t + r + u + e

l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e2 = name1.count("e2") + name2.count("e2")

love_total = l + o + v + e

total_str = str(true_total) + str(love_total)
total_int = int(total_str)

# print(total_int)
# print(type(total_int))

if total_int <= 10 or total_int >= 90:
    print(f"Your score is {total_int}, you go together like coke and mentos.")
elif total_int >= 40 and total_int <= 50:
    print(f"Your score is {total_int}, you are alright together.")
else:
    print(f"Your score is {total_int}.")
