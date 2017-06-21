import media  # Imports the class for the movies bahvior
import fresh_tomatoes  # html and css for the movies to display

# Star Trek Movie: Title, Storyline, Poster Image, and Movie Trailer
star_trek = media.Movie(
    "StarTrek",
    "The brash James T. Kirk tries to live up to his father's legacy with Mr. \
    Spock keeping him in check as a vengeful Romulan from the future creates b\
    lack holes to destroy the Federation one planet at a time.",
    "http://www.impawards.com/2009/posters/star_trek_xi_ver19_xlg.jpg",
    "https://www.youtube.com/watch?v=SyJszxnJydA")
# The Shawshack Redemption: Title, Storyline, Poster Image, and Movie Trailer
theShawshankRedemption = media.Movie(
    "The Shawshank Redemption",
    "Two imprisoned men bond over a number of years, finding solace and eventu\
    al redemption through acts of common decency.",
    "https://images-na.ssl-images-amazon.com/images/I/51SZp7RhtQL._AC_UL320_SR216,320_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=6hB3S9bIaco")
# The Godfather: Title, Storyline, Poster Image, and Movie Trailer
theGodfather = media.Movie(
    "The Godfather",
    "The aging patriarch of an organized crime dynasty transfers control of hi\
    s clandestine empire to his reluctant son.",
    "https://s-media-cache-ak0.pinimg.com/originals/7f/bf/39/7fbf396b1234209ed0c887b8b932476f.jpg",  # NOQA
    "https://www.youtube.com/watch?v=sY1S34973zA")
# The Godfather Part II: Title, Storyline, Poster Image, and Movie Trailer
theGodfatherPartII = media.Movie(
    "The Godfather: Part II",
    "The early life and career of Vito Corleone in 1920s New York is portrayed\
    while his son, Michael, expands and tightens his grip on the family crime \
    syndicate.",
    "http://www.dvdsreleasedates.com/posters/800/T/The-Godfather-Part-II-1974-movie-poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=qJr92K_hKl0")
# The Dark Knight: Title, Storyline, Poster Image, and Movie Trailer
theDarkKnight = media.Movie(
    "The Dark Knight",
    "When the menace known as the Joker emerges from his mysterious past, he w\
    reaks havoc and chaos on the people of Gotham, the Dark Knight must accept\
    one of the greatest psychological and physical tests of his ability to fig\
    ht injustice.",
    "http://www.impawards.com/2008/posters/dark_knight_ver5_xlg.jpg",
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")
# Schindlers List: Title, Storyline, Poster Image, and Movie Trailer
schindlersList = media.Movie(
    "Schindler's List",
    "In German-occupied Poland during World War II, Oskar Schindler gradually \
    becomes concerned for his Jewish workforce after witnessing their persecut\
    ion by the Nazi Germans.",
    "http://img.moviepostershop.com/schindlers-list-movie-poster-1993-1020189480.jpg",  # NOQA
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
