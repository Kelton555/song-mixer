import math

f = open('log.txt', 'r')
o = open('newtimestamps.txt', 'w')

for line in f:
    line = line.strip().split(':')
    time = math.floor(int(line[0].strip())/1000)
    path = line[1].strip()

    timestr = ""
    if (time < 60):
        timestr = "0:"
        if (time < 10):
            timestr += "0"
        timestr += str(time)
    elif (time < (60*60)):
        minutes = math.floor(time/60)
        seconds = time % 60

        timestr = str(minutes) + ":"
        if (seconds < 10):
            timestr += "0"
        timestr += str(seconds)
    else:
        hours = math.floor(time/(60*60))
        minutes = math.floor(time/60) % 60
        seconds = time % 60

        timestr = str(hours) + ":"

        if (minutes < 10):
            timestr += "0"
        timestr += str(minutes) + ":"

        if (seconds < 10):
            timestr += "0"
        timestr += str(seconds)
    o.write(timestr + " - " + path + "\n")

f.close()
o.close()