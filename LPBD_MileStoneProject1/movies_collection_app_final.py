selections = """
Hello to our simple movie selection app.
Please enter the number corresponds to the desired action, enter q to exit the app
1- Add a new movie.
2- List all movies in the collection.
3- Search for a movie in the collection.

Your Selection: """
movies = []

# function defined to add movies by appending info to the movies_list list
def new_movie():
    # user input for movie info
    title = input("Please enter the movie title: ").lower()
    director = input(f"Please enter {title}'s director name: ").lower()
    release_year = input(f"{title}'s release date: ")
    # check if the movie title already exist in the list
    is_exist = next((movie for movie in movies if movie["title"] == title and movie["director"] == director and movie["release_year"]), False)
    # if movie new to the list, movie appended to the collection
    if is_exist is False:
        movies.append({
            'title': title,
            'director': director,
            'release_year': release_year
        })
    else:
        print(f"{title} movie already in the list, use search to find the movie info")


# function defined to list all the movies in the collection
def list_movies():
    # if list is empty then no movies added yet, user notified
    if len(movies) == 0:
        print("No movies added yet to the list, consider start adding your favorite movies!")
    else:
        print(f"=========================Your Movies Collection=========================")

        for movie in movies:
            print_movie(movie)

        print(f"============================ end of the list ===========================")


# function defined to search the movies_list by title and return the movie info
def movie_search():
    # if list is empty then no movies added yet, user notified
    if len(movies) == 0:
        print("No movies added yet to the list, consider start adding your favorite movies!")
    else:
        search_title = input("Please enter the movie title you searching for: ").lower()
        # check if the movie title exist in the list
        movie_title = next((movie for movie in movies if movie["title"] == search_title), False)
        # if movie title does not exist -> notify user:
        if movie_title is False:
            print(f"=========================Searching the collection DONE!=========================")
            print(f"The movie title {search_title} does not exist in your movies list, select 1 to add it to the collection!")
        else:
            print(f"=========================Searching the collection DONE!=========================")
            print_movie(movie_title)

def print_movie(movie):
    print(f'Movie title is: {movie["title"]}')
    print(f'Movie director is: {movie["director"]}')
    print(f'Movie release year is: {movie["release_year"]}')

selection_options = {
    '1': new_movie,
    '2': list_movies,
    '3': movie_search
}

def menu():
    selection = input(selections)
    while selection != 'q':
        if selection in selection_options:
            selected_function = selection_options[selection]
            selected_function()

        else:
            print("Invalid Selection!")
        selection = input(selections)
    print("Thanks for using the movie collection app, see you later!")

menu()