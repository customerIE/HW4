# Напишите функцию для транспонирования матрицы.

def trans_matrix(*a_list: list[[int]]) -> list[()] | str:
    is_trans = True
    col = len(a_list[0])
    for a in list(a_list):
        if len(a) != col:
            is_trans = False
    if is_trans:
        return list(zip(*a_list))
    else:
        return 'Матрицу нельзя транспорировать'


print(trans_matrix([1, 3, 5], [2, 4, 6]))
