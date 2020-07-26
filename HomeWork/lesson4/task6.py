from itertools import count
from itertools import cycle

for el in count(3):
    if el > 8:
        break
    else:
        print(el)

i = 1
for el in cycle('ABCDE'):
    if i > 20:
        break
    else:
        print(el)
        i += 1
