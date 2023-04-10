#FUNCTIONS PT 2
#Interactive help:
def counter(s, e, st):
    """
    -> Do a count and show on the screen.
    :Parameter s: Start of the count
    :Parameter e: End of the count
    :Parameter st: Steps between the numbers
    :Return: No return
    """
    c = s
    while c <= e:
        print(f'{c}', end='..')
        c += st
    print('end')

help(counter)