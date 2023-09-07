with open("file1.txt") as file1:
    file_1_data = file1.readline()

with open("file2.txt") as file2:
    file_2_data = file2.readline()

#result = [new_item for item in list if test]
result = [int(num) for num in file_1_data if num in file_2_data]

print(result)





##### other result true

def filereader(file):
  """Read file and remove newline tag"""
  with open(file, "r") as file:
    f_read = file.readlines()
    f = [int(i.replace("\n", "")) for i in f_read]
    return f

file1 = filereader("file1.txt")
file2 = filereader("file2.txt")

# find duplicates and save to result
result = [num for num in file1 if num in file2]

# Write your code above 👆

print(result)