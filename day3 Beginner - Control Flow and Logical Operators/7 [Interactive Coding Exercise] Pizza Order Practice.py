# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni  == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"your final bill is ${bill}")



'''  mi fornma
bill = 0

if size == "S":
    bill += 15
    print(f"Smaill Pizza ${bill}")
    pepperoni = input("Do you want a photo taken? Y or N. ")
    if add_pepperoni == "Y":
        bill += 2
        print(f"pepperoni for small Pizza ${bill}")

if size != "S":

    if size == "M":
        bill += 20
        print(f"Medium Pizza ${bill}")

    if sizwe == "L":
        bill += 25
        print(f"Large Pizza: ${bill}")

    pepperoni = input("Do you want Extra peperoni? Y or N. ")
    if pepperoni == "Y":
        bill += 3
        print(f"")


extra_cheese = input("Do you want Extra cheese? Y or N. ")
if extra_cheese == "Y":
    bill += 1
    print(f"conta final ${bill}")

 '''

# Pizza Order
# UPDATE
# We've moved away from repl.it for coding exercises. Check out the new exercises on Coding Rooms with automated submissions.

# Login to your Udemy course and head over to the link below to get the sign up link:

# Click here

# Instructions
# Congratulations, you've got a job at Python Pizza. Your first job is to bill an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15
# Small Pizza: $15
# Medium Pizza: $20
# Medium Pizza: $20
# Large Pizza: $25
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
# Extra cheese for any size pizza: + $1
# Example Input
# size = "L"
# size = "L"
# add_pepperoni = "Y"
# add_pepperoni = "Y"
# extra_cheese = "N"
# extra_cheese = "N"
# Example Output
# Your final bill is: $28.
# Your final bill is: $28.
# e.g. When you hit run, this is what should happen:

# https://cdn.fs.teachablecdn.com/p1evEkwQxGNR4WlolIb4

# Hint
# Think about what you've learnt about multiple if statements and see if you can reduce the number of lines of code while having the same functionality.
# Test Your Code
# Before checking the solution, try copy-pasting your code into this repl:

# https://repl.it/@appbrewery/day-3-4-test-your-code

# This repl includes my testing code that will check if your code meets this assignment's objectives.

# Solution
# https://repl.it/@appbrewery/day-3-4-solution