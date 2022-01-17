personnel_info = []

csv_data = open("csv_data.txt", "r")
csv_data_lines = [line.strip() for line in csv_data.readlines()]

csv_data.close()

csv_data_lines = csv_data_lines[1:]
#print(csv_data_lines)

for line in csv_data_lines:
    person_data = line.split(",")
    personnel_info.append({
        "name": person_data[0].title(),
        "age": person_data[1],
        "university": person_data[2].title(),
        "degree": person_data[3].capitalize()
    })


print(personnel_info)