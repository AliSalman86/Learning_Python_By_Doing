# Ask a user for a list of 3 friends
# for each friend, user will be told wether they are nearby
# for each nearby friend, the friend name will be saved to nearby_friends.txt

# hint: readlines()
user_input = input("Please enter names of 3 nearby friends separated by spaces: ").lower().split()
origin_read_file = open("people.txt", "r")
file_content = origin_read_file.readlines()
origin_read_file.close()
file_content_mod = []

for line in file_content:
    file_content_mod.append(line.rstrip("\n").lower())

print(file_content_mod)

for friend in user_input:
    dest_writing_file = open("nearby_friends.txt", "r")
    file_original_content = dest_writing_file.read()
    dest_writing_file.close()
    if friend in file_content_mod:
        print(f"{friend}, is in the list of people and been added to the nearby friends list!")
        file_writing = open("nearby_friends.txt", "w")
        file_writing.write(file_original_content + friend.title() + "\n")
        file_writing.close()
