import webbrowser


# Class Movie creates objects in entertainment_center.py
class Movie():
    """ This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # Initialization of variables to display all relavant infomation
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # The function that calls the trailer to be opened in the web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
