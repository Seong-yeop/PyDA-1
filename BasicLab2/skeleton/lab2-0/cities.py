
"""
Python Basic Lab 2-0
Compute distance between
2 cities using latitude & longitude

get_cities()
    making dict {key:= name : val:= loc}
        loc:= (lat, lon) <- tuple

get_city_by_name(cities, name)
    get loc from cities <- using DB from get_cities

city_dist()
    interact with user
"""
import math


"""
just copy & paste 2 functions 
from distEarth.py
- radian(d
- dist_between_loc(loc1, loc2)
"""
# convert degree to radian
def radian(d):
    """
    just copy and paste from distEarth.py
    """
    pass # remove this


# distance between loc1 & loc2
# using latitude & longitude
def dist_between_loc(loc1, loc2):
    """
    just copy and paste from distEarth.py
    """
    pass # remove this


# from 'cities.txt' get
# name of city                  <- str      : key
# (latitide, longitude) loc     <- tuple    : val
# => make cities                <- dict
def get_cities():
    """
    :return: cities <- dict {key:= name : val:= loc}
                    loc:= (lat, lon) <- tuple
    """
    # try to open file : 'cities.txt'

    # make cities
    cities = dict()

    # read info from file line by line
        # split the line

        # get city name without country name

        # get latitude & longitude

        # store info in names & locs

    # return names & locs
    return cities


# get location (lat, lon) by name
def get_city_by_name(cities, name):
    """
    :param cities: dict {key:= name : val:= loc}
    :param name: name of city to find
    :return: loc <- (latitude, longitude) : tuple
    """
    # check name is in cities
    # if there are no such name, return None
    return None


# interface
def city_dist():
    """
    :return: None
    """
    # call 'the get_cities' to get a DB

    # while user enter 'EXITprogram' processing
        # call input() with out parameter
        # be careful '\n' : using strip()

        # if 'EXITprogram' stop the program

        # get two locs using 'get_city_by_name'
        # CAUTION : two city names separated by ', '

        # if loc1 and loc2 in cities's name print dist
        # else print 'There are no ~' (~ : wrong name)

    # exit the program
    # CAUTION : if user enter 'EXITprogram', then print 'exit'
    print('exit')
    exit(0)


if __name__ == '__main__':
    city_dist()
