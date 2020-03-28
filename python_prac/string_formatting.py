def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(number):
        print('{:{align}{width}} {:{align}{width}} {:{align}{width}} {:{align}{width}}'.format(i+1, oct(i+1)[2:], hex(i+1).upper()[2:], bin(i+1)[2:], align='>', width=width))
        

print(print_formatted(17))


