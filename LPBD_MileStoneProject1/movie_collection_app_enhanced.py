# Global variable holding the prompt message:
menu_message = """
Pleaese enter number of desired action, click q to exit the app:
1 - Add new movie
2 - List all movies in the collection
3 - Search for a movie by movie title
"""
# Global variable holding empty list where movies will be added as dictionaries
movies_list = []

# function defined to add movies by appending info to the movies_list list
def add_movie():
    # user input for movie info
    title = input("Please enter the movie title: ")
    director = input(f"Please enter {title}'s director name: ")
    release_year = input(f"{title}'s release date: ")
    # check if the movie title already exist in the list
    is_exist = next((movie for movie in movies_list if movie["title"] == title and movie["director"] == director), False)
    # if movie new to the list, movie appended to the collection
    if is_exist is False:
        movies_list.append({
            'title': title,
            'director': director,
            'release_year': release_year
        })
    else:
        print(f"{title} movie already in the list, use search to find the movie info")


# function defined to list all the movies in the collection
def list_movies():
    # if list is empty then no movies added yet, user notified
    if len(movies_list) == 0:
        print("No movies added yet to the list, consider start adding your favorite movies!")
    else:
        print(f"=========================Your Movies Collection=========================")
        for i, movie in enumerate(movies_list):
            print(f"{i+1}- {movie['title']} by {movie['director']} released on {movie['release_year']}.")
        print(f"============================ end of the list ===========================")

# function defined to search the movies_list by title and return the movie info
def movie_search():
    # if list is empty then no movies added yet, user notified
    if len(movies_list) == 0:
        print("No movies added yet to the list, consider start adding your favorite movies!")
    else:
        search_title = input("Please enter the movie title you searching for: ")
        # check if the movie title exist in the list
        is_exist = next((movie for movie in movies_list if movie["title"] == search_title), False)
        # if movie title does not exist -> notify user:
        if is_exist is False:
            print(f"=========================Searching the collection DONE!=========================")
            print(f"The movie title {search_title} does not exist in your movies list, select 1 to add it to the collection!")
        else:
            print(f"=========================Searching the collection DONE!=========================")
            print(f"{is_exist['title']} by {is_exist['director']} released on {is_exist['release_year']}")

def menu():
    menu_display = input(menu_message)
    while menu_display != 'q':
        if menu_display == '1':
            add_movie()
        elif menu_display == '2':
            list_movies()
        elif menu_display == '3':
            movie_search()
        else:
            print("Invalid Selection!")
        menu_display = input(menu_message)
    print("Thanks for using the movie collection app, see you later!")

menu()