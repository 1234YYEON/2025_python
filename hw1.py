# 조건 1

def get_radius(prompt):
    r = int(input(prompt))
    return r

# 조건2

def get_circle_area(radius):
    area = 3.14 * radius * radius
    return area

# 주 프로그램부

radius = get_radius('넓이를 구하고자 하는 원의 반지름은? ')
area= get_circle_area(radius)
print (area)
