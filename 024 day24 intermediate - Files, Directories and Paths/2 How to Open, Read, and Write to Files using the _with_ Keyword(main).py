### if the list no exist python create ##

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# w delect all contect in the file and write 
with open("my_file.txt", mode="w") as file:   
    file.write("New text")
    
# # a aapend new element in the list not delect anything
# with open("my_file.txt", mode="a") as file:   
#     file.write("New text")