"""
Saves info about films

parameters :
1- movie title
2- movie poster url
3- movie trailer url
"""
class Movie():
	def __init__(alhussiny,movie_title,movie_poster_link,movie_trailer_link):
		alhussiny.title = movie_title
		alhussiny.poster_image_url = movie_poster_link
		alhussiny.trailer_youtube_url = movie_trailer_link
