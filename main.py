

movies_log = [

    {
        "genre": "horror",
        "movies": ["human centipede", "annabelle", "scary movie"],
        "times_watched": 20
    },
    {
        "genre": "comedy",
        "movies": ["irresponsible", "you complete me ho", "Jumanji"],
        "times_watched": 50
    },
]

#please do not touch the lines above
def add_a_new_log (genre, movies_w, time):
    new_dictionary = {
        "genre": genre,
        "movies": movies_w,
        "times_watched": time
    }
    movies_log.append(new_dictionary)


#please do not touch the lines below


add_a_new_log("romantic", ["in time", "la rosa de guadalupe", " amor amor"], 5)
i = 0
for item in movies_log:
    print(movies_log[i])
    i += 1