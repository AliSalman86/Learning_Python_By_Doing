movies_collection = []

app_running = True

while app_running:
    menu = input("""
                Pleaese enter number of desired action, click q to exit the app:
                1 - Add new movie
                2 - List all movies in the collection
                3 - Search for a movie by movie title
                """)
    # if user choose to add a new movie, if the movie title exist then the app notify the user and suggest search instead
    if menu == '1':
        new_movie_title = input("What is the new movie name: ").lower()
        is_exist = next((movie for movie in movies_collection if movie["movie_title"] == new_movie_title), False)
        if not is_exist:
            new_movie_duration = input("What is the movie duration in (hh:mm): ")
            movies_collection.append({
                'movie_title': new_movie_title,
                'movie_duration': new_movie_duration
            })
            #print(movies_collection) for debugging

        else:
            print("This movie already exists! you can enter number 3 to search for the movie instead")
            continue
    # if user choose to list all movies in the selection, if no movies added yet then the app notify the user and suggest start adding movies instead        
    elif menu == '2':
        if len(movies_collection) == 0:
            print("No movies in the collection yet, press 1 to add new movies!")
            continue
        else:
            for i, movie in enumerate(movies_collection):
                print(f'{i}- {movie["movie_title"]} ({movie["movie_duration"]})')
    # if user choose to search for a movie by movie_title, if movie does not exist, user notified and suggest adding the movie instead
    elif menu == '3':
        movie_title = input('Please enter the title of the movie you looking for: ').lower()
        is_exist = next((movie for movie in movies_collection if movie["movie_title"] == movie_title), False)
        print(is_exist)
        if is_exist is False:
            print('The movie that you are looking for does not exist, please check spelling or add the movie to the collection by entering 1!')
        else:
            print(f'{is_exist["movie_title"]} ({is_exist["movie_duration"]})')
    # if user select q then app exit
    elif menu == 'q':
        print("Thank you for using the movie collection app, see you later!")
        app_running = False
    # if none of the listed options selected then user notified of invalid entry and go back to main menu.
    else:
        print("Invalid entry, please try again!")
        continue