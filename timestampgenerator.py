import math

link = 'https://youtu.be/x8Fq1GpMhGU'

f = open('log.txt', 'r')
o = open('timestamps.md', 'w')

for line in f:
    line = line.strip().split(':')
    time = math.floor(int(line[0].strip())/1000)
    path = line[1].strip()

    o.write('[' + str(time) + 's](' + link + '?t=' + str(time) + '): ' + path + '<br>\n')

f.close()
o.close()