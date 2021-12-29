import json

# load turn a JSON file to dictionary
file = open("friends.json", "r")
file_contents = json.load(file)
file.close()

#print(file_contents)

for friend in file_contents["friends"]:
    print(friend)


# Writing a dictionary to JSON file

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'},
    {'make': 'Ford', 'model': 'Fusion'}
]

file_write = open("cars.json", "w")
json.dump(cars, file_write, indent=4)
file_write.close

my_json_string = '[{"name": "Alpha Romeo", "released": 1990}]'

string_json = json.loads(my_json_string)

# for deeper understanding the below was printed out
print(type(file_contents))
print(type(my_json_string))
print(type(string_json))
print(type(string_json[0]))