import media
import fresh_tomatoes


star_trek = media.Movie("StarTrek", "The brash James T. Kirk tries to live up to his father's legacy with Mr. Spock keeping him in check as a vengeful Romulan from the future creates black holes to destroy the Federation one planet at a time.", "http://www.impawards.com/2009/posters/star_trek_xi_ver19_xlg.jpg", "https://www.youtube.com/watch?v=SyJszxnJydA")
theShawshankRedemption = media.Movie("The Shawshank Redemption", "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.", "https://images-na.ssl-images-amazon.com/images/I/51SZp7RhtQL._AC_UL320_SR216,320_.jpg", "https://www.youtube.com/watch?v=6hB3S9bIaco")
theGodfather = media.Movie("The Godfather", "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.", "https://s-media-cache-ak0.pinimg.com/originals/7f/bf/39/7fbf396b1234209ed0c887b8b932476f.jpg", "https://www.youtube.com/watch?v=sY1S34973zA")
theGodfatherPartII = media.Movie("The Godfather: Part II", "The early life and career of Vito Corleone in 1920s New York is portrayed while his son, Michael, expands and tightens his grip on the family crime syndicate.", "http://www.dvdsreleasedates.com/posters/800/T/The-Godfather-Part-II-1974-movie-poster.jpg", "https://www.youtube.com/watch?v=qJr92K_hKl0")
theDarkKnight = media.Movie("The Dark Knight", "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.", "http://www.impawards.com/2008/posters/dark_knight_ver5_xlg.jpg", "https://www.youtube.com/watch?v=EXeTwQWrcwY")
schindlersList = media.Movie("Schindler's List", "In German-occupied Poland during World War II, Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazi Germans.", "http://img.moviepostershop.com/schindlers-list-movie-poster-1993-1020189480.jpg", "https://www.youtube.com/watch?v=M5FpB6qDGAE")


movies = [star_trek, theShawshankRedemption, theGodfather, theGodfatherPartII, theDarkKnight, schindlersList]
fresh_tomatoes.open_movies_page(movies)
