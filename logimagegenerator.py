from PIL import Image, ImageDraw, ImageFont

f = open('log.txt', 'r')

trees = {}

for line in f:
    line = line.split(':')[1].strip()
    trees[line] = True
f.close()

if 'END' in trees:
    del trees['END']

f = open('parsed.txt', 'w')

for key in trees:
    f.write(key)
    f.write('\n')

f.close()

font = ImageFont.truetype('arial.ttf', size=75)

f = open('interlinks.txt', 'w')

i = 0
for key in trees:
    image = Image.new("RGB", (1920, 1080), 'black')
    draw = ImageDraw.Draw(image)
    j = 0
    k = 0
    for song in key.split(' > '):
        draw.text((j, k), song.strip(), font=font, fill=(255, 255, 255))
        j = j + 60
        k = k + 100
    image.save('images/' + str(i) + '.png')
    f.write(str(i) + ':' + key + '\n')
    i = i + 1

f.close()