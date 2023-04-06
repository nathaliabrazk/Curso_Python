#FUNCTIONS
def fold(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


numbers = [2, 5, 3, 11, 9]
fold(numbers)
print(numbers)