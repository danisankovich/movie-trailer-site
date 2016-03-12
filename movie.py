#Class information for movies. 

import webbrowser

# movie class instantiates a movie with title, storyline, poster image, youtube trailer, release date, rating, and genres
class Movie():
    #double underscore indicates special functino/method
    #init takes self as a parameter
    def __init__(self, movie_title, movie_story_line, poster_image, trailer_youtube, release_date, rotten_tomatoes_rating, genre):
        self.title = movie_title
        self.storyline = movie_story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date
        self.rotten_tomatoes_rating = rotten_tomatoes_rating
        self.genre = genre
    def show_trailer(self): #opens trailer specified in self.trailer_youtube_url
        webbrowser.open(self.trailer_youtube_url)
    #constructor: the init function that sets up the construction of a class instance
    
