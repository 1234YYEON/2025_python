# 사용자 정의 함수부
def rep_char(c, n):
    print(c * n)

def draw_line_string(msg1, msg2):
    nstr = len(msg1)if(len(msg1) > len(msg2)) else len(msg2)
    rep_char('-', nstr + 2)
    print(f' {msg1}\n {msg2}')
    rep_char('-', nstr + 2)

# 주 프로그램부
name = input('Input his/her name: ')
msg1 = 'Hello ' + name
msg2 = 'Welcome to Seoul.'
draw_line_string(msg1, msg2)
draw_line_string(msg1, msg2)

    
