import webbrowser


class Movie:
    """This class provides a way to store movie related information"""

    def __init__(self, title, duration, storyline, poster_image,
                 trailer_youtube_url):
        self.title = title
        self.duration = duration
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Opens movie trailer in a webbrowser"""
        webbrowser.open(self.trailer_url)
