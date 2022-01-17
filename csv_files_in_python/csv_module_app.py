import csv

movies = [
    {"name": "The Matrix", "director": "Wachowski"},{"name": "Green Book", "director": "Farrelly"},{"name": "Amadeus", "director": "Forman"}
]

def write_to_file(output):
    with open("file.csv", "w", newline="") as f:
        #writer = csv.writer(f)
        writer = csv.DictWriter(f, fieldnames=["name","director"])
        writer.writeheader()
        #f.write("name,director\n") ->  not needed when using DectWriter to write in the file
        writer.writerows(output)


def read_from_file():
    with open("file.csv", "r") as f:
        reader = csv.DictReader(f)
        for line in reader:
            print(f"Name: {line['name']}\tDirector: {line['director']}")

write_to_file(movies)
read_from_file()