my_file = open("data.txt", "r") # r is the mode of opening the file data.txt, the file will be opened with read only rights

file_content = my_file.read()

my_file.close()
print(file_content)

user_name = input("Enter your name: ")
my_file_writing = open("data.txt", "w")
my_file_writing.write(file_content + "\n" + user_name)

my_file_writing.close()