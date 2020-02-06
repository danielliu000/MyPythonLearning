'''check a num if in a list'''

my_list = [[1, 2, 11, 4], [2, 4, 8, 9], [3, 7, 9, 10]]


def find_num(target, array):

    for each_row in array:
        for each in each_row:
            if target == each:
                print('yes')
                return
    print('no')
    return


find_num(11, my_list)
