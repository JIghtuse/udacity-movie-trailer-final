#!/usr/bin/env python3

import fresh_tomatoes
import media
import json
import logging


MOVIES_FILE = "movies.json"


def load_movies_data(filename):
    """Loads movie details from specified @filename in JSON format"""
    movies = []
    with open(filename) as movies_file:
        try:
            data = json.load(movies_file)
        except json.decoder.JSONDecodeError:
            logging.critical("Cannot get movies data.")
            return movies

        for movie_data in data:
            try:
                movies.append(media.Movie(**movie_data))
            except TypeError:
                logging.warning("Cannot load a movie; skipping an item")

    return movies

if __name__ == "__main__":
    movies = load_movies_data(MOVIES_FILE)
    if movies:
        movies.sort(key=lambda m: m.title)
        fresh_tomatoes.open_movies_page(movies)
