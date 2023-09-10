def add(*args):
    sum = 0
    #print(args)
    for n in args:
        sum += n
    return sum

print(add(3,5,6,2,1,2,1,1))