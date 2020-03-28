from itertools import combinations

def minion_game(string):
    vowels = 'AEIOU'

    sub_strings = [string[x:y] for x, y in combinations(range(len(string) + 1), r = 2)]

    kevin = {}
    stuart =  {}

    for word in sub_strings:
        if word[0] in vowels:
            kevin.setdefault(word,0)
            kevin[word] += 1
        else:
            stuart.setdefault(word,0)
            stuart[word] += 1

    kevin_score = sum(kevin.values())
    stuart_score = sum(stuart.values())

    if stuart_score > kevin_score:
        print('Stuart', stuart)
    elif stuart_score < kevin_score:
        print('Kevin', kevin_score)
    else:
        print('Draw')
                
print(minion_game('AAAAAAAAAAAAAAAAAAAAAAAAA'))