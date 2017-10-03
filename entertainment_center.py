import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")

jack_frost = media.Movie("Rise of the Guardians",
                         "Rise of the Guardians is an epic adventure that tells the story of a group of heroes",
                         "https://upload.wikimedia.org/wikipedia/en/9/92/Rise_of_the_Guardians_poster.jpg",
                         "https://youtu.be/yd71LWhCO4s")

jack_skeletron = media.Movie("The Nightmare Before Christmas",
                             "Adventures of Jack Skeletron",
                             "https://upload.wikimedia.org/wikipedia/en/9/9a/The_nightmare_before_christmas_poster.jpg",
                             "https://www.youtube.com/watch?v=wr6N_hZyBCk")

jack_sparrow = media.Movie("Pirates of the Caribbean",
                        "A pirate story of Capitan Jack Sparrow",
                        "https://upload.wikimedia.org/wikipedia/en/8/89/Pirates_of_the_Caribbean_-_The_Curse_of_the_Black_Pearl.png",
                        "https://www.youtube.com/watch?v=naQr0uTrH_s")

lord_of_the_rings = media.Movie("The Lord of the Rings",
                                "The Lord of the Rings is a film series consisting of three high fantasy adventure films",
                                "https://upload.wikimedia.org/wikipedia/en/8/87/Ringstrilogyposter.jpg",
                                "https://www.youtube.com/watch?v=V75dMMIW2B4")

movies = [toy_story, avatar, jack_frost, jack_skeletron, jack_sparrow, lord_of_the_rings]
fresh_tomatoes.open_movies_page(movies)
