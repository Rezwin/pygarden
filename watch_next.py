import spacy

nlp = spacy.load('en_core_web_md')

# read movies.txt and build internal dictionary for look up
movies = {}
for line in open('movies.txt').readlines():
    # split by : to movie name and description and load in dictionary
    index = line.find(":")
    name = line[0:index]
    description = line[index+1:]
    movies[name] = description

# function to find the similar movies from description
def find_similar_movie(description):
    closest_match_movie_name = None
    closest_match_movie_similarity = None

    nlpd = nlp(description)

    for movie in movies:
        similarity = nlpd.similarity(nlp(movies[movie]))
        if closest_match_movie_name is None or similarity > closest_match_movie_similarity:
                closest_match_movie_name = movie
                closest_match_movie_similarity = similarity
    return closest_match_movie_name

hulk_movie_description = "Will he save their world or destroy it? when they hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

similar_movie = find_similar_movie(hulk_movie_description)

print("similar movie: ", similar_movie)


