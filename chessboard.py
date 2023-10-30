# python基础，棋盘+棋子
import turtle


row = 8   # 8行
col = 8   # 8列
s = 60
tx = -s*4
ty = s*4

turtle.tracer(0)
turtle.hideturtle()
turtle.up()

for j in range(row):  # 绘制row行
    for i in range(col):  # 每一行绘制 col列个格子
        x = tx + i*s   # 每个x坐标由左上角的x坐标为基准进行偏移
        y = ty - j*s   # 每个y坐标由左上角的y坐标为基准进行偏移
        turtle.goto(x, y) # 移动到每个小方格的位置
        turtle.down()     # 落笔
        if i%2!=j%2:
            c = '#D2D2D2'
        else:
            c = '#EFEFEF'
        turtle.fillcolor(c)
        turtle.begin_fill()
        for k in range(4):  # 绘制一个小方格
            turtle.fd(s)
            turtle.rt(90)
        turtle.end_fill()
        turtle.up()       # 抬笔

#  ♜ ♞ ♝ ♛ ♚ ♟
chs1 = ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
# ♜ ♞ ♝ ♛ ♚ ♟ ♖ ♘ ♗ ♕ ♔ ♙
chs4 = ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']

# ! 高阶用法：列表生成式！！！
chs2 = ['♟' for i in range(8)]
chs3 = ['♙' for i in range(8)]

chs = [chs1, chs2, chs3, chs4]
x_list1 = []
y_list1 = []

x_list2 = []
y_list2 = []

x_list3 = []  # [tx+s*i+s//2 for i in range(8)]
for i in range(8):
    x_list3.append(tx+s*i+s//2)
y_list3 = [ty-7*s for i in range(8)]

x_list4 = [tx+s*i+s//2 for i in range(8)]
y_list4 = [ty-8*s for i in range(8)]

x_list = [x_list1, x_list2, x_list3, x_list4]
y_list = [y_list1, y_list2, y_list3, y_list4]

for j in range(2):
    for i in range(8):
        x_list[j].append(tx+s*i+s//2)
        y_list[j].append(ty-(j+1)*s)

# arr = [
#     [32, 11, 25, 18, 9],
#     [21, 12, 87, 11, 23],
#     [54, 67, 32, 98, 11]
# ]
# arr[1][2] -> 行编号为1中，编号为2的元素：87

for j in range(4):
    for i in range(8):
        turtle.goto(x_list[j][i], y_list[j][i])
        turtle.write(chs[j][i], False, 'center', ('楷体', 35))

turtle.update()
turtle.done()
