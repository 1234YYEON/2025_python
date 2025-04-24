def display_multiplication_table() :
    for i in range(1, 10) :
        for dan in range(2, 6):
            print(f'{dan} X {i} = {dan * i:2d}', end ='\t')
        print()

    print()
        
       # 6단 - 9단
       
    for i in range(1, 10) :
        for dan in range(6, 10):
            print(f'{dan} X {i} = {dan * i:2d}', end ='\t')
        print()
        
    
    
display_multiplication_table()
