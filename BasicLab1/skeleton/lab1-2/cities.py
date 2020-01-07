"""
cities : 두 도시간의 거리 재기
뼈대 코드는 예시일 뿐, 더 편하신 방법이 있다면
parameter, return 값, 내부 logic
변수의 타입 등 얼마든지 뼈대 코드를 수정하셔도 됩니다.
"""
import math


# 각도 d 를 radian 으로 변환
def radian(d):
    """
    :param d: 각도 (0 ~ 360)
    :return: radian (실수)
    """
    # 각도를 radian 으로 변환하여 반환
    # hint : math.pi
    #        2pi = 360도

    return


# 위도 경도로 나타낸 두 위치 간의 거리
def dist_between_loc(loc1, loc2):
    """
    :param loc1: 위치 정보 튜플 (latitude, longitude)
    :param loc2: 위치 정보 튜플 (latitude, longitude)
    :return: 두 위치 간의 거리
    """
    # 지구의 반지름 6371 km
    r = 6371000 # m 단위

    # loc1 과 loc2 의 위도를 radian 으로 변환
    lat1_r =
    lat2_r =

    # 경도 차이를 radian 으로 변환
    d_lon_r =

    # 두 위치 사이의 구 중심으로부터 각도 차이 : theta 구하기
    # hint : math.cos, math.sin
    #        math.acos
    #        theta = acos(cos(theta))
    costh =

    theta =

    # 구한 각도를 이용해 두 위치 사이 거리 구하기 (m)
    # hint : 원의 둘레 = 원의 반지름 * 2pi
    #        2pi = 360도
    return


# 사용자에게 두 위치의 위도 경도를 각각 입력 받아 거리를 출력하는 프로그램
def loc_dist():
    # 첫 번째 위치의 위도와 경도를 차례로 받고

    # 튜플에 저장 후 출력

    # 두 번째 위치의 위도와 경도를 차례로 받고

    # 튜플에 저장 후 출력

    # 두 지점 간의 거리를 출력


# 'cities.txt' 파일로 부터
# 도시의 이름 (나라 제외)    <- str
# (위도, 경도) loc      <- tuple
# {도시의 이름 : loc} 의 딕셔너리를 만들어 반환하는 함수
def get_cities():
    """
    :return: 도시정보 {key = city_name : value = (longitude, latitude) } 모은 딕셔너리
    """
    # 파일 열기
    # 경로 ./cities.txt
    if :
        # 파일 열기에 실패한 경우 빈 리스트 반환
        return []

    # 빈 딕셔너리를 만들어
    # key = name, value = (latitude, longitude)
    # 형태로 DB 구축하기
    while True:
        # 한 줄씩 읽기

        if :
            # 더 이상 읽을 것이 없는 경우 break
            break

        # 읽어들이 line 을 적절히 나누기

        # '도시이름, 나라' 에서 도시 이름만 추출

        # 위도와 경도를 숫자 형태로 저장


        # 위치를 tuple 로 만들어 딕셔너리에 모으기

    # 파일 닫기

    # 모은 도시 정보 딕셔너리 반환하기
    return


# 도시 위치를 이름으로 가져오기
def get_city_by_name(cities, name):
    """
    :param cities: 도시 정보의 딕셔너리 (get_cities 애서 받은)
    :param name: 찾고자 하는 도시의 이름
    :return: (도시 위치) <- (latitude, longitude)
    """
    # cities 에 찾는 도시가 있는지 체크

        # 같은 이름의 도시가 있다면 위치 반환

        # 같은 이름의 도시가 없다면 None 반환
        return None


# 사용자에게 두 도시의 이름을 입력받아 거리를 출력하는 프로그램
def city_dist():
    """
    사용자가 done 을 입력할 때 까지
    계속해서 두 도시의 이름을 차례로 받아
    두 도시 사이의 거리를 출력
    :return: 없음
    """
    # 먼저 DB 구축 하기
    cities = get_cities() # 이 줄 외에 cities 를 호출하지 않습니다.
    # 사용자가 끝낼 때까지 계속함
        # 두 도시 이름 차례로 받기

            # 제대로 된 입력이 올 때까지 받음
                # 사용자 입력이 done 이라면 프로그램 종료
                if :
                    print('프로그램을 종료합니다.')
                    exit()
                # 도시 정보를 불러옴

                    # 불러오는 데에 실패한 경우 오류 메시지 출력 후

                    # 도시 이 새로 입력 받음


        # 입력 받은 두 도시의 거리를 출력
        # 구현한 dist_between_loc() 함수 사용

    # 아무것도 반환하지 않음

