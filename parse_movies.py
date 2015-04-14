#!/bin/python

import json
import unicodedata

movie_filename = "movies_tab_clean.txt"
tags_filename = "tags.csv"

# write data as json object for future processing
def writeToJSON(filename, obj):
    with open(filename, 'w') as outfile:  
        json.dump(obj, outfile)

# modify movie names as necessary (change encoding?)
def parseMovieNames(name):
    if name.startswith('"') and name.endswith('"'):
        name = name[1:-1]
    ## Need to process out the unordered titles - "The", "A", etc.???
    return name

def main():
    movie_ID_to_name = {} ## movieID to text name of movie
    movie_ID_to_genres = {} ## movieID to list of genres
    with open(movie_filename, 'rU') as f:
        ## extract the movieIDs and genres
        for line in f:
            print line
            items = line.strip().split('\t') 
            name = parseMovieNames(items[1])
            movie_ID_to_name[items[0]] = name
            genres = items[2].strip().split('|')
            movie_ID_to_genres[items[1]] = genres
    movie_ID_to_tags = {} ## movieID to list of tags
    with open(tags_filename) as f:
        ## extract the movieIDs and tags
        for line in f:
            items = line.strip().split(',')
            movie_ID_to_tags.setdefault(items[1], []).append(items[2])

    ## create a flipped index for tags
    tags_to_movie_IDs = {}
    for movie, tags in movie_ID_to_tags.items():
        for tag in tags:
            tags_to_movie_IDs.setdefault(tag, []).append(movie)

    ## sort the lists associated with each tag by movieID
    for tag in tags_to_movie_IDs:
        movies = tags_to_movie_IDs[tag]
        tags_to_movie_IDs[tag] = sorted(movies)

    ## create a flipped index for genres
    genres_to_movie_IDs = {}
    for movie, genres in movie_ID_to_genres.items():
        for genre in genres:
            genres_to_movie_IDs.setdefault(genre, []).append(movie)

    ## sort the lists associated with each tag by movieID
    for genre in genres_to_movie_IDs:
        movies = genres_to_movie_IDs[genre]
        genres_to_movie_IDs[genre] = sorted(movies)

    ## write out the five dictionaries in JSON
    writeToJSON("movie_ID_to_name.json", movie_ID_to_name)
    writeToJSON("movie_ID_to_tags.json", movie_ID_to_tags)
    writeToJSON("movie_ID_to_genre.json", movie_ID_to_genres)
    writeToJSON("tags_to_movie_IDs.json", tags_to_movie_IDs)
    writeToJSON("genres_to_movie_IDs.json", genres_to_movie_IDs)

if __name__ == '__main__':
     main()
