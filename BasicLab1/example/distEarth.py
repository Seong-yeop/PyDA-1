import math

def radian(d):
    """
    :param d: degree
    :return: radian that converted from degree
    """
    return d * math.pi / 180.0


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
    lat1_r = radian(loc1[0])
    lat2_r = radian(loc2[0])

    # convert difference of longitudes to radian
    #   : compute difference in degree form
    d_lon_r = radian(loc2[1]-loc1[1])

    # cos(theta) : theta - radian of two location
    costh = (math.sin(lat1_r) * math.sin(lat2_r) +
             math.cos(lat1_r) * math.cos(lat2_r) * math.cos(d_lon_r))

    # get theta by acos
    theta = math.acos(costh)

    # radius * theta = distance (r * 2pi = circumference of circle)
    return r * theta

# interact with user
def loc_dist():
    """
    get two location (pair of latitude & longitude)
        loc := tuple contains lat & lon
    print distance between 2 locations
    :return: None
    """
    # call input() function without parameter
    # get first loc's latitude & longitude

    # store at tuple
    loc1 = (37.455813, 126.954699)

    # get second loc's latitude & longitude

    # store at tuple
    loc2 = (37.266653, 126.999386)

    # print distance between 2 locations
    print(dist_between_loc(loc1, loc2))


if __name__ == '__main__':
    loc_dist()