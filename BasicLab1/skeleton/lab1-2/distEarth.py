
"""
distEarth : compute distance between
2 location using latitude & longitude

-> using math library

radian(d)
    convert degree to radian

dist_between_loc(loc1, loc2)
    compute distance between 2 locations

loc_dist()
    interface that interacts with user
"""
import math


# convert degree to radian
def radian(d):
    """
    :param d: degree
    :return: radian that converted from degree
    """

    return 0.0


# distance between loc1 & loc2
# using latitude & longitude
def dist_between_loc(loc1, loc2):
    """
    :param loc1: [latitude, longitude]
    :param loc2: [latitude, longitude]
        -> list which contains latitude at index 0,
                               longitude at index 1
    :return: distance between 2 location
    """
    # earth's radius
    r = 6371000  # meter

    # convert latitudes of loc1 and loc2 to radian

    # convert difference of longitudes to radian
    #   : compute difference in degree form

    # cos(theta) : theta - radian of two location

    # get theta by acos
    theta = 0.0

    # radius * theta = distance (r * 2pi = circumference of circle)
    return r * theta


# interact with user
def loc_dist():
    """
    get two location (pair of latitude & longitude)
    print distance between 2 locations
    :return: None
    """
    # call input() function without parameter
    # get first loc's latitude & longitude

    # store at list
    loc1 = [0, 0]

    # get second loc's latitude & longitude

    # store at list
    loc2 = [0, 0]

    # print distance between 2 locations
    print(dist_between_loc(loc1, loc2))


if __name__ == '__main__':
    loc_dist()
