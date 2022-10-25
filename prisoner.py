import random


def prison_free(count):
    total_cnt = 0

    for n in range(count):
        random_number = [i for i in range(100)]
        random.shuffle(random_number)

        is_fail = False
        for prison_num in range(100):
            is_found = False
            index_num = prison_num
            for _ in range(50):
                index_num = random_number[index_num]

                if index_num == prison_num:
                    is_found = True
                    break

            if not is_found:
                is_fail = True
                break

        if not is_fail:
            total_cnt += 1

        print(f"\r진행률 {round(n/count * 100, 4)}% - {count} 중에 {n}개 완료", end=' ')

    print(f"\r진행률 100% - {count} 중에 {count}개 완료", end=' ')

    return total_cnt/count * 100


if __name__ == '__main__':
    cnt = int(input('테스트를 진행할 횟수를 입력해주세요 : '))
    print('\n최종 확률입니다 =>', prison_free(cnt), "%")

