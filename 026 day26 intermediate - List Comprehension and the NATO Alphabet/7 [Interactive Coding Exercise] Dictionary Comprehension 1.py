sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

#for word in sentence.split():
#    print(word)

# Write your code below:
result = {word:len(word) for word in sentence.split()}

print(result)



#other format

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

split_sentence = sentence.split(" ")

result = {word:len(word) for word in split_sentence}

print(result)

