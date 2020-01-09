"""
cities : 두 도시간의 거리 재기

"""
import math


# 각도 d 를 radian 으로 변환
def radian(d):
    return d * math.pi / 180.0


# 위도 경도로 나타낸 두 위치 간의 거리
def dist_between_loc(loc1, loc2):
    """
    :param loc1: 위치 정보 튜플 (latitude, longitude)
    :param loc2: 위치 정보 튜플 (latitude, longitude)
    :return: 두 위치 간의 거리
    """
    # 지구의 반지름
    r = 6371000 # m

    # loc1 과 loc2 의 위도를 radian 으로 변환
    lat1_r = radian(loc1[0])
    lat2_r = radian(loc2[0])

    # 경도 차이를 radian 으로 변환
    d_lon_r = radian(loc2[1]-loc1[1])

    # 두 위치 사이의 구 중심으로부터 각도 차이 : theta 구하기
    # cos(theta)
    costh = (math.sin(lat1_r) * math.sin(lat2_r) +
             math.cos(lat1_r) * math.cos(lat2_r) * math.cos(d_lon_r))
    theta = math.acos(costh)
    # 반지름 * 각도 = 호의 길이 (r * 2pi = 원의 둘레)
    return r * theta


# 사용자에게 두 위치의 위도 경도를 각각 입력 받아 거리를 출력하는 프로그램
def loc_dist():
    # 첫 번째 위치의 위도와 경도를 차례로 받고
    lat1 = float(input('첫 번째 위도 : '))
    lon1 = float(input('첫 번째 경도 : '))
    # 튜플에 저장 후 출력
    loc1 = (lat1, lon1)
    print(loc1)

    # 두 번째 위치의 위도와 경도를 차례로 받고
    lat2 = float(input('두 번째 위도 : '))
    lon2 = float(input('두 번째 경도 : '))
    # 튜플에 저장 후 출력
    loc2 = (lat2, lon2)
    print(loc2)

    # 두 지점 간의 거리를 출력
    print('거리 :', dist_between_loc(loc1, loc2))


# 'cities.txt' 파일로 부터
# 도시의 이름 (나라 제외)    <- str
# (위도, 경도) loc      <- tuple
# {도시의 이름 : loc} 의 딕셔너리를 만들어 반환하는 함수
def get_cities():
    """
    :return: 도시정보 {key = city_name : value = (longitude, latitude) } 모은 딕셔너리
    """
    # 파일 열기
    f = open('./cities.txt', 'r')
    if not f:
        # 파일 열기에 실패한 경우 빈 리스트 반환
        return []

    # 빈 딕셔너리를 만들어
    # key = name, value = (latitude, longitude)
    # 형태로 DB 구축하기
    cities = dict()
    for line in f:
        # 한 줄씩 읽기

        # 읽어들이 line 을 적절히 나누기
        lineStr = line.split('\t')
        name = lineStr[0].split(',')[0]
        lat = float(lineStr[1])
        lon = float(lineStr[2])

        # 위치를 tuple 로 만들어 딕셔너리에 모으기
        cities[name] = (lat, lon)

    # 파일 닫기
    f.close()
    # 모은 도시 정보 반환하기
    return cities


# 도시 위치를 이름으로 가져오기
def get_city_by_name(cities, name):
    """
    :param cities: 도시 정보의 딕셔너리 (get_cities 애서 받은)
    :param name: 찾고자 하는 도시의 이름
    :return: (도시 위치) <- (latitude, longitude)
    """
    # cities 에 찾는 도시가 있는지 체크
    return cities.get(name, None)


# 사용자에게 두 도시의 이름을 입력받아 거리를 출력하는 프로그램
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


city_dist()

