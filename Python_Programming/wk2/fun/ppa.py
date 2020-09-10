# pen pineapple apple pen

import time

lyrics = ['I have a pen', 'I have an apple', 'UH!', 'Apple Pen!']

for song in lyrics:
    print(song)
    time.sleep(.5)

width = 17
height = 12.0
delimiter = '.'

print(width//2)
print(width/2.0)
print(height/3)
print(1+2*5)
print(delimiter * 5)
print("")

print(f'''Testing
Pen\t${width}
Apple\t${width}
Pear\t${width}
multi\t${width}
line comment''')
