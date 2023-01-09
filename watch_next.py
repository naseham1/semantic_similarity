import spacy
# Open and read the movies.txt file 
f = open("movies.txt", "r")
f.read
nlp = spacy.load("en_core_web_lg")

# Create a description variable
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
nlpdescription = nlp(description)

# Create a empty movies list 
movie_list = []
# Split the lines in movies.txt to create a movie_list
with f:
    for line in map(str.strip, f):
        if not line:
            continue
        line.split()
        movie_list.append(line)

# Tokenisation of the movie list
for token in movie_list:
    token = nlp(token)
    # print the most similar token to the description
    print(max((nlp(token).similarity(nlpdescription), token) for token in movie_list))