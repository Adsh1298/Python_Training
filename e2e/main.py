import MovieRepo as movieRepo
from Movie import Movie

movieDb = movieRepo.MovieRepository('demo.csv')

def get_movie_details():
    id = int(input('Enter the MovieID:'))
    title = input('Enter the title: ')
    director = input('Enter the Director name: ')
    year = input('Enter the year of release: ')
    movie = Movie(id, title, director, year)
    return movie

add_feature = lambda movie: movieDb.add_movie(movie)

def view_all_feature():
    movies = movieDb.list_movies()
    if not movies:
        print('No movies are available')
    else:
        for m in movies:
            print(m)

update_feature = lambda movie: movieDb.update_movie(movie.id, movie)

def select_feature():
    title = input('Enter the title of the movie to search: ')
    found = movieDb.get_movie_detail(title)
    if not found:
        print('No movie found to display')
    else:
        print(found)


choice = input('Enter the choice [1-4]:')
match choice:
    case '1':
        new_movie = get_movie_details()
        add_feature(new_movie)
    case '2': view_all_feature()
    case '3':
            print('Enter the details of the movie for updating')
            updating_movie = get_movie_details()
            update_feature(updating_movie)
    case '4': select_feature()
    case '_': print('Invalid choice, Please try again')
