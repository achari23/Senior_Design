import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import u_sensor
import time
import time
import copy
import rcpy 
import rcpy.motor as motor
import rcpy.mpu9250 as mpu9250


def in_and_write():
    while True: 
        font = ImageFont.load_default()
        RST = 'GP0_6'
        disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
        disp.begin()
        disp.clear()
        disp.display()
        width = disp.width
        height = disp.height
        image = Image.new('1', (width, height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        padding = -2
        top = padding
        bottom = height-padding
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        x = 0
        draw.text((x, top), "Enter the",  font=font, fill=255)
        draw.text((x, top + 8), "distance to travel",  font=font, fill=255)
        draw.text((x, top+ 16), "forward in feet",  font=font, fill=255)
        draw.text((x, top+ 24), "then press #",  font=font, fill=255)
        disp.image(image)
        disp.display()
        y = 0
        while True:
            z = get_key()
            
            if z == '#':
                break
            if z == 'A' or z == 'B' or z == 'C' or z == 'D':
                continue
            y *= 10
            y += z
        disp.clear()
        disp.display()
        width = disp.width
        height = disp.height
        image = Image.new('1', (width, height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        padding = -2
        top = padding
        bottom = height-padding
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        x = 0
        draw.text((x, top), "Confirm that",  font=font, fill=255)
        draw.text((x, top + 8), "distance to travel",  font=font, fill=255)
        draw.text((x, top+ 16), "forward in feet",  font=font, fill=255)
        draw.text((x, top+ 24), "is " + str(y),  font=font, fill=255)
        disp.image(image)
        disp.display()
        
        time.sleep (3)
        
        disp.clear()
        disp.display()
        width = disp.width
        height = disp.height
        image = Image.new('1', (width, height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        padding = -2
        top = padding
        bottom = height-padding
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        x = 0
        draw.text((x, top), "Enter the",  font=font, fill=255)
        draw.text((x, top + 8), "distance to travel",  font=font, fill=255)
        draw.text((x, top+ 16), "right in feet",  font=font, fill=255)
        draw.text((x, top+ 24), "then press #",  font=font, fill=255)
        disp.image(image)
        disp.display()
        corrd_x = 0
        while True:
            z = get_key()
            
            if z == '#':
                break
            if z == 'A' or z == 'B' or z == 'C' or z == 'D':
                continue
            corrd_x *= 10
            corrd_x += z
        disp.clear()
        disp.display()
        width = disp.width
        height = disp.height
        image = Image.new('1', (width, height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        padding = -2
        top = padding
        bottom = height-padding
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        x = 0
        draw.text((x, top), "Confirm that",  font=font, fill=255)
        draw.text((x, top + 8), "distance to travel",  font=font, fill=255)
        draw.text((x, top+ 16), "right in feet",  font=font, fill=255)
        draw.text((x, top+ 24), "is " + str(corrd_x),  font=font, fill=255)
        disp.image(image)
        disp.display()
        
        time.sleep(3)
        
        disp.clear()
        disp.display()
        width = disp.width
        height = disp.height
        image = Image.new('1', (width, height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        padding = -2
        top = padding
        bottom = height-padding
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        x = 0
        draw.text((x, top), "distance forward: " + str(y),  font=font, fill=255)
        draw.text((x, top + 8), "distance right: " + str(corrd_x),  font=font, fill=255)
        draw.text((x, top+ 16), "# to start",  font=font, fill=255)
        draw.text((x, top+ 24), "* to cancel" ,  font=font, fill=255)
        disp.image(image)
        disp.display()
        while True:
            if get_key() == '#':
                disp.clear()
                disp.display()
                width = disp.width
                height = disp.height
                image = Image.new('1', (width, height))
                draw = ImageDraw.Draw(image)
                draw.rectangle((0,0,width,height), outline=0, fill=0)
                disp.image(image)
                disp.display()
                return corrd_x, y
            if get_key() == '*':
                break
    
def get_key():
    ADC.setup()
    new = 21
    prev_val = 21
    while(1):
        time.sleep(.3)
        
        x = int((ADC.read("AIN0") / 1.78) * 512)
        y = int((ADC.read("AIN1") / 1.78) * 512)
        w = int((ADC.read("AIN2") / 1.78) * 512)
        z = int((ADC.read("AIN3") / 1.78) * 512)
    
        if (x and not y and not w and not z):
            if (x < 6): 
              
                prev_val = 'A'
            elif (x < 10): 
                
                prev_val = 'B'
            elif (x < 18): 
                
                prev_val = 'C'
            else: 
                
                prev_val = 'D'
        elif(not x and y  and not w and not z):
            if (y < 6): 
                
                prev_val = 3
            elif (y < 10): 
              
                prev_val = 6
            elif (y < 18): 
              
                prev_val = 9
            else: 
                
                prev_val = '#'
        elif(not x and not y  and w and not z):
            if (w < 6): 
                
                prev_val = 2
            elif (w < 10): 
                
                prev_val = 5
            elif (w < 18): 
                
                prev_val = 8
            else:
                
                prev_val = 0
        elif(not x and not y  and not w and z):
            if (z < 6): 
               
                prev_val = 1
            elif (z < 10): 
               
                prev_val = 4
            elif (z < 18): 
                
                prev_val = 7
            else: 
               
                prev_val = '*'
        
        if new  != prev_val:
            print(prev_val)
            return prev_val
        elif(not x and not y  and not w and not z):
            prev_val = 21
        
        new = prev_val

def turn_right():
    d = -1 * .6 # d + direction * delta
    motor.set(1, -1 * d)
    motor.set(2, -1* d)
    motor.set(3, d)
    motor.set(4, d)
    
    data = mpu9250.read()
    start = time.time()
    deg = 0
    
    while True:
        data = mpu9250.read()
        deg += (.1) * abs(data['gyro'][2]) /.75
        print((data['gyro'][2]))
        if abs(deg) >= 90:
            
            motor.set(1, 0)
            motor.set(2, 0)
            motor.set(3, 0)
            motor.set(4, 0)
            break
        time.sleep(.1)
    
def turn_left():
    d = .6 # d + direction * delta
    motor.set(1, -1 * d)
    motor.set(2, -1* d)
    motor.set(3, d)
    motor.set(4, d)
    
    data = mpu9250.read()
    start = time.time()
    deg = 0
    
    while True:
        data = mpu9250.read()
        deg += (.1) * abs(data['gyro'][2]) /.75
        print((data['gyro'][2]))
        if abs(deg) >= 90:
            
            motor.set(1, 0)
            motor.set(2, 0)
            motor.set(3, 0)
            motor.set(4, 0)
            break
        time.sleep(.1)
 

    
def move_forward(rover, orientation):
    d =  1 * .4 # d + direction * delta
    motor.set(1, d)
    motor.set(2, d)
    motor.set(3, d)
    motor.set(4, d)
    time.sleep(.26)
    motor.set(1, 0)
    motor.set(2, 0)
    motor.set(3, 0)
    motor.set(4, 0)
    
def move_forward_long():
    d =  1 * .4 # d + direction * delta
    motor.set(1, d)
    motor.set(2, d)
    motor.set(3, d)
    motor.set(4, d)
    time.sleep(.5)
    motor.set(1, 0)
    motor.set(2, 0)
    motor.set(3, 0)
    motor.set(4, 0)

#check distance too close
def obj_ahead():
    x = u_sensor.Measurement
    vcc = "5V"
    # white wire
    trig = "GP1_3" #3_2
    trigger = trig
    # blue wire using resistor
    echo = "GP1_4" #3_1
    # black wire
    gnd = "GND"
   # GPIO.setwarnings(False)
    
    # use default temp of 20 Celcius
    distance_warm = x.basic_distance(trig, echo)
    
    
    if distance_warm < 10:
        return 1
    return 0
def check_mag(start):
    #rcpy.set_state(rcpy.RUNNING)
    #mpu9250.initialize(enable_magnetometer = True)
    temp = mpu9250.read_imu_temp()
    data = mpu9250.read()
    print(start)
    print(data['mag'][2])
    if abs(data['mag'][2] - start) > 60:
        return 1
    return 0

def make_sound():
    gnd = 'GPIO1_17'
    switch = 'GP0_5'
    #vcc = '5V'
    GPIO.setup(gnd,GPIO.OUT)
    GPIO.setup(switch, GPIO.OUT)
    GPIO.output(gnd, GPIO.LOW)
    
    start = time.time()
    while(time.time() - start < 1):
        GPIO.output(switch, GPIO.HIGH)
        time.sleep(.000001)
        GPIO.output(switch, GPIO.LOW)
        time.sleep(.000001)
    start = time.time()
    time.sleep(.5)
    while(time.time() - start < 2):
        GPIO.output(switch, GPIO.HIGH)
        time.sleep(.000001)
        GPIO.output(switch, GPIO.LOW)
        time.sleep(.000001)
    start = time.time()
    time.sleep(.5)
    while(time.time() - start < 2):
        GPIO.output(switch, GPIO.HIGH)
        time.sleep(.000001)
        GPIO.output(switch, GPIO.LOW)
        time.sleep(.000001)
    

def search(x):
    cover = sum(sum(x,[]))
    return cover / (len(x) * len(x[0]))
    
GPIO.setwarnings(False)

#print(__name__)
rcpy.set_state(rcpy.RUNNING)
mpu9250.initialize(enable_magnetometer = True)
#wait for imu init
while rcpy.get_state() != rcpy.RUNNING:
    pass
temp = mpu9250.read_imu_temp()
data = mpu9250.read()
start = data['mag'][2]
print(start)
count = 5
rover = [0,0]
metal = []
x, y = in_and_write()
area = [[0]*(int(x*4)) for _ in range(int(y*4))] 
print(len(area)) # is y direction
print(len(area[0])) # is x direction

freq_area = copy.deepcopy(area)
orientation = 0 # 0 up, 1 rightwards, 2 down, 3 leftwards
# returns which side of the area is less traveled, right or left
def right_or_left(area, mid, orientation):
    right_sum = 0
    left_sum = 0
    for y in range(len(area)):
        for x in range(len(area[0])):
            if x < mid: 
                left_sum += area[y][x]
            elif x > mid:
                right_sum += area[y][x]
    if mid == 0:
        return 'r'
    if mid == len(area[0]):
        return 'l'
    if (right_sum / (len(area) * (len(area[0]) - mid))) < (left_sum / (len(area) * mid)):
        return 'r'
    else:
        return 'l'
    
# returns which side of the area is less traveled, up or down
def up_or_down(area, mid, orientation):
    top_sum = 0
    down_sum = 0
    for y in range(len(area), orientation):
        for x in range(len(area[0])):
            if y < mid: 
                down_sum += area[y][x]
            elif y > mid:
                top_sum += area[y][x]
    if mid == 0:
        return 't'
    if mid == len(area):
        return 'd'
    if (top_sum / (len(area[0]) * (len(area) - mid))) < (down_sum/ (len(area[0]) * mid)):
        return 't'
    else:
        return 'd'
        
def make_motion_decision(area, freq_area, rover, orientation): 
    if orientation == 0:
        if (rover[0] + 1 < len(area) and area[rover[0] + 1][rover[1]] == 0):
            return orientation
        elif(rover[0] + 1 == len(area) or area[rover[0] + 1][rover[1]] == 1):
            if (rover[1] + 1< len(area[0]) and area[rover[0]][rover[1] + 1] == 0):
                turn_right()
                return 1
            elif (rover[1] - 1 > 0 and area[rover[0]][rover[1] - 1] == 0):
                turn_left()
                return 3
            else: 
                return 4
                
    elif orientation == 1: 
        if (rover[1] + 1 < len(area[0]) and area[rover[0]][rover[1] + 1] == 0):
            return orientation
        elif(rover[1] + 1 == len(area[0]) or area[rover[0]][rover[1] + 1] == 1):
            if (rover[0] + 1< len(area) and area[rover[0] + 1][rover[1]] == 0):
                turn_left()
                return 0
            elif (rover[0] - 1 > 0 and area[rover[0] - 1][rover[1]] == 0):
                turn_right()
                return 2
            else: 
                return 4
        
    elif orientation == 2: 
        if (rover[0] - 1 > 0 and area[rover[0] - 1][rover[1]] == 0):
            return orientation
        elif(rover[0] - 1 == 0 or area[rover[0] - 1][rover[1]] == 1):
            if (rover[1]  + 1< len(area[0]) and area[rover[0]][rover[1] + 1] == 0):
                turn_left()
                return 1
            elif (rover[1] - 1> 0 and area[rover[0]][rover[1] - 1] == 0):
                turn_right()
                return 3
            else: 
                return 4
    elif orientation == 3: 
        if (rover[1] - 1 > 0 and area[rover[0]][rover[1] - 1] == 0):
            return orientation
        elif(rover[1] - 1 == 0 or area[rover[0]][rover[1] - 1] == 1):
            if (rover[0] + 1< len(area) and area[rover[0] + 1][rover[1]] == 0):
                turn_right()
                return 0
            elif (rover[0] - 1 > 0 and area[rover[0] - 1][rover[1]] == 0):
                turn_left()
                return 2
            else: 
                return 4
    return orientation

def check_area(area, rover, orientation):
    x  = rover[1]
    y = rover[0]
    if orientation == 0:
        if rover[1] == 0:
            turn_right()
            return 1
        elif(rover[1] == len(area[0])):
            turn_left()
            return 3
        right = 0
        left = 0
        space_r = 1
        space_l = 1
        for y1 in range(len(area)): 
            for x1 in range(len(area[0])):
                if x1 > x:
                    right += area[y1][x1]
                    space_r += 1
                elif x1 < x:
                    left += area[y1][x1]
                    space_l += 1
        if right/space_r < left/space_l:
            turn_right()
            orientation = 1
        elif right/space_r > left/space_l:
            turn_left()
            orientation = 3
    elif orientation == 2:
        if rover[1] == 0:
            turn_left()
            return 1
        elif(rover[1] == len(area[0])):
            turn_right()
            return 3
        right = 0
        left = 0
        space_r = 1
        space_l = 1
        for y1 in range(len(area)): 
            for x1 in range(len(area[0])):
                if x1 < x:
                    right += area[y1][x1]
                    space_r += 1
                elif x1 > x:
                    left += area[y1][x1]
                    space_l += 1
        if right/space_r < left/space_l:
            turn_right()
            orientation = 3
        elif right/space_r > left/space_l:
            turn_left()
            orientation = 1
    elif orientation == 1:
        if rover[0] == 0:
            turn_right()
            return 2
        elif(rover[0] == len(area)):
            turn_left()
            return 0
        right = 0
        left = 0
        space_r = 1
        space_l = 1
        for y1 in range(len(area)): 
            for x1 in range(len(area[0])):
                if y1 < y:
                    right += area[y1][x1]
                    space_r += 1
                elif y1 > y:
                    left += area[y1][x1]
                    space_l += 1
        if right/space_r < left/space_l:
            turn_right()
            orientation = 2
        elif right/space_r > left/space_l:
            turn_left()
            orientation = 0
    elif orientation == 3:
        if rover[0] == 0:
            turn_left()
            return 0
        elif(rover[0] == len(area)):
            turn_right()
            return 2
        right = 0
        left = 0
        space_r = 1
        space_l = 1
        for y1 in range(len(area)): 
            for x1 in range(len(area[0])):
                if y1 < y:
                    right += area[y1][x1]
                    space_r += 1
                elif y1 > y:
                    left += area[y1][x1]
                    space_l += 1
        if right/space_r < left/space_l:
            turn_right()
            orientation = 0
        elif right/space_r > left/space_l:
            turn_left()
            orientation = 2
    return orientation
        
while(search(area) < .8):
    #update area map and frequency map
    area[rover[0]][rover[1]] = 1

    freq_area[rover[0]][rover[1]] += 1
    #count makes sure the rover doesn't hit the same place twice
    count += 1
    #check magnets
    if check_mag(start) and count > 5:
        metal.append([rover[0], rover[1]])
        count = 0 
        make_sound()
    #move_forward(rover,orientation)
    if(obj_ahead()):
        orientation = check_area(area, rover, orientation)
    else: 
        orientation = make_motion_decision(area, freq_area, rover, orientation)
        move_forward(rover, orientation)
        if orientation == 0:
            rover[0] += 1
        elif orientation == 1:
            rover[1] += 1
        elif orientation == 2:
            rover[0] -= 1
        elif orientation == 3:
            rover[1] -= 1
        elif orientation == 4:
            break
    
    for x in area: 
        print(x)
    
    
    
while orientation != 2:
    turn_right()
    orientation += 1
    orientation %= 4
    time.sleep(.3)
while rover[0] >= 0:
    move_forward(rover, orientation)
    rover[0] -= 1
turn_right()
while rover[1] >= 0:
    move_forward(rover, orientation)
    rover[1] -= 1
    print(rover[1])
if len(metal) == 0:
    font = ImageFont.load_default()
    RST = 'GP0_6'
    disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
    disp.begin()
    disp.clear()
    disp.display()
    width = disp.width
    height = disp.height
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    padding = -2
    top = padding
    bottom = height-padding
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    x = 0
    draw.text((x, top), "No Metal Found",  font=font, fill=255)
    disp.image(image)
    disp.display()
    time.sleep(10)
else:
    font = ImageFont.load_default()
    RST = 'GP0_6'
    disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
    for m in metal:
        disp.begin()
        disp.clear()
        disp.display()
        width = disp.width
        height = disp.height
        image = Image.new('1', (width, height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        padding = -2
        top = padding
        bottom = height-padding
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        x = 0
        draw.text((x, top), "Metal Found At",  font=font, fill=255)
        draw.text((x, top + 8), "y: " + str(m[0] * 3) + " inches", font = font, fill = 255)
        draw.text((x, top + 16), "x: " + str(m[1] * 3) + " inches", font = font, fill = 255)
        draw.text((x, top + 24), "Press #", font = font, fill = 255)
        
        disp.image(image)
        disp.display()
        while get_key() != '#':
            continue
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)
padding = -2
top = padding
bottom = height-padding
draw.rectangle((0,0,width,height), outline=0, fill=0)
x = 0
draw.text((x, top), "Thanks for using",  font=font, fill=255)
draw.text((x, top + 8), "Team 33's", font = font, fill = 255)
draw.text((x, top + 16), "Autonomous Metal", font = font, fill = 255)
draw.text((x, top + 24), "Detector!", font = font, fill = 255)
    
disp.image(image)
disp.display()

time.sleep(10)

disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)
padding = -2
top = padding
bottom = height-padding
draw.rectangle((0,0,width,height), outline=0, fill=0)
x = 0
draw.text((x, top), "Laura Kelsey",  font=font, fill=255)
draw.text((x, top + 8), "Alyssa DeLouise", font = font, fill = 255)
draw.text((x, top + 16), "Tim Diemer", font = font, fill = 255)
draw.text((x, top + 24), "Anand Chari", font = font, fill = 255)
    
disp.image(image)
disp.display()

time.sleep(10)