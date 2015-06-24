#!/usr/bin/env python3

# -------
# Netflix.py
# -------

from functools import reduce
from math      import sqrt
from numpy     import mean, sqrt, square, subtract
import json

# ------------
# netflix_predict
# ------------

def netflix_predict (b, c) :
    """
    returns predict 
    """
    average = (b + c)/2
    return average

# ------------
# netflix_rmse
# ------------

def netflix_rmse (a, p) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    return sqrt(mean(square(subtract(a, p))))

# -------------
# netflix_print
# -------------

def netflix_print (w, i) :
    """
    w a writer
    j the movie_id or the customer_id
    """
    w.write(str(i) + "\n")

# -------------
# netflix_print_rmse
# -------------

def netflix_print_rmse (w, j) :
    """
    w a writer
    j the movie_id or the customer_id
    """
    w.write("RMSE: " + "{0:.2f}".format(j) +  "\n")

# -------------
# netflix_solve
# -------------

def netflix_solve (r, w) :
    """
    r a reader
    w a writer
    """
    
    # open cache files from hard coded address
    """
    with open('/u/thunt/cs373-netflix-tests/ddg625-ActualCache.json', 'r') as f:
        original_rating = json.load(f)
    with open('/u/thunt/cs373-netflix-tests/irvin-user_avg.json', 'r') as i:
        avg_user_rating = json.load(i)
    with open('/u/thunt/cs373-netflix-tests/irvin-movie_avg.json', 'r') as g:
        avg_movie_rating = json.load(g)
    """   
 
    # parses input movie by movie and places into temp_list
    # where first value is movie_id and the rest are customer_id's
    
    temp_list = []
    actual_predictions = []
    calculated_predictions = []
    count = 0

    for s in r :
        if s[-2] == ':' :
            if count > 0 :
                # handle old list --> make predictions 
                iter_temp = iter(temp_list)
                movie_id = next(iter_temp)
                netflix_print(w, movie_id)
                for q in iter_temp :
                    #prediction = netflix_predict(movie_id, user_id, av_movie_rating, av_user_rating)
                    #netflix_print(w, prediction)
                    #calculated_predictions.append(prediciton)
                    actual_predictions.append(0)
                temp_list.clear()
                temp_list.append(s[:-1])
            else :
                # setup new list
                temp_list.clear()
                temp_list.append(s[:-1])
                count += 1
        else :
            temp_list.append(s)     
    # handle last list iteration
    iter_temp = iter(temp_list)
    movie_id = next(iter_temp)
    netflix_print(w, movie_id)
    for q in iter_temp :
        #prediction = netflix_predict(movie_id, user_id, av_movie_rating, av_user_rating)
        #netflix_print(w, prediction)
        #calculated_predictions.append(prediciton)
        actual_predictions.append(0)

    #rmse = netflix_rmse(actual_predictions, calculated_predictions)
    #w.write(len(calculated_predictions))
   
