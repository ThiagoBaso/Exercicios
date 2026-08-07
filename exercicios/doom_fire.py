import shutil
import random
import time

PALETTE = " .,:;#9B&@"
INTENSITY = 9

def update_fire(fire, height, width):
    for y in range(1,height):
        for x in range(1,width+1):
            v = (x-1)+((y-1)*width)
            offset = random.randint(-1,1)
            v2 = min(max(width*y,v+width+offset), width*y + width - 1)
            
            fire[v] = max(0, fire[v2] + random.randint(-1,0))

def render_fire():

    size = shutil.get_terminal_size()
    width = size.columns
    height = size.lines

    fire = [0] * (width * height)

    for x in range(width):
        fire[(height - 1) * width + x] = INTENSITY

    while True:
        time.sleep(0.02)
        print('\x1b[H', end='')

        update_fire(fire, height, width)

        for y in range(1,height+1):
            for x in range(1,width+1):
                
                v = fire[(x-1)+((y-1)*width)]
                #print(v if v > 0 else ' ', end='')
                print(PALETTE[v], end='')
            print('\n')

render_fire()
