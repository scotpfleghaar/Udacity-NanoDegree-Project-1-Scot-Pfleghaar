import media  # Imports the class for the movies bahvior
import fresh_tomatoes  # html and css for the movies to display

# The information for each movie
star_trek = media.Movie("StarTrek",
                        "The brash James T. Kirk tries to live up to his fathe\
                        r's legacy with Mr. Spock keeping him in check as a ve\
                        ngeful Romulan from the future creates black holes to \
                        destroy the Federation one planet at a time.",
                        "http://www.impawards.com/2009/posters/star_trek_xi_ve\
                        r19_xlg.jpg",
                        "https://www.youtube.com/watch?v=SyJszxnJydA")
theShawshankRedemption = media.Movie("The Shawshank Redemption",
                                     "Two imprisoned men bond over a number of\
                                     years, finding solace and eventual redemp\
                                     tion through acts of common decency.",
                                     "https://images-na.ssl-images-amazon.com/\
                                     images/I/51SZp7RhtQL._AC_UL320_SR216,320_\
                                     .jpg",
                                     "https://www.youtube.com/watch?v=6hB3S9bI\
                                     aco")
theGodfather = media.Movie("The Godfather",
                           "The aging patriarch of an organized crime dynasty \
                           transfers control of his clandestine empire to his \
                           reluctant son.",
                           "https://s-media-cache-ak0.pinimg.com/originals/7f/\
                           bf/39/7fbf396b1234209ed0c887b8b932476f.jpg",
                           "https://www.youtube.com/watch?v=sY1S34973zA")
theGodfatherPartII = media.Movie("The Godfather: Part II",
                                 "The early life and career of Vito Corleone i\
                                 n 1920s New York is portrayed while his son, \
                                 Michael, expands and tightens his grip on the\
                                 family crime syndicate.",
                                 "http://www.dvdsreleasedates.com/posters/800/\
                                 T/The-Godfather-Part-II-1974-movie-poster.jpg\
                                 ",
                                 "https://www.youtube.com/watch?v=qJr92K_hKl0")
theDarkKnight = media.Movie("The Dark Knight",
                            "When the menace known as the Joker emerges from h\
                            is mysterious past, he wreaks havoc and chaos on t\
                            he people of Gotham, the Dark Knight must accept o\
                            ne of the greatest psychological and physical test\
                            s of his ability to fight injustice.",
                            "http://www.impawards.com/2008/posters/dark_knight\
                            _ver5_xlg.jpg",
                            "https://www.youtube.com/watch?v=EXeTwQWrcwY")
schindlersList = media.Movie("Schindler's List",
                             "In German-occupied Poland during World War II, O\
                             skar Schindler gradually becomes concerned for hi\
                             s Jewish workforce after witnessing their persecu\
                             tion by the Nazi Germans.",
                             "http://img.moviepostershop.com/schindlers-list-m\
                             ovie-poster-1993-1020189480.jpg",
                             "https://www.youtube.com/watch?v=M5FpB6qDGAE")
# The array that is finally called fresh_tomatoes
movies = [star_trek,
          theShawshankRedemption,
          theGodfather,
          theGodfatherPartII,
          theDarkKnight,
          schindlersList]
# Calling the function that displays the code to the webpage
fresh_tomatoes.open_movies_page(movies)
