"""

Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x weeks left.

"""
age = input()
(years_left) = 90 - int(age)
weeks_left = int(years_left*52)
print(f"You have {weeks_left} weeks left.")