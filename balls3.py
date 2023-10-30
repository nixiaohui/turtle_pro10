# python基础：turtle实现随机移动的小球动画
import turtle
import random  # 随机模块 -> 生成随机数（随机整数）
import time

width, height = 1200, 600  # 设置窗口的宽、高
n = 50                     # 设置小球的数量
dlist = []                 # 存储所有小球的所有直径
xlist = []                 # 存储所有小球的x坐标
ylist = []                 # 存储所有小球的y坐标
clist = []                 # 存储所有小球的颜色
sxlist = []                # 存储所有小球x方向的速度
sylist = []                # 存储所有小球y方向的速度

# 循环n次，每次生成一个小球的所有属性，并将这些属性添加到相应的列表中
for i in range(n):
    d = random.randint(20, 220)  # 生成一个小球的直径
    dlist.append(d)              # 将这个小球的直径添加到列表中
    x = random.randint(-width//2, width//2)   # 生成一个小球的x坐标
    y = random.randint(-height//2, height//2) # 生成一个小球的y坐标
    xlist.append(x)         # 将x坐标添加到列表
    ylist.append(y)         # 将y坐标添加到列表
    r = random.randint(0, 255)  # 生成一个红色的随机值
    g = random.randint(0, 255)  # 生成一个绿色的随机值
    b = random.randint(0, 255)  # 生成一个蓝色的随机值
    c = (r, g, b)               # 将生成的红、绿、蓝合成一个随机颜色
    clist.append(c)             # 将随机的颜色加入列表
    sx = random.randint(-5, 5)  # 生成一个x方向的速度负为向左的速度，正为向右的速度
    sy = random.randint(-5, 5)  # 生成一个y方向的速度负为向下的速度，正为向上的速度
    sxlist.append(sx)   # 将x方向的速度添加到列表
    sylist.append(sy)   # 将y方向的速度添加到列表

turtle.setup(width, height)     # 设置窗口大小
turtle.tracer(0)                # 设置不跟踪绘制过程
turtle.hideturtle()             # 隐藏海龟
turtle.colormode(255)           # 将颜色模式设置为 (r, g, b)三元组模式
turtle.up()                     # 抬笔

# 动画的主循环
while True:
    # 1 清空画布
    turtle.clear()
    # 2 更新状态
    for i in range(n):  # 循环n次，更新n个小球的坐标
        # 根据第i个小球的x方向和y方向的速度更新x坐标和y坐标
        xlist[i] = xlist[i] + sxlist[i]
        ylist[i] = ylist[i] + sylist[i]
        # 判断第i个小球是不是出了边界，如果出了边界就将相应方向的速度变为相反
        if xlist[i] <= -width//2 or xlist[i] >= width//2:
            sxlist[i] = -sxlist[i]
        if ylist[i] <= -height//2 or ylist[i] >= height//2:
            sylist[i] = -sylist[i]
    # 3 绘制结果
    for i in range(n):
        turtle.goto(xlist[i], ylist[i])  # 移动到第i个小球的坐标上
        turtle.dot(dlist[i], clist[i])   # 按直径和颜色来绘制第i个小球
    turtle.update()  # 更新绘制结果到画布
    time.sleep(0.01) # 让程序等待0.01秒
