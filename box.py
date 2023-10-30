# 推箱子小项目
import turtle

s = 60  # 背景每一个小格子的边长
row = 10   # 背景分成几行
col = 10   # 背景分成几列
width = s*col + 2*s  # 窗口的宽度
height = s*row + 2*s # 窗口的高度
tx = -s*5  # 地图左上角x坐标, 作为地图及各角色的位置基准值
ty = s*5   # 地图左上角y坐标, 作为地图及各角色的位置基准值
boxs = []  # 存储本关所有箱子的行、列的列表
targets = []  # 存储本关所有目标点的行、列的列表
walls = []  # 存储本关所有墙（障碍物）的行、列的列表
prow, pcol = 0, 0  # 玩家所以的位置行和列
win = False # 当前是否胜利
level = 1   # 当前关卡
board = []  # 当前地图
# 所有地图
# ! 1 表示箱子， 2 表示目标点， 4 表示墙， 5 玩家
maps = [
    [#1
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 0, 1, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ],
    [#2
        [0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 1, 0, 0, 1, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 4, 0],
        [0, 2, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ],
    [#3
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 4, 0, 0, 4, 0, 0, 4, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
]

# 初始化设置
def init():
    turtle.title('推箱子小游戏 - by 灰灰老师')
    turtle.setup(width, height) # 设置窗口大小
    turtle.tracer(0)            # 设置不跟踪海龟绘制的过程
    turtle.hideturtle()         # 隐藏海龟
    turtle.up()                 # 抬起画笔

# 绘制一个正方形， edge是边长， bgcolor是背景颜色
def draw_rect(edge, bgcolor):
    turtle.down()               # 落笔
    turtle.fillcolor(bgcolor)   # 设置填充颜色
    turtle.begin_fill()         # 开始填充
    for i in range(4):          # 循环四步，绘制正方形
        turtle.fd(edge)
        turtle.rt(90)
    turtle.end_fill()           # 结束填充
    turtle.up()                 # 抬笔

# 绘制玩家，x,y是玩家坐标


def draw_player(x, y, bgcolor='#F5B041'):
    turtle.goto(x, y)           # 移动到玩家所在的坐标
    draw_rect(s, bgcolor)       # 绘制玩家的外部大正方形
    turtle.goto(x+s/5, y-s/5)   # 移动到玩家左眼睛所在的坐标
    draw_rect(s/5, bgcolor)     # 绘制玩家内部的左眼睛
    turtle.goto(x+s*3/5, y-s/5) # 移动到玩家右眼睛所在的坐标
    draw_rect(s/5, bgcolor)     # 绘制玩家内部的右眼睛

# 绘制箱子
def draw_box(x, y, bgcolor='#5DADE2'):
    turtle.goto(x, y)           # 移动到箱子所在的坐标
    draw_rect(s, bgcolor)       # 绘制箱子的外形，一个正方形
    turtle.down()               # 落笔后绘制一个交叉
    turtle.goto(x+s, y-s)
    turtle.goto(x, y-s)
    turtle.goto(x+s, y)
    turtle.up()                 # 绘制后抬笔

# 绘制目标点
def draw_target(x, y, bgcolor='#7DCEA0'):
    turtle.goto(x+s/2, y-s/2)   
    turtle.dot(s/2, bgcolor)    # 绘制一个小圆点表示目标点

# 绘制墙体（障碍物）
def draw_wall(x, y, bgcolor='#E74C3C'):
    turtle.goto(x, y)
    draw_rect(s, bgcolor)               # 绘制一个正方形
    # 通过绘制一些竖线和横线，让墙看起来像用砖头组成的样子
    for i in range(1,3):                
        turtle.goto(x, y-s*i/3)
        turtle.down()
        turtle.goto(x+s, y-s*i/3)
        turtle.up()
    for j,i in [(0,2),(1,1),(2,2)]:
        turtle.goto(x+s*i/3, y-j*s/3)
        turtle.down()
        turtle.goto(x+s*i/3, y-(j+1)*s/3)
        turtle.up()

# 绘制背景
def draw_bg():
    for j in range(row):   # row行
        for i in range(col): # col列
            if i%2==j%2:           # 设置每个小方格的背景颜色
                c = '#F0F0F0'
            else:
                c = '#E2E2E2'
            # 根据行、列进行y、x方向的偏移
            turtle.goto(tx+i*s, ty-j*s)  
            draw_rect(s, c)         # 绘制背景中的每个小方格

# 从地图中加载当前关卡的各角色的位置数据
def load_board():
    global prow, pcol, boxs, targets, walls, board
    board = maps[level-1] # 初始化当前地图
    boxs = []     # 重置 箱子 列表
    targets = []  # 重置 目标点 列表
    walls = []    # 重置 墙（障碍物） 列表
    for j in range(row):       # 地图board的row行
        for i in range(col):   # 地图board的col列
            if board[j][i] == 1: # 1是箱子
                boxs.append([j, i])
            elif board[j][i] == 2: # 2是目标点
                targets.append([j, i])
            elif board[j][i] == 4: # 4是墙
                walls.append([j, i])
            elif board[j][i] == 5: # 5是玩家
                prow, pcol = j, i

# 绘制各个角色
def draw_elements():
    for r, c in targets:  # 画目标点
        draw_target(tx+c*s, ty-r*s)
    for r, c in boxs:  # 画箱子
        draw_box(tx+c*s, ty-r*s)
    for r, c in walls: # 画墙
        draw_wall(tx+c*s, ty-r*s)
    # 画玩家
    draw_player(tx+pcol*s, ty-prow*s)

# 绘制提示信息
def draw_tips():
    turtle.goto(0, ty-10.5*s)  # 在窗口正下方
    turtle.write('按r键重新开始本关',0,'center',('楷体',20))
    turtle.goto(0, ty)
    if win == True: # 如果游戏的状态为胜利，则显示胜利提示
        turtle.write('You Win', 0, 'center', ('黑体', 40))
    else:   # 如果游戏还没胜利，则显示当前关卡是第几关
        turtle.write(f'第{level}关', 0, 'center', ('黑体', 20))


# 判断是否完成本关
def is_next_level():
    # 如果所有的箱子都和目标点的坐标重合，则本关完成了
    for box in boxs:
        if box not in targets:
            return False
    return True

# 判断是否可以移动
def moving(r1, c1, r2, c2):
    global prow, pcol
    # r1, c1 是下一个点的行、列
    # r2, c2 是下下个点的行、列
    # 如果下一个点出了边界，则不移动
    if r1 < 0 or c1 < 0 or r1 > row-1 or c1 > col-1: return
    if [r1, c1] in walls: return # 如果下一个点是墙，也不移动
    if [r1, c1] in boxs: # 如果下一个点是箱子，则要分情况处理
        # 如果下一个点是箱子，且下下个点出了边界，则不移动
        if r2 < 0 or c2 < 0 or r2 > row-1 or c2 > col-1:return
        # 如果下一个点是箱子，且下下个点是墙或箱子，也不移动
        if [r2, c2] in walls or [r2, c2] in boxs: return
        # 其他情况，将箱移动到新的位置
        boxs.remove([r1, c1])   # 移动箱子相当于将原来位置的箱子删除
        boxs.append([r2, c2])   # 并在下下个位置中添加一个新的箱子
    prow, pcol = r1, c1  # 移动玩家玩色，即：将玩家坐标更新为下一个位置



# 上下左右键的绑定
def move_up():  # 向上，下一个位置为当前列，行数减1
    moving(prow-1, pcol, prow-2, pcol)
turtle.onkey(move_up, 'Up')

def move_down():  # 向下，下一个位置为当前列，行数加1
    moving(prow+1, pcol, prow+2, pcol)
turtle.onkey(move_down, 'Down')

def move_left():  # 向左，下一个位置为当前行，列数减1
    moving(prow, pcol-1, prow, pcol-2)
turtle.onkey(move_left, 'Left')

def move_right():  # 向右，下一个位置为当前行，列数加1
    moving(prow, pcol+1, prow, pcol+2)
turtle.onkey(move_right, 'Right')

# r键的重新开始功能绑定
def restart():  # 重新开始本关
    load_board() # 重新开始本关，只需要重新加载当前关卡地图数据即可
turtle.onkey(restart, 'r')

# n键，进入下一关
def next_level():
    global level
    if level+1 <= len(maps):  # 如果不是最后一关
        level += 1
        load_board()
turtle.onkey(next_level, 'n')

# p键，进入上一关
def pre_level():
    global level
    if level > 1:  # 如果不是第一关
        level -= 1
        load_board()
turtle.onkey(pre_level, 'p')

turtle.listen()

# 游戏主函数
def main():
    global win
    turtle.clear()      # 清空画布
    draw_bg()           # 绘制背景
    draw_elements()     # 绘制各个角色
    draw_tips()         # 绘制提示
    # 如果win为True，也就当前为胜利的状态就结束游戏循环
    if win: return
    # 判断是否完成本关
    if is_next_level():
        # 完成本关时，判断是否为最后一关
        if level == len(maps):
            win = True
        else:
            next_level()
    turtle.update()
    turtle.ontimer(main, 100)


if __name__ == '__main__':
    # 游戏开始
    init()  # 先初始化设置
    load_board()  # 加载地图
    main()
    turtle.done()
