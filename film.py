def addMovie(newFilm, newActor):
    if newFilm not in movie.keys():
        movie[newFilm] = newActor
    return movie

movie = {"Lucifer" : "Mohanlal",
         'bheeshmaparvam' : 'Mammotti',
         'niram' : 'kunchakko boban',
         'CID moosa' : 'dileep'
        }

new = addMovie('chithram', 'mohanlal')

for i,j in movie.items():
    print(f'The actor {j} has acted in {i}')