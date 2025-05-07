# 연습문제 9.4

shopping_bag = {}

print('[구입]')
while True:
    item = input('상품명? ')
    if item == '':
        break
    qty = int(input('수량은? '))
    if item in shopping_bag:
        shopping_bag[item] += qty
    else:
        shopping_bag[item] = qty
    print(f'장바구니에 {item} {qty}개가 담겼습니다.')
    print()
    
print(f'\n>>> 장바구니 보기: {shopping_bag}')

# 검색기능 추가

print('[검색]')
item = input('장바구니에서 확인하고자 하는 상품은? ')
quantity = shopping_bag.get(item)
print(f'{item}은(는) {quantity}개 담겨 있습니다.')
