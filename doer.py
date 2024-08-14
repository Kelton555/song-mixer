from pydub import AudioSegment

segmentSize = 5000000

metadata = {}

file = open('data.txt', 'r')
cur = ''
nextIsFile = False
for line in file:
    if line[0] in '/#*\\ \t': # ignore comments
        continue 
    elif line[0] == '-':
        print(line) # treat dashes as printed comments, e.g. a todo list
        continue

    line = line.rstrip()
    if line.startswith('[') and line.endswith(']'):
        cur = line[1:-1]
        if not cur in metadata:
            nextIsFile = True
            metadata[cur] = {'timestamps': [], 'name': cur}
        continue
    
    if nextIsFile:
        fileData = line.split(':')
        if len(fileData) == 2:
            nextIsFile = False
            metadata[cur]['filename'] = fileData[0]
            metadata[cur]['filetype'] = fileData[1]
    else:
        data = line.split(':')
        if len(data) == 3:
            metadata[cur]['timestamps'].append({'start': int(data[0]), 'end': int(data[2]), 'embed': data[1]})
        elif len(data) == 4:
            metadata[cur]['timestamps'].append({'start': int(data[0]), 'end': int(data[2]), 'embed': data[1], 'cutin': int(data[3])})

file.close()

errored = False
for k in metadata: # check for linking errors now rather than waiting for one to crop up halfway through the process
    for cutaway in metadata[k]['timestamps']:
        if cutaway['embed'] not in metadata:
            print('Error: Cutaway to nonexistant track "' + cutaway['embed'] + '"')
            errored = True # don't immediately exit so that all errors can be printed before terminating

if errored:
    exit(1)

log = open('log.txt', 'w')

audio = AudioSegment.empty()
nextSegment = 0

def saveFragment():
    global audio
    global nextSegment
    global segmentSize

    if len(audio) > segmentSize:
        audio[:segmentSize+1].export('outputs/output' + str(nextSegment) + '.wav', format="wav")
        audio = audio[segmentSize+1:]
        nextSegment = nextSegment + 1
    else:
        audio.export('outputs/output' + str(nextSegment) + '.wav', format="wav")
        audio = AudioSegment.empty()
        nextSegment = nextSegment + 1


def writeLog(stack):
    global audio
    global segmentSize
    global nextSegment

    if len(stack) == 0:
        return # no need for an empty line, trust the process

    log.write(str(len(audio) + nextSegment*segmentSize)) # i hope this isn't an off by one or i'm gonna be clowned so unbelievably hard
    log.write(': ')

    write = ''
    for song in stack:
        write = write + song + ' > '
    write = write[:-3]

    log.write(write)
    log.write('\n')

    print(str(len(audio) + nextSegment*segmentSize) + ': ' + write)
        

def handleSong(song, playingStack, cutin=0):
    global audio # coming from lua, python is so stupid sometimes
    global segmentSize

    playingStack.append(song)
    writeLog(playingStack)

    song = metadata[song]
    songAudio = AudioSegment.from_file(song['filename'], song['filetype']) #

    if len(song['timestamps']) == 0:
        audio = audio + songAudio
        playingStack.pop()
        writeLog(playingStack)
        if len(audio) > segmentSize:
            saveFragment()
        return

    i = -1
    lastCutaway = -1
    for cutaway in song['timestamps']:
        i = i + 1
        if cutaway['embed'] in playingStack:
            continue # avoid recursion
        elif cutaway['start'] < cutin:
            continue # avoid doing cutaways in a cut part of the song
        else:
            if lastCutaway == -1: # if first cutaway, start from cutin point (defaults to beginning)
                audio = audio + songAudio[cutin:cutaway['start']]
            else: # otherwise, start from last dropoff point
                if song['timestamps'][lastCutaway]['end'] <= cutaway['start']:
                    audio = audio + songAudio[song['timestamps'][lastCutaway]['end']:cutaway['start']]
                else:
                    print('AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH FIRE FIRE FIRE FIRE FIRE I REPEAT FIRE FIRE FIRE FIRE FIRE BAD THINGS HAVE HAPPENED SOMETHINGS ON FIRE AHHHHHHHHHHHHHHHHHHHHHHHHHHH')

            if 'cutin' in cutaway:
                handleSong(cutaway['embed'], playingStack, cutaway['cutin'])
            else:
                handleSong(cutaway['embed'], playingStack)

            lastCutaway = i
    
    if lastCutaway == -1:
        audio = audio + songAudio[cutin:]
    else:
        audio = audio + songAudio[song['timestamps'][lastCutaway]['end']:]
    
    playingStack.pop()
    writeLog(playingStack)
    if len(audio) > segmentSize:
        saveFragment()


# main loop
for song in metadata:
    handleSong(song, [])

log.write(str(len(audio) + nextSegment*segmentSize))
log.write(': END')
log.close()

while len(audio) > 0:
    saveFragment()