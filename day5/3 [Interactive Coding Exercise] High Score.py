# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# print(max(student_scores))
# print(min(student_scores))


highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"the highrest score in the class is : {highest_score}")



''' 
Highest Score
UPDATE
We've moved away from repl.it for coding exercises. Check out the new exercises on Coding Rooms with automated submissions.

Login to your Udemy course and head over to the link below to get the sign up link:

Click here

Instructions
You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x

Example Input
78 65 89 86 55 91 64 89
78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

Example Output
The highest score in the class is: 91
The highest score in the class is: 91
e.g. When you hit run, this is what should happen:

https://cdn.fs.teachablecdn.com/DnSPgYNSTgeHRJ3MinHg

Hint
Think about the logic before writing code. How can you compare numbers against each other to see which one is larger?
Test Your Code
Before checking the solution, try copy-pasting your code into this repl:

https://repl.it/@appbrewery/day-5-2-test-your-code

This repl includes my testing code that will check if your code meets this assignment's objectives.

Solution
https://repl.it/@appbrewery/day-5-2-solution
 '''