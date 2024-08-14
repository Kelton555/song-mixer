import cv2

fps = 25

out = cv2.VideoWriter('outputVideo.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (1920, 1080))

imageLookup = {}

f = open('interlinks.txt', 'r')

for line in f:
    line = line.strip().split(':')
    imageLookup[line[1]] = 'images/' + line[0] + '.png'

f.close()

f = open('log.txt', 'r')

msperframe = 1000/fps
currentms = 0
currentImage = None
firstImage = True
for line in f:
    print(line)
    if firstImage:
        currentImage = cv2.imread(imageLookup[line.split(':')[1].strip()])
        firstImage = False
        continue
    
    ms = int(line.split(':')[0])
    while currentms <= ms:
        out.write(currentImage)
        currentms = currentms + msperframe

    path = line.split(':')[1].strip()
    if path in imageLookup:
        currentImage = cv2.imread(imageLookup[path])

f.close()

out.release()