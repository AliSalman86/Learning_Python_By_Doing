# file_read = open("data.txt", "r")   #file name, mode and here r is for read only mode
# file_content = file_read.read()
# file_read.close()

# print(file_content)

# file_write = open("data.txt", "w")  #file name, mode and here w is for write mode
# file_write.write(file_content + "\n" + "new content")
# file_write.close()


people_file = open("../people.txt")
people_content = [line.strip() for line in people_file.readlines()]
people_file.close()

print(type(people_content))
print(people_content)