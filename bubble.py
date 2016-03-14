

def bubble_sort(ls):
    '''
    Sorts a list ls
    '''
    for i in range(len(ls) - 1):
        for index, val in enumerate(ls):
            if index < len(ls) - 1 and val > ls[index + 1]:
                    ls[index], ls[index + 1] = ls[index + 1], ls[index]
    return ls

print bubble_sort([13, 2, 5, 1])
