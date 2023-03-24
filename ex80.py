#LIST
#Program where the user can type 5 numeric values and regist them on a list, already on right position
#(dont use sort(). On the end show the orderly list 
lis = []
for c in range(0,5):
    n = int(input('Type a number:'))
    if c == 0 or n > lis[-1]:
        lis.append(n)
        print('Number registered on the end of the list')
    else:
        pos = 0
        while pos < len(lis):#len its used to make a count of elements on a list or a tuple
            if n <= lis[pos]:
                lis.insert(pos, n)
                print(f'Number registered on position: {pos}')
                break
            pos += 1
print('-*' * 25)
print(f'The values typed IN ORDER: {lis}')