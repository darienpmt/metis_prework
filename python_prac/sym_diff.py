def symDiff(str_m, str_n):

    list_m = str_m.split()
    list_n = str_n.split()

    set_m, set_n = set(map(int, list_m)), set(map(int, list_n))

    for num in sorted(list(set_m.union(set_n) - set_m.intersection(set_n))):
        print(num)


symDiff('2 4 5 9', '2 4 11 12')