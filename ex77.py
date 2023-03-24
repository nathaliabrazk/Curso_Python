#COMPOSITE VARIABLES
#Program will has a tuple with several words(dont use accents). Before this need show, for every word what are
#your vowels
words = ('bed', 'hair', 'nails', 'book', 'clothes', 'eyeglasses', 'mouse',
         'ball', 'bag', 'wather', 'flower', 'makeup', 'gloss', 'clock')
for w in words:
    print(f'\nOn word {w.upper()} we have',end=' ')
    for letter in w:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')

