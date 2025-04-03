# 사용자 정의 함수부
def get_fixed_price(discount_rate, discounted_price):
    original = discounted_price / (1 - discount_rate/100)
    return original

# 주 프로그램부

rate = float(input('할인율은? '))
a_received = float(input('A 상품의 할인된 가격은? '))
b_received = float(input('B 상품의 할인된 가격은? '))

a_origin = get_fixed_price(rate, a_received)
b_origin = get_fixed_price(rate, b_received)


print('A 상품의 정가는 ', a_origin)
print('B 상품의 정가는 ', b_origin)


