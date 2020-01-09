
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
from distEarth import dist_between_loc


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
    try:
        f = open('./cities.txt', 'r')
    except:
        print('fail')
        exit(1)

    # make names and locs
    names = list()
    locs = list()
    for line in f: # read line by line
        # split the line
        lineStr = line.split('\t')

        # get city name without country name
        name = lineStr[0].split(',')[0]
        # get latitude & longitude
        lat = float(lineStr[1])
        lon = float(lineStr[2])

        # store info in names & locs
        names.append(name)
        locs.append([lat, lon])

    # close the file
    f.close()
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
    if name in cities[0]:
        return cities[1][cities[0].index(name)]
    else:
        return None


# interface
def city_dist():
    """
    :return: None
    """
    # call 'the get_cities' to get a DB
    cities = get_cities()

    # while user enter 'EXITprogram' processing
    while True:
        # call input() with out parameter
        userInput = input().strip()

        # if 'EXITprogram' stop the program
        if userInput == 'EXITprogram':
            break

        # get two locs using 'get_city_by_name'
        # CAUTION : two city names separated by ', '
        city1and2 = userInput.split(', ')
        loc1 = get_city_by_name(cities, city1and2[0])
        loc2 = get_city_by_name(cities, city1and2[1])

        # if loc1 and loc2 in cities's name print dist
        # else print 'There are no ~' (~ : wrong name)
        if not loc1:
            print("There are no '" + city1and2[0] + "'")
        elif not loc2:
            print("There are no '" + city1and2[1] + "'")
        else:
            print(dist_between_loc(loc1, loc2))

    # exit the program
    print('exit')
    exit(0)


if __name__ == '__main__':
    city_dist()
