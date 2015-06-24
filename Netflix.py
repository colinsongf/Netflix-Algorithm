#!/usr/bin/env python3

# -------
# Netflix.py
# -------

from functools import reduce
from math      import sqrt
import json
from urllib.request import urlopen

# ------------
# netflix_predict
# ------------

def netflix_predict (b, c) :
    """
    returns predict 
    """
    #average = (b + c)/2
    return 2

# ------------
# netflix_rmse
# ------------

def netflix_rmse (a, p) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert hasattr(a, "__len__")
    assert hasattr(p, "__len__")
    assert hasattr(a, "__iter__")
    assert hasattr(p, "__iter__")
    z = zip(a, p)
    v = sum((x - y) ** 2 for x, y in z)
    return sqrt(v / len(a))

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
    cache1 = urlopen("http://www.cs.utexas.edu/~ebanner/netflix-tests/ezo55-Average_Viewer_Rating_Cache.json")
    average_user_rating = json.loads(cache1.read().decode(cache1.info().get_param('charset') or 'utf-8'))

    cache2 = urlopen("http://www.cs.utexas.edu/~ebanner/netflix-tests/BRG564-Average_Movie_Rating_Cache.json")
    average_movie_rating = json.loads(cache2.read().decode(cache2.info().get_param('charset') or 'utf-8'))

    cache3 = urlopen("http://www.cs.utexas.edu/~ebanner/netflix-tests/pam2599-probe_solutions.json")
    probe_rating = json.loads(cache3.read().decode(cache3.info().get_param('charset') or 'utf-8'))

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
                for user_id in iter_temp :
                    # get average (movie and user) ratings from caches
                    u_id = user_id[:-1]
                    m_id = movie_id[:-1]
                    user_rating = average_user_rating[str(u_id)]
                    movie_rating = average_movie_rating[str(m_id)]
                    # use cache values to predict rating
                    prediciton = netflix_predict(user_rating, movie_rating)
                    netflix_print(w, prediciton)
                    # store predicted in list
                    calculated_predictions.append(prediciton)
                    # get actual rating from probe cache and store in list
                    probe_users = probe_rating[str(m_id)]
                    actual_rating = probe_users[str(u_id)]
                    actual_predictions.append(actual_rating)
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
    for user_id in iter_temp :
        # get average (movie and user) ratings from caches
        u_id = user_id[:-1]
        m_id = movie_id[:-1]
        user_rating = average_user_rating[str(u_id)]
        movie_rating = average_movie_rating[str(m_id)]
        # use cache values to predict rating
        prediciton = netflix_predict(user_rating, movie_rating)
        netflix_print(w, prediciton)
        # store predicted in list
        calculated_predictions.append(prediciton)
        # get actual rating from probe cache and store in list
        probe_users = probe_rating[str(m_id)]
        actual_rating = probe_users[str(u_id)]
        actual_predictions.append(actual_rating)

    rmse = netflix_rmse(actual_predictions, calculated_predictions)
    netflix_print_rmse(w, rmse)
    w.write(str(len(calculated_predictions)) + "\n")
