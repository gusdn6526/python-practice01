# 주어진 if 문을 dict를 사용하도록 수정하세요.

menu = input('메뉴: ')

if menu == '오뎅':
    price = 300
elif menu == '순대':
    price = 400
elif menu == '만두':
    price = 500
else:
    price = 0

print('가격: {0}'.format(price))

