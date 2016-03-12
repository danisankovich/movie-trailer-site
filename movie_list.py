#run this file to open the web page

import movie #Class construction file for movies
import fresh_tomatoes #html rendering info

#the following 6 movies are instantiated from movie.py
#movie parameters: title, storyline, poster, youtube, release date, rating, genres

harry_potter_one = movie.Movie("Harry Potter and the Sorcerer's Stone",
                               "A sttory of a young boy who discovers a magical secret",
                               "https://upload.wikimedia.org/wikipedia/en/6/6b/Harry_Potter_and_the_Philosopher%27s_Stone_Book_Cover.jpg",
                               "https://www.youtube.com/watch?v=VyHV0BRtdxo",
                               "Nov. 14, 2001",
                               "80%",
                               "Fantasy, Adventure, Magic")

toy_story = movie.Movie('Toy Story',
                        'A story of a boy and his toys',
                        'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc',
                        "Nov. 19, 1995",
                        "100%",
                        "Animation, Comedy")

fellowship = movie.Movie("Lord of the Rings: The Fellowship of the Ring",
                         "An epic tale of most unlikely proportions",
                         "https://upload.wikimedia.org/wikipedia/en/8/87/Ringstrilogyposter.jpg",
                         "https://www.youtube.com/watch?v=V75dMMIW2B4",
                         "Dec. 19, 2001",
                         "97%",
                         "Fantasy, Adventure")

guardians_of_the_galaxy = movie.Movie("The Guardians of the Galaxy",
                                      "A tale of the radest, baddest, actually worst heroes ever",
                                      "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
                                      "https://www.youtube.com/watch?v=B16Bo47KS2g",
                                      "July 21, 2014",
                                      "91%",
                                      "Super Hero, Comedy, Action, Sci-Fi")

empire_strikes_back = movie.Movie("Star Wars Episode V: the Empire Strikes Back",
                                  "The saga continues as luke plans to face his darkest fears",
                                  "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                                  "https://www.youtube.com/watch?v=JNwNXF9Y6kY",
                                  "May 17, 1980",
                                  "94%",
                                  "Sci-Fi, Space Opera")

crazy_stupid_love = movie.Movie("Crazy, Stupid, Love",
                                "A tale of love, loss, and rekindling",
                                "https://upload.wikimedia.org/wikipedia/en/7/78/CrazyStupidLovePoster.jpg",
                                "https://www.youtube.com/watch?v=aDLhjm-0rJQ",
                                "July 29, 2011",
                                "78%",
                                "Rom-Com")

#open_movies_page in fresh tomatoes requires a list
movies = [harry_potter_one, toy_story, fellowship, guardians_of_the_galaxy, empire_strikes_back, crazy_stupid_love]

#this function from fresh tomatoes launches the web page
#print(movie.Movie.VALID_RATINGS)
fresh_tomatoes.open_movies_page(movies)
