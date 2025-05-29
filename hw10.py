import os
import pickle

def input_scores():
    s = []
    i = 0
    while True:
        n = int(input(f'#{i + 1}? '))
        if n < 0:
            break
        s.append(n)
        i += 1
    return s

def get_average(s):
    total = 0
    for n in s:
        total += n
    return total / len(s)

def show_scores(s):
    for n in s:
        print(n, end = ' ')
    print()

def save_data(s, filepath):
    with open(filepath, 'wb') as file:
        pickle.dump(s, file)

def load_data(filepath):
    with open(filepath, 'rb') as file:
        return pickle.load(file)

# 주 프로그램부

filepath = 'score.bin'

if os.path.exists(filepath):
    print('[파일 읽기]')
    scores = load_data(filepath)
else:
    print('[점수 입력]')
    scores = input_scores()
    save_data(scores, filepath)

print('\n[점수 출력]')
print('개인점수: ', end=' ')
show_scores(scores)

avg = get_average(scores)
print(f'평균: {avg: }')
