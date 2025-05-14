# buy() 함수

def buy():
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
        print(f'장바구니에 {item} {qty}개가 담겼습니다.\n')
    return shopping_bag
        
    
def show(shopping_bag):
    print('\n>>> 장바구니 보기:', shopping_bag)

def find_item(shopping_bag):
    while True:
        print('[검색]')
        item = input('장바구니에서 확인하고자 하는 상품은? ')
        qty = shopping_bag.get(item)
        if qty is None:
            print(f'장바구니에 {item}은(는) 없습니다.')
        else:
            print(f'{item}은(는) {qty}개 담겨 있습니다.')
    

shopping_bag = buy()
show(shopping_bag)
find_item(shopping_bag)
