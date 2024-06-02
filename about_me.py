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
    def print_student_name_and_id(my_info):
        """Prints sentences containing student name and ID
        Args:
            my_info (dict): Data structure containing information about me
        """
        # Print sentence containing name
        print(f"My full name is {my_info['name']} but you can call me Sir {my_info['name'].split()[0]}")

        # Print sentence containing student ID
        print(f"My student ID is {my_info['stdid']}\n")

    def print_pizza_toppings(my_info):
        """Prints a bullet list of favourite pizza toppings
        Args:
            my_info (dict): Data structure containing information about me
        """
        # TODO: Complete function body per Step 4
        # Print header "My favourite pizza toppings are:"
        print("My favourite pizza toppings are:")

        # Print bullet list of favourite pizza toppings
        for topping in my_info['pizza toppings']:
            print(f"-{topping}")
        print('\n')

    def add_pizza_toppings(my_info, tup):
        """Adds some pizza toppings to the list of favourites
        Args:
            my_info (dict): Data structure containing information about me
            toppings (list): List of pizza toppings
        """
        # Append new pizza toppings to end of list         
        for item in tup:
            my_info['pizza toppings'].append(item)

        # Convert all pizza toppings to lowercase
        my_info['pizza toppings'] = [item.lower() for item in my_info['pizza toppings']]

        # Sort toppings list alphabetically
        my_info['pizza toppings'].sort()

    def add_movie(my_info, movieTitle, movieGenre):
        """Adds a movie to the list of favourites

        Args:
            my_info (dict): Data structure containing information about me
            title (str): Movie title
            genre (str): Movie genre
        """
        # Create dictionary for new movie and add to movie list
        new_item = {
            'title': movieTitle,
            'genre': movieGenre
        }
        my_info['movies'].append(new_item)
    
    def print_movie_genres(my_info):
        """Prints a sentence listing all favourite movie genres

        Args:
            my_info (dict): Data structure containing information about me
        """
        print('I like to watch', end=" ")
        for item in range(len(my_info['movies'])):
            if item < len(my_info['movies']) - 1:
                print(my_info['movies'][item]['genre'], end=", ")
            else:
                print(f"and {my_info['movies'][item]['genre']}", end=" ") 
        print("movies. \n")
    
    def print_movie_titles(my_info):
        """Prints a sentence listing all favourite movie titles

        Args:
            movie_list (list): List of favourite movies
        """
        print("Some of my favourite movies are", end=" ")
        for item in range(len(my_info)):
            if item < len(my_info) - 1:
                print(my_info[item]['title'], end=", ")
            else:
                print(f"and {my_info[item]['title']}", end="!\n") 

    # Step 3: Print student name and ID
    print_student_name_and_id(about_me)

    # Step 4: Print a bullet list of pizza toppings
    print_pizza_toppings(about_me)

    # Step 5: Add pizza toppings to the data structure
    add_pizza_toppings(about_me, ['soylent green', 'racht'])
    print_pizza_toppings(about_me)

    # Step 6: Add another movie to the data structure
    add_movie(about_me, 'the lord of the rings', 'fantasy')

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me)

    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(about_me['movies'])

if __name__ == '__main__':
    main()

