import turtle
import random
from settings import *
from tools import *

def build_fruits(cnt=5):
    while cnt:
        flag = 1
        row = random.randint(1, row_num-2)
        col = random.randint(1, col_num-2)
        cl = random.randint(0, len(colors['fruits'])-1)
        for fr,fc,fcl in fruits:
            if row == fr and col == fc:
                flag = 0
                break
        if (row, col) in snakes or (row, col) in walls[level-1]:
            flag = 0
        if flag:
            fruits.append((row, col, cl))
            cnt-=1

def draw_border():
    turtle.pencolor(colors['gray'])
    turtle.goto(tx, ty)
    turtle.down()
    for i in range(2):
        turtle.fd(s*col_num)
        turtle.rt(90)
        turtle.fd(s*row_num)
        turtle.rt(90)
    turtle.up()
def draw_bg():
    for row in range(row_num):
        for col in range(col_num):
            turtle.goto(tx+col*s, ty-row*s)
            draw_rect(s, colors['bg'][row%2==col%2])

def draw_snake_head(x, y):
    turtle.goto(x+1, y-1)
    draw_rect(s-1, colors['snake'][1], colors['snake'][1])
    if directions['dx'] == 0 and directions['dy'] == -1:
        x1, y1 = x+s/5, y-s/5
        x2, y2 = x+s*3/5, y-s/5
    elif directions['dx'] == 0 and directions['dy'] == 1:
        x1, y1 = x+s/5, y-s*3/5
        x2, y2 = x+s*3/5, y-s*3/5
    elif directions['dx'] == -1 and directions['dy'] == 0:
        x1, y1 = x+s/5, y-s/5
        x2, y2 = x+s/5, y-s*3/5
    else:
        x1, y1 = x+s*3/5, y-s/5
        x2, y2 = x+s*3/5, y-s*3/5
    turtle.goto(x1, y1)
    draw_rect(s/5, colors['snake'][1])
    turtle.goto(x2, y2)
    draw_rect(s/5, colors['snake'][1])

def draw_snakes():
    for i in range(len(snakes)-1):
        r, c = snakes[i]
        turtle.goto(tx+c*s+1, ty-r*s-1)
        draw_rect(s-1, colors['snake'][0], colors['snake'][0])
    r, c = snakes[-1]
    draw_snake_head(tx+c*s, ty-r*s)

# 绘制墙体（障碍物）
def draw_wall(x, y, bgcolor=colors['walls'][0]):
    turtle.goto(x, y)
    draw_rect(s, bgcolor, bgcolor)               # 绘制一个正方形
    # 通过绘制一些竖线和横线，让墙看起来像用砖头组成的样子
    turtle.pencolor(colors['white'])
    for i in range(0, 4):
        turtle.goto(x, y-s*i/3)
        turtle.down()
        turtle.goto(x+s, y-s*i/3)
        turtle.up()
    if (y - ty)//s % 2:
        pts = [(0, 2), (1, 1), (2, 2)]
    else:
        pts = [(0, 1), (1, 2), (2, 1)]
    for j, i in pts:
        turtle.goto(x+s*i/3, y-j*s/3)
        turtle.down()
        turtle.goto(x+s*i/3, y-(j+1)*s/3)
        turtle.up()

def draw_walls():
    for wr, wc in walls[level-1]:
        draw_wall(tx+wc*s, ty-wr*s)

def draw_fruits():
    for r,c,cl in fruits:
        turtle.goto(tx+c*s, ty-r*s)
        draw_rect(s, colors['fruits'][cl])

def draw_tips():
    turtle.pencolor(colors['tips'][0])
    turtle.goto(tx, ty+s//3)
    turtle.write('得分：'+str(total_score), 0, 'left', ('黑体', 20))
    turtle.goto(0, ty+s//3)
    turtle.write('第'+str(level)+'关', 0, 'center', ('楷体', 30))
    turtle.goto(0, -2.5*s)
    if status == -1:
        turtle.write('Game Over', 0, 'center', ('Arial Black', 100))
    elif status == 2:
        turtle.write('You Win', 0, 'center', ('Arial Black', 100))
    elif count_down > 0:
        turtle.write(count_down, 0, 'center', ('Arial Black', 140, 'bold'))
    elif count_down == 0:
        turtle.write('Go', 0, 'center', ('Arial Black', 140))
    elif pause:
        turtle.write('PAUSE', 0, 'center', ('Arial Black', 140))

    turtle.color(colors['white'])

def collision():
    global score, total_score
    sr, sc = snakes[-1]
    eated = None
    for fr, fc, fcl in fruits:
        if fr == sr and fc == sc:
            eated = (fr, fc, fcl)
            break
    if eated and eated in fruits:
        fruits.remove(eated)
        score += 1
        play_get_coin()
        total_score += 1
    if len(fruits) == 0:
        build_fruits(5)
    if eated: return True
    else: return False

def load_map():
    global score, speed, count_down
    count_down = 4
    score = 0
    speed = (5-level)*100
    fruits.clear()
    build_fruits()
    snakes.clear()
    snakes.append((2, 2))
    directions['dx'] = 1
    directions['dy'] = 0

def restart():
    global status, count_down, total_score
    total_score -= score
    status = 1
    load_map()
    cd()
    run()

def next_level():
    global score, level, speed, status
    if score >= level*nxt_level_score:
        level += 1
        if level > len(walls):
            status = 2
            level -= 1
            play_win()
            return
        load_map()
        cd()
        play_next_level()

def moving():
    global status
    sr, sc = snakes[-1]
    sr += directions['dy']
    sc += directions['dx']
    if sr < 0 or sr > row_num-1 or sc < 0 or sc > col_num-1:
        status = -1
        play_sound()
        return
    if (sr, sc) in snakes or (sr, sc) in walls[level-1]:
        status = -1
        play_sound()
        return
    snakes.append((sr, sc))
    if not collision():
        snakes.pop(0)

def move_up():
    directions['dx'] = 0
    directions['dy'] = -1
def move_down():
    directions['dx'] = 0
    directions['dy'] = 1
def move_left():
    directions['dx'] = -1
    directions['dy'] = 0
def move_right():
    directions['dx'] = 1
    directions['dy'] = 0

def change_pause():
    global pause
    pause = not pause

def cd():
    global count_down
    count_down -= 1
    if count_down < 0:
        return
    turtle.ontimer(cd, 1000)

def init():
    turtle.title('贪吃蛇 by 灰灰老师')
    turtle.setup(w, h)
    turtle.tracer(0)
    turtle.hideturtle()
    turtle.up()
    turtle.onkey(move_up, 'Up')
    turtle.onkey(move_down, 'Down')
    turtle.onkey(move_left, 'Left')
    turtle.onkey(move_right, 'Right')
    turtle.onkey(change_pause, 'space')
    turtle.onkeypress(volume_down, '-')
    turtle.onkeypress(volume_up, '=')
    turtle.onkey(restart, 'r')
    turtle.listen()
    load_sound()
    play_bgm()
    load_map()
    cd()

def run():
    turtle.clear()
    if not pause and status == 1 and count_down == -1:
        moving()
        next_level()
    # draw_border()
    draw_bg()
    draw_snakes()
    draw_fruits()
    draw_walls()
    draw_tips()
    turtle.update()
    if status != 1: return
    turtle.ontimer(run, speed)

def main():
    init()
    run()
    turtle.done()
