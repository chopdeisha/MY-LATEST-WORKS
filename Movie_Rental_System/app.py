from movie import Movie
from user import User

#user = User("Isha")


#user.add_movie("Harry Potter", "Fantasy")
#user.add_movie("Iron Man", "Sci-Fi")

#User.save_to_file()
user = User.load_from_file('Isha')
print(user.movies)