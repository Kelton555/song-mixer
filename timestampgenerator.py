import math

# yes, i know order of operations exists, i know that i don't need the grouping, but it's easier for me to type this way
times = [(11*60*60)+(55*60)+6, (11*60*60)+(54*60)+54, (11*60*60)+(55*60)+7, (11*60*60)+(55*60)+1, (11*60*60)+(54*60)+50, (11*60*60)+(55*60)+1, (11*60*60)+(54*60)+59, (11*60*60)+(55*60)+6, (4*60)+51]
# and we'll just put the last link twice to prevent the issue at the end of the thing
links = ['https://youtu.be/A4kagEufIX0', 'https://youtu.be/VMPiUxZgsx0', 'https://youtu.be/oYR2EjAijQ0', 'https://youtu.be/8ZXxOcf-DdQ', 'https://youtu.be/ucGn05vNEJw', 'https://youtu.be/lpND4nNUDrs', 'https://youtu.be/TSNaqkH8giA', 'https://youtu.be/w27OsA9olkU', 'https://youtu.be/6FdPKJKLRQ4', 'https://youtu.be/6FdPKJKLRQ4']

f = open('log.txt', 'r')
o = open('timestamps.md', 'w')

for line in f:
    line = line.strip().split(':')
    time = math.floor(int(line[0].strip())/1000)
    path = line[1].strip()

    i = 0
    for x in times:
        if time > x:
            time = time - x
            i = i + 1

    o.write('[' + str(time) + 's](' + links[i] + '?t=' + str(time) + '): ' + path + '<br>\n')

f.close()
o.close()
