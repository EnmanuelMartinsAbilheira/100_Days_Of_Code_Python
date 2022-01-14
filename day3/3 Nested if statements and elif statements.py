height = int(input("what is yopur height in cm?"))

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("what ios your age"))
    if  age < 12:
        print("you pay 5$")
    elif age <= 18:
        print("please pay 7$")
    else:
        print("please pay 12$")
else:
    print("sorry, you have to grow before you can ride")
