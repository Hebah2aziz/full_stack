
import fresh_tomatoes
import media
toystory=media.Movies("toystory","the boy and his toys come a live","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=rNk1Wi8SvNc")
#print(toystory.storyline)
#toystory.show_trailer()

the_lord=media.Movies("the lord of the rings","the story of bravy guy try to save the middel earth",
                      "https://upload.wikimedia.org/wikipedia/en/e/e9/First_Single_Volume_Edition_of_The_Lord_of_the_Rings.gif","https://youtu.be/rCZ3SN65kIs")
#print(the_lord.storyline)
#the_lord.show_trailer()

movies={toystory,the_lord}#create varible and send two movies objects
fresh_tomatoes.open_movies_page(movies)#use fresh_tomato to style web page 

 
