import pandas as pd
import time

df = pd.read_excel('toeic_words.xlsx')

input_count = -1
total_count = 0
correct_count = 0

while True:
    if input_count == -1:
        question = df.sample().values[0]
        print(f'=============== 현재 정답 횟수 : {correct_count} (정답률 : {round(correct_count/total_count, 3) * 100 if correct_count else 0}%))===============')
        total_count += 1
        input_count = 0
    elif input_count < 3:
        print(question[2])

        b = input('정답 : ')
        input_count += 1

        if b == question[1].lower():
            print('정답입니다!')
            input_count = -1
            correct_count += 1
        elif b == 'q':
            total_count -= 1
            break
        else:
            if input_count < 3:
                print(f'오답입니다! 기회가 {3 - input_count}번 남았습니다. 다시 정답을 한번 입력해주세요!')
                time.sleep(0.5)
            if input_count == 2:
                print(f'hint!! {question[1][:1] + "*" * len(question[1][1:-1]) + question[1][-1]}')
                print(len(question[1:-1]))
    else:
        print('기회를 모두 날렸습니다. 정답은 ', question[1], '였습니다!')
        time.sleep(0.5)
        input_count = -1

print(f'최종 결과 입니다. 정답 횟수 : {correct_count} (정답률 : {round(correct_count/total_count, 3) * 100 if correct_count else 0}%)')

