"""
File: class_reviews.py
Name:Ethan 林劭懿
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""
# This constant controls when to stop
EXIT = -1


def main():
    """
    TODO:
    """
    data = str(input('Which class? '))
    # capital insensitive
    data_ch = data.upper()
    # input score
    score = int(input('Score : '))
    # illegal format
    if data == str(EXIT):
        print('No class scores were entered')
    else:
        if data_ch == 'SC001':
            score_001 = score
            max_001 = score_001
            min_001 = score_001
            sum_001 = 0
            sum_n_001 = 0
            score = int(input('Score : '))
            if score == EXIT:
                for i in range(13):
                    print('=', end='')
                print('SCOO1', end='')
                for i in range(13):
                    print('=', end='')
                print('No Score for SC001')
                break
            if score > max_001:
                max_001 = score_001
            if score < min_001:
                min_001 = score_001
            if score != EXIT:
                sum_001 = sum_001 + score_001
                sum_n_001 = sum_n_001 + 1
            avg_001 = sum_001 / sum_n_001
        else:
            score_101 = score
            max_101 = score_101
            min_101 = score_101
            sum_101 = 0
            sum_n_101 = 0
            if data == EXIT:
                for i in range(13):
                    print('=', end='')
                print('SC101', end='')
                for i in range(13):
                    print('=', end='')
                print('No Score for SC101')
                break
            if score > max_101:
                max_101 = score_101
            if score < min_101:
                min_101 = score_101
            if score != EXIT:
                sum_101 = sum_101 + score_101
                sum_n_101 = sum_n_101 + 1
            avg_101 = sum_101 / sum_n_101
        while True:
            score = int(input('Score : '))
            if data_ch == 'SC001':
                score_001 = score
                max_001 = score_001
                min_001 = score_001
                sum_001 = 0
                sum_n_001 = 0
                score = int(input('Score : '))
                if score == EXIT:
                    for i in range(13):
                        print('=', end='')
                    print('SCOO1', end='')
                    for i in range(13):
                        print('=', end='')
                    print('No Score for SC001')
                    break
                if score > max_001:
                    max_001 = score_001
                if score < min_001:
                    min_001 = score_001
                if score != EXIT:
                    sum_001 = sum_001 + score_001
                    sum_n_001 = sum_n_001 + 1
                avg_001 = sum_001 / sum_n_001
            else:
                score_101 = score
                max_101 = score_101
                min_101 = score_101
                sum_101 = 0
                sum_n_101 = 0
                if data == EXIT:
                    for i in range(13):
                        print('=', end='')
                    print('SC101', end='')
                    for i in range(13):
                        print('=', end='')
                    print('No Score for SC101')
                    break
                if score > max_101:
                    max_101 = score_101
                if score < min_101:
                    min_101 = score_101
                if score != EXIT:
                    sum_101 = sum_101 + score_101
                    sum_n_101 = sum_n_101 + 1
                avg_101 = sum_101 / sum_n_101

    # Print SC001
        if score_001 != 0:
            for i in range(13):
                print('=', end='')
            print('SCOO1', end='')
            for i in range(13):
                print('=', end='')
            print('Max (001): ' + str(max_001))
            print('Min (001): ', str(min_001))
            print('Avg (001): ', str(avg_001))


    # Print SC101
        if score_101 != 0:
            for i in range(13):
                print('=', end='')
            print('SC101', end='')
            for i in range(13):
                print('=', end='')
            print('Max (101): ' + str(max_001))
            print('Min (101): ', str(min_001))
            print('Avg (101): ', str(avg_101))



# def collect():
#     while True:
#         which_class()
#         score()
#         save_point()
#
#
# def which_class():
#     classroom = str(input('Which class? '))
#     classroom_ch = classroom.upper()
#     if classroom_ch == EXIT:
#         print('No class score are answer.')
#     return classroom_ch
#
#
#
# def score():
#     point = int(input('Score: '))
#     return point
#
#
# def save_point():
#     if classroom_ch = 'SC001'





# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
