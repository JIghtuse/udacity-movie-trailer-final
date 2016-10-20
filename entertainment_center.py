#!/usr/bin/env python3

import fresh_tomatoes
import logging
import media


MOVIES_FILE = "movies.txt"


def load_movies_data(filename):
    """Loads movie details from specified @filename"""
    movies = []
    with open(filename) as movies_file:
        while True:
            try:
                title = movies_file.readline()
                duration = int(movies_file.readline())
                storyline = movies_file.readline()
                poster_url = movies_file.readline()
                trailer_url = movies_file.readline()
                movie = media.Movie(title, duration, storyline,
                                    poster_url, trailer_url)
            except ValueError:
                logging.warning("Cannot load a movie; skipping rest of input")
                # Following reads is dangerous, stop now
                break

            movies.append(movie)

            if not movies_file.readline():
                # Reached end of file, no more data
                break
    return movies

if __name__ == "__main__":
    movies = load_movies_data(MOVIES_FILE)
    fresh_tomatoes.open_movies_page(movies)
