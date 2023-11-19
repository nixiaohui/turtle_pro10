s = 40
score = 0
total_score = 0
nxt_level_score = 3
count_down = 4
row_num, col_num = 10, 20
w, h = s*col_num + 4*s, s*row_num+4*s
colors = {
    'snake': ['#3498DB', '#3498DB'],
    'fruits': ['#F5B041', '#E74C3C', '#27AE60'],
    'bg': ['#C2F2C2', '#E2F2E2'],
    'walls': ['#E74C3C'],
    'tips': ['#CB4335'],
    'white': '#FFFFFF',
    'gray' : '#DDDDDD'
}
snakes = [(2, 2)]
directions = {'dx':1, 'dy':0}
speed = 1
pause = False
status = 1  # -1 失败， 1 进行中，2 胜利
fruits = [] #[(5, 3, 1), (7, 2, 2), (4, 6, 0)]
tx, ty = -s*col_num//2, s*row_num//2

level = 1
speed = (8-level)*50
walls = [
    [(8, 8), (8, 9)],
    [(2, 6), (2, 7), (6, 15), (7, 15)],
    [(4, 6), (5, 6), (3, 16), (3, 17)]
]