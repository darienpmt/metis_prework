
lst = [['Harsh', 20], ['Beria', 20], ['Varun', 19], ['Kakunami', 19], ['Vikas', 21]]

min_score = min(x[1] for x in lst)

score_dict = {}

for sub_lst in lst:
    names = []
    if sub_lst[1] != min_score:
        score_dict.setdefault(sub_lst[1], names)
        names.append(sub_lst[0])
        

print(score_dict)




# new_lst = []
# for sub_lst in lst:
#     if sub_lst[1] != min_score:
#         new_lst.append(sub_lst)

# penultimate_score = min(x[1] for x in new_lst)
# for sub_lst in new_lst:
#     if sub_lst[1] == penultimate_score:
#         print(sub_lst[0])



