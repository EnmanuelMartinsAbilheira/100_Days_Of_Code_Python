programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again."
}

#Retrieving item from dictionary
print(programming_dictionary["Bug"])

#adding new item to dictionary
programming_dictionary["Loop"] = "the action of doing somethiong over and over again"
print(programming_dictionary)

#Create an empty dictionary
empty_dictionary = {}

#wide an existing dicrionary
programming_dictionary = {}
print(programming_dictionary)

#edit an item in a empty_dictionary
programming_dictionary["Bug"] = "a moth in your computer"
print(programming_dictionary)

#Loop through a dictionary
for thing in programming_dictionary:
  print(thing) # automatica mente solo imprimira las llaves

for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key]) # imprimir el valor de la llave correspondiendte 