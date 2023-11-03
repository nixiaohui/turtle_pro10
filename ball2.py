# 项目6：听话的小球 
import turtle
import time

# 绘制小球
def draw_ball(x, y, edge, bgcolor='#E74C3C'):
    turtle.goto(x, y)
    turtle.dot(edge, bgcolor)

# 获取小球的方向，根据方向返回文本
def get_dir():
    if dx == 1 and dy == 0: return '右'
    if dx == -1 and dy == 0: return '左'
    if dx == 0 and dy == 1: return '上'
    if dx == 0 and dy == -1: return '下'
# 绘制左上角的提示信息
def draw_tips():
    turtle.goto(-w/2+10, h/2-140)
    msg = f"当前坐标：({x:<3}, {y:<3})\n当前速度：{speed:2}\n当前方向：{get_dir()}\n"
    msg += '按下方向键↑↓←→进行改变方向\n'
    msg += '按下减号-降速，按下+号提速(最低速2,最高速10)\n'
    msg += '按1挂1档(低速),按2挂2档(中速),按3按3档(高速)\n'
    msg += '按下空格键暂停'
    turtle.write(msg, 0, 'left', ('黑体', 14))
# 改变方向
def turn_dir(d1, d2):
    global dx, dy, pause
    dx, dy = d1, d2
    pause = (0, 0)
# turtle键盘事件响应三步骤
# 1 创建一个键盘事件处理函数
# 根据上下左右键来改变方向的处理函数
def move_up():
    turn_dir(0, 1)
def move_down():
    turn_dir(0, -1)
def move_left():
    turn_dir(-1, 0)
def move_right():
    turn_dir(1, 0)
# 2 绑定键盘事件-处理函数
turtle.onkey(move_up, 'Up')
turtle.onkey(move_down, 'Down')
turtle.onkey(move_left, 'Left')
turtle.onkey(move_right, 'Right')
# 停止移动
def stop():
    global dx, dy, pause
    (dx, dy), pause = pause, (dx, dy)
# 提升速度
def speed_up():
    global speed
    speed += 2
    if speed >= 10: speed = 10
# 降低速度
def speed_down():
    global speed
    speed -= 2
    if speed <= 2: speed = 2
turtle.onkey(speed_up, 'equal')
turtle.onkey(speed_down, 'minus')
turtle.onkey(stop, 'space')
# 设置速度
def set_speed(spd):
    global speed
    speed = spd
# 按1、2、3进行速度设置的处理函数
def speed_max():
    set_speed(10)
def speed_mid():
    set_speed(6)
def speed_min():
    set_speed(2)
turtle.onkey(speed_max, '3')
turtle.onkey(speed_mid, '2')
turtle.onkey(speed_min, '1')
# 3 启动监听
turtle.listen()

# 基础设置
w, h = 800, 600  # 窗口宽、高
x, y = 0, 0      # 起始位置
speed = 5        # 起始速度
dx, dy = -1, 0   # 起始运动方向：向左
s = 50           # 小球的直径
pause = (0, 0)   # 暂停时的运动方向

turtle.title('听话的小球 by 灰灰老师')  # 设置窗口标题
turtle.setup(w, h)                    # 设置窗口宽高
turtle.tracer(0)                      # 设置不跟踪绘制过程
turtle.hideturtle()                   # 隐藏海龟
turtle.up()                           # 抬起画笔

# 动画的主循环
while True:
    turtle.clear()  # 清空画布
    # 根据移动方向dx\dy与移动速度speed来更新x、y
    x = x + dx*speed
    y = y + dy*speed
    # 判断小球如果到达边缘，就改变移动方向
    if x+s/2 >= w/2 or x-s/2 <= -w/2:
        dx = -dx
    if y+s/2 >= h/2 or y-s/2 <= -h/2:
        dy = -dy
    draw_ball(x, y, s)   # 绘制小球
    draw_tips()          # 绘制提示信息
    turtle.update()      # 更新绘制结果
    time.sleep(0.01)     # 等待0.01秒
