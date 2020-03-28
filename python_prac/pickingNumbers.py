def pickingNumbers(a):
    a = sorted(a)
    longest_lst = []
    for i in range(len(a)):
        current_longest = [a[i]]
        for j in range(i+1, len(a)):
            if abs(current_longest[0] - a[j]) > 1:
                break
            else:
                current_longest.append(a[j])
        if len(current_longest) > len(longest_lst):
            longest_lst = current_longest
    return max([sum((a.count(i), a.count(i+1))) for i in set(a)])

print(pickingNumbers([1, 1, 2, 2, 4, 4, 5, 5, 5]))