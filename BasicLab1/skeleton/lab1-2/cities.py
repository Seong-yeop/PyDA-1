
"""
Python Basic Lab 1-2
Compute distance between
2 cities using latitude & longitude

get_cities()
    making list of two lists : [names, locs]
get_city_by_name(cities, name)
    get loc from cities <- from get_cities
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
# name of city                  <- str
# [latitide, longitude] loc     <- list
def get_cities():
    """
    names : list of cities
    locs : list of locations
        location : list that latitude at index 0,
                             longitude at index 1
    :return: cities = [names, locs] list of lists
    index of names and locs are corresponding
    """
    # try to open file : 'cities.txt'

    # make names and locs
    names = list()
    locs = list()

    # read info from file line by line
        # split the line

        # get city name without country name

        # get latitude & longitude

        # store info in names & locs

    # return names & locs
    return [names, locs]


# get location [lat, lon] by name
def get_city_by_name(cities, name):
    """
    :param cities: [names, locs] : list from get_cities
    :param name: name of city to find
    :return: loc <- [latitude, longitude] : list
    """
    # check name is in cities [names, locs]

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
