"""
Description:
 Uses a complex data structure to store information about me.

Usage:
 python about_me.py
"""
def main():
    # Step 2: Create a complex data structure that holds information about me
    about_me = {
        'name': 'Justin Ehlert',
        'stdid': 10075000,
        'pizza toppings' : ["PEPPERONI", "BACON", "MUSHROOMS"],
        'movies': [
            # TODO: Change this to a movie you like
            {
                'title': 'The empire strikes back',
                'genre': 'sci-fi'
            },
            # TODO: Add one more movie
            {
                'title': 'A new hope',
                'genre': 'sci-fi'
            }
        ]
    }
    #Function prints sudent name and ID
    def print_student_name_and_id(info):
        print(f"My full name is {info['name']} but you can call me Sir {info['name'].split()[0]}")
        print(f"My student ID is {info['stdid']}")

    def print_pizza_toppings(info):
        for topping in info['pizza toppings']:
            print(f"-{topping}")

    def add_pizza_toppings(dict, tup):
        for item in tup:
            dict['pizza toppings'].append(item)
        for item in dict['pizza toppings']:
            item = item.lower()
        dict['pizza toppings'].sort()

    def add_movie(info, movieTitle, movieGenre):
        new_item = {
            'title': movieTitle,
            'genre': movieGenre
        }
        info['movies'].append(new_item)
    
    def print_movie_genres(info):
        print('I like to watch', end=" ")
        for item in range(len(info['movies'])):
            if item < len(info['movies']) - 1:
                print(info['movies'][item]['genre'], end=", ")
            else:
                print(f"and {info['movies'][item]['genre']}", end=" ")
        print("movies.")

    # Step 3: Print student name and ID
    print_student_name_and_id(about_me)

    # Step 4: Print a bullet list of pizza toppings
    print_pizza_toppings(about_me)

    # Step 5: Add pizza toppings to the data structure
    add_pizza_toppings(about_me, ['soylent green', 'racht'])
    print_pizza_toppings(about_me)

    # Step 6: Add another movie to the data structure
    # TODO: Change to a movie you like
    add_movie(about_me, 'the lord of the rings', 'fantasy')

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me)

    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(about_me['movies'])

def print_student_name_and_id(my_info):
    """Prints sentences containing student name and ID

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 3
    # Print sentence containing name
    # Print sentence containing student ID
    print()

def print_pizza_toppings(my_info):
    """Prints a bullet list of favourite pizza toppings

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 4
    # Print header "My favourite pizza toppings are:"
    # Print bullet list of favourite pizza toppings
    print()

def add_pizza_toppings(my_info, toppings):
    """Adds some pizza toppings to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        toppings (list): List of pizza toppings
    """
    # TODO: Complete function body per Step 5
    # Append new pizza toppings to end of list 
    # Convert all pizza toppings to lowercase
    # Sort toppings list alphabetically
    return

def add_movie(my_info, title, genre):
    """Adds a movie to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        title (str): Movie title
        genre (str): Movie genre
    """
    # TODO: Complete function body per Step 6
    # Create dictionary for new movie and add to movie list
    return

def print_movie_genres(my_info):
    """Prints a sentence listing all favourite movie genres

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 7
    print()

def print_movie_titles(movie_list):
    """Prints a sentence listing all favourite movie titles

    Args:
        movie_list (list): List of favourite movies
    """
    # TODO: Complete function body per Step 8
    print()

if __name__ == '__main__':
    main()

