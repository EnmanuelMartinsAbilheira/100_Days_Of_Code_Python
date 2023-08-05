import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#get the total number of items in list.

#            modo1
# num_intem = len(names)
# #generate randopm numbers between 0 and last index
# random_choice = random.randint(0, num_intem - 1)
# person_who_will_pay = names[random_choice]

#           modo 2
person_who_will_pay = random.choice(names)

#imprime nombre alatorio
print(person_who_will_pay + "is going to buy the meal today.")


''' 
Who's Paying
UPDATE
We've moved away from repl.it for coding exercises. Check out the new exercises on Coding Rooms with automated submissions.

Login to your Udemy course and head over to the link below to get the sign up link:

Click here

Instructions
You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

Example Input
Angela, Ben, Jenny, Michael, Chloe
Angela, Ben, Jenny, Michael, Chloe
Note: notice that there is a space between the comma and the next name.

Example Output
Michael is going to buy the meal today!
Michael is going to buy the meal today!
Hint
You might need the help of the len() function.
https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list

Remember that Lists start at index 0!
Solution
https://repl.it/@appbrewery/day-4-2-solution
 '''