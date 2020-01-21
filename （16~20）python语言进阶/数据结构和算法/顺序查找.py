def seq_search(items, key):
    '''顺序查找'''
    for index, items in enumerate(items):
        if items == key:
            return index
    return -1

origin = [10, 12, 4, 78, 54, 9]
print(seq_search(origin, 54))
