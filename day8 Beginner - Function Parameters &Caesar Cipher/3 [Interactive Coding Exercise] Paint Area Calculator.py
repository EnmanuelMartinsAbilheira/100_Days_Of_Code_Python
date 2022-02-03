''' mi resolucion '''
#Write your code below this line 👇

def paint_calc(height, width, cover):
  number_of_cach = (test_h * test_w) / coverage

  print(round(number_of_cach))


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# 
# 

''' professora '''
#Write your code below this line 👇
import math
def paint_calc(height, width, cover):
  area = (test_h * test_w)
  num_of_cash = math.ceil(area / cover)

  print(round(f"you'll need {num_of_cash} cans of paint. "))


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)




'''  
## Area Calc

# UPDATE
We've moved away from repl.it for coding exercises.
Check out the new exercises on Coding Rooms with automated submissions.

Login to your Udemy course and head over to the link below to get the sign up link:

[Click here](https://www.udemy.com/course/100-days-of-code/learn/lecture/17825914#questions)

# Instructions

You are painting a wall. The instructions on the paint can says that **1 can of paint can cover 5 square meters** of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height ✖️ wall width) ÷ coverage per can. 

e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 ✖️ 4) ÷ 5 

                         = 1.6

But because you can't buy 0.6 of a can of paint, the **result should be rounded up** to **2** cans. 

IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.

# Example Input

```
test_h = 3
```

```
test_w = 9
```

# Example Output

```
You'll need 6 cans of paint.
```

   

# Hint

**1. To round up a number**: 

[https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python](https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python)

2. Make sure you name your function/parameters the same as when it's called on the last line of code. 

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-8-1-test-your-code](https://repl.it/@appbrewery/day-8-1-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 

# Solution

[https://repl.it/@appbrewery/day-8-1-solution](https://repl.it/@appbrewery/day-8-1-solution)
'''