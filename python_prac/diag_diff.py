

def diagonalDifference(arr):

    n = len(arr[0])

    main_diag = sum([arr[i][i] for i in range(n)])

    sec_diag = sum([arr[i][n-i-1] for i in range(n)])

    return abs(main_diag - sec_diag)




print(diagonalDifference([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))


