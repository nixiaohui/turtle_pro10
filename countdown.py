from turtle import *
import time

hideturtle()
counter = 10

for i in range(counter):
    write(counter, align='center', font=('楷体', 120, 'bold'))
    counter -= 1
    time.sleep(1)
    clear()

color('red')
write('BOOM!!!', align='center', font=('楷体', 80, 'bold'))
done()
