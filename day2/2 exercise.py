# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)

print(result)



'''
Data Types
Instructions
Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

Example Input
39
39
Example Output
3 + 9 = 12

12
12
e.g. When you hit run, this is what should happen:

https://cdn.fs.teachablecdn.com/iyJTPDDRRJCB1gmdVQMS

Hint
Try to find out the data type of two_digit_number.
Think about what you learnt about subscripting.
Think about type conversion.
Test Your Code
Before checking the solution, try copy-pasting your code into this repl:

https://repl.it/@appbrewery/day-2-1-test-your-code

This repl includes my testing code that will check if your code meets this assignment's objectives.

Solution
https://repl.it/@appbrewery/day-2-1-solution
'''