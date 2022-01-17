# Ask a user for a list of 3 friends
# for each friend, user will be told wether they are nearby
# for each nearby friend, the friend name will be saved to nearby_friends.txt

# hint: readlines()
user_input = input("Please enter names of 3 nearby friends separated by spaces: ").lower().split()
people = open("people.txt", "r")
nearby_people = [line.strip().lower() for line in people.readlines()]
people.close()

print(nearby_people)

for friend in user_input:
    
    if friend in nearby_people:
        # below 3 lines are to copy the exist content and append it to the file when use write() to avoid override the existing content
        dest_writing_file = open("nearby_friends.txt", "r")
        file_original_content = dest_writing_file.read()
        dest_writing_file.close()
        # append the new content to the old content and write it to the new file
        print(f"{friend}, is in the list of people and been added to the nearby friends list!")
        file_writing = open("nearby_friends.txt", "w")
        file_writing.write(file_original_content + friend.title() + "\n")
        file_writing.close()
