class Movie():
    """
    Saves info about films

    parameters :
    1- movie title
    2- movie poster url
    3- movie trailer url
    """
    def __init__(self, movie_title, movie_poster_link, movie_trailer_link):
        self.title = movie_title
        self.poster_image_url = movie_poster_link
        self.trailer_youtube_url = movie_trailer_link
