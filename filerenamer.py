import os

file_count = int(input("How many files would you like to rename?"))
file_array = []


for i in range(file_count):
    user_input = input("Enter the file path: ")
    file_array.append(user_input)

def rename_file():
    rename = input("What would you like to rename the files to?")
    for i in range(file_count):
        os.rename(file_array[i], f"{rename}_{i}.txt")

rename_file()

