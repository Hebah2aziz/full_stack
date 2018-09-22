import fresh_tomatoes
import media

toystory = media.Movies("toystory",
                        "the boy and his toys come a live",
                        "https://goo.gl/j7nkk9",
                        "https://www.youtube.com/watch?v=rNk1Wi8SvNc")
the_lord = media.Movies("the lord of the rings",
                        "the story of bravy guy try to save the middel earth",
                        "https://goo.gl/VSGgVM",
                        "https://youtu.be/rCZ3SN65kIs")


movies = {toystory, the_lord}  # create varible and send two movies objects
fresh_tomatoes . open_movies_page(movies)  # use fresh_tomato to style webpage
