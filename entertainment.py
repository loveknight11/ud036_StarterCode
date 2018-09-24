import media
import fresh_tomatoes

mazeRunner = media.Movie("Maze Runner:Death Cure",
                         "https://upload.wikimedia.org/wikipedia/en/e/" +
                         "eb/MazeRunnerDeathCureFinalPoster.jpeg",
                         "https://www.youtube.com/watch?v=S_9OSktlm6s")
cloverfield = media.Movie("The Cloverfield Paradox",
                          "https://upload.wikimedia.org/wikipedia/en/e/" +
                          "e5/Cloverfield_paradox_poster.jpg",
                          "https://www.youtube.com/watch?v=8brYvhEg5Aw")
blackPanther = media.Movie("Black Panther",
                           "https://upload.wikimedia.org/wikipedia/en/0/" +
                           "0c/Black_Panther_film_poster.jpg",
                           "https://www.youtube.com/watch?v=dxWvtMOGAhw")
mute = media.Movie("Mute",
                   "https://upload.wikimedia.org/wikipedia/en/8/82/" +
                   "Mute_poster.png",
                   "https://www.youtube.com/watch?v=ma8te7ywEio")
annihilation = media.Movie("Annihilation",
                           "https://upload.wikimedia.org/wikipedia/en/f/f6/" +
                           "Annihilation_%28film%29.png",
                           "https://www.youtube.com/watch?v=89OP78l9oF0")
prospect = media.Movie("Prospect",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/b/" +
                       "b0/Prospect_film_poster.jpg/220px-Prospect_" +
                       "film_poster.jpg",
                       "https://www.youtube.com/watch?v=XBwPVTyKDEY")

# create list of movies to pass to fresh_tomatoes open_movies_page function
moviesList = [mazeRunner, cloverfield, blackPanther, annihilation,
              prospect, mute]
# call fresh_tomatoes open_movies_page function
fresh_tomatoes.open_movies_page(moviesList)
