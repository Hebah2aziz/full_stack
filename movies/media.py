import webbrowser
class Movies():#create a class for movies properties
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube_url):
        
      self.title=movie_title
      self.storyline=movie_storyline
      self.poster_image_url=poster_image
      self.trailer_youtube_url=trailer_youtube_url

    def show_trailer(self):#a funtion to show movies trailar
          webbrowser.open(self.trailer_youtube_url)
          




