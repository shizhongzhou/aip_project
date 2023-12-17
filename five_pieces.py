
import random
import sys
import pygame
import numpy as np

# 0表示空棋
# 1表示黑棋
# 2表示白棋
# 3表示下棋的位置

cdata = [
    # 一颗棋子的情况

    [1, 3, 0, 0, 0], [0, 1, 3, 0, 0], [0, 0, 1, 3, 0], [0, 0, 0, 1, 3], [0, 0, 0, 3, 1],
    [2, 3, 0, 0, 0], [0, 2, 3, 0, 0], [0, 0, 2, 3, 0], [0, 0, 0, 2, 3], [0, 0, 0, 3, 2],
    # 二颗棋子的情况
    [0, 1, 3, 1, 0], [1, 1, 3, 0, 0], [0, 0, 3, 1, 1],
    [2, 2, 3, 0, 0], [0, 0, 3, 2, 2], [0, 2, 3, 2, 0],
    # 三颗棋子的情况
    [1, 1, 1, 3, 0], [0, 3, 1, 1, 1], [1, 1, 3, 1, 0], [1, 3, 1, 1, 0],
    [2, 2, 0, 3, 2], [2, 3, 0, 2, 2], [0, 3, 2, 2, 2], [2, 2, 3, 2, 0],
    [2, 3, 2, 2, 0], [0, 2, 3, 2, 2], [0, 2, 2, 3, 2], [2, 2, 2, 3, 0], [3, 2, 2, 2, 0],
    # 四颗棋子情况
    [1, 1, 1, 1, 3], [3, 1, 1, 1, 1], [1, 1, 1, 3, 1], [1, 3, 1, 1, 1], [1, 1, 3, 1, 1],
    [2, 2, 2, 2, 3], [3, 2, 2, 2, 2], [2, 2, 3, 2, 2], [2, 3, 2, 2, 2], [2, 2, 2, 3, 2]
]

def draw_start_screen(screen):
    """绘制开始屏幕和开始游戏按钮。"""
    # screen.fill((0, 0, 0))  # 用黑色填充屏幕
    background = pygame.image.load("/Users/shi/python/WechatIMG364.pic")
    background = pygame.transform.scale(background, (615, 615))  # 调整背景图片大小以适应屏幕
    screen.blit(background, (0, 0))
    font = pygame.font.Font(None, 70)

    # 绘制标题
    title_text = font.render("Backgammon game", True, (255, 255, 255))
    screen.blit(title_text, ((615 - title_text.get_width()) / 2, 150))

    # 绘制开始游戏按钮
    button_text = font.render("play", True, (255, 255, 255))
    button_rect = button_text.get_rect(center=(307, 400))
    pygame.draw.rect(screen, (0, 128, 0), button_rect.inflate(20, 20))
    screen.blit(button_text, button_rect)

    pygame.display.update()
    return button_rect

def auto_mach(row, col, level, dx, dy):
    global ai_col, ai_row, max_level
    col_sel = -1  # 暂存棋子列号
    row_sel = -1  # 暂存棋子行号
    isfind = True  # 匹配成功的标记

    for j in range(5):
        cs = alist[row + j * dx][col + j * dy]
        if cs == 0:
            if cdata[level][j] == 3:
                row_sel = row + j * dx
                col_sel = col + j * dy
            elif cdata[level][j] == 1:
                isfind = False
                break
            elif cdata[level][j] == 2:
                isfind = False
                break
        elif cs != cdata[level][j]:
            isfind = False
            break
    if isfind:
        ai_row = row_sel
        ai_col = col_sel
        max_level = level
        return True
    return False


def ai_play():
    global ai_col, ai_row, max_level
    ai_col = -1
    ai_row = -1
    max_level = -1
    # 搜素棋盘每个位置
    for i in range(19):
        for j in range(19):
            # 从高到低搜索
            for level in range(len(cdata) - 1, -1, -1):
                if level > max_level:
                    if i + 4 < 19:
                        if auto_mach(i, j, level, 1, 0):
                            break
                    if j + 4 < 19:
                        if auto_mach(i, j, level, 0, 1):
                            break

                    if i + 4 < 19 and j + 4 < 19:
                        if auto_mach(i, j, level, 1, 1):
                            break

                    if j + 4 < 19 and i - 4 > 0:
                        if auto_mach(i, j, level, -1, 1):
                            break
    if ai_row!=-1 and ai_row!=-1:
        alist[ai_row][ai_col]=2
        return True
    while True:
        col = random.randint(0,18)
        row = random.randint(0, 18)
        if alist[row][col]==0:
            alist[row][col]=2
            ai_row=row
            ai_col=col

            return True
    return False


def init(screen):
    pygame.init()
    # 创建窗口，背景为棕色
    # global screen
    screen = pygame.display.set_mode((615, 615))
    pygame.display.set_caption('五子棋')
    screen.fill("#DD954F")
    # 创建外边框

    a = pygame.Surface((603, 603), flags=pygame.HWSURFACE)
    a.fill(color='#121010')
    b = pygame.Surface((585, 585), flags=pygame.HWSURFACE)
    b.fill(color="#DD954F")
    c = pygame.Surface((579, 579), flags=pygame.HWSURFACE)
    c.fill(color='#121010')

    e = pygame.Surface((31, 31), flags=pygame.HWSURFACE)
    e.fill(color="#DD954F")
    screen.blit(a, (6.5, 6.5))
    screen.blit(b, (15, 15))
    screen.blit(c, (18, 18))
    # 棋盘格子
    for j in range(18):
        for i in range(18):
            # 起点是20,间隔是32，每个格子大小31，所以格子间距1
            screen.blit(e, (20 + 32 * i, 20 + 32 * j))
    # 存储棋盘状态
    global alist
    alist = np.zeros((19, 19))
    # 星位
    pygame.draw.circle(screen, '#121010', [307.5, 307.5], 5)
    pygame.draw.circle(screen, '#121010', [115.5, 307.5], 5)
    pygame.draw.circle(screen, '#121010', [499.5, 307.5], 5)
    pygame.draw.circle(screen, '#121010', [115.5, 499.5], 5)
    pygame.draw.circle(screen, '#121010', [499.5, 499.5], 5)
    pygame.draw.circle(screen, '#121010', [115.5, 115.5], 5)
    pygame.draw.circle(screen, '#121010', [499.5, 115.5], 5)
    pygame.draw.circle(screen, '#121010', [307.5, 499.5], 5)
    pygame.draw.circle(screen, '#121010', [307.5, 115.5], 5)
    # 刷新窗口
    pygame.display.flip()


# 绘制棋子
def black(x, y,screen):
    a = 20
    b = 20
    c = 20
    d = 0.01
    # 循环50次，每次绘制50个半径颜色不同的同心圆
    for i in range(50):
        pygame.draw.circle(screen, (a, b, c), [19.5 + 32 * x, 19.5 + 32 * y], (16 / (d - 5) + 16))
        a += 1
        b += 1
        c += 1
        d += 0.08
    pygame.display.update()


def white(x, y,screen):
    a = 170
    b = 170
    c = 170
    d = 0.02
    for i in range(50):
        pygame.draw.circle(screen, (a, b, c), [19.5 + 32 * x, 19.5 + 32 * y], (16 / (d - 5) + 16))
        a += 1
        b += 1
        c += 1
        d += 0.08
    pygame.display.update()


pygame.font.init()
font1 = pygame.font.Font(None, 250)


# 主要操作
def do(wb,screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # 棋盘边界线的中点是19.5， 通过计算得到当前坐标在棋盘的行号和列号（x，y）
                x = round((x - 19.5) / 32)
                y = round((y - 19.5) / 32)
                if x < 0:
                    x = 0
                if x > 18:
                    x = 18
                if y < 0:
                    y = 0
                if y > 18:
                    y = 18
                if alist[x][y] == 0:
                    black(x, y,screen)
                    alist[x][y] = 1
                    wb1 = "You"
                    wb = "white"
                    check(x, y, wb1,screen)
                    pygame.time.wait(100)
                    if ai_play():
                        white(ai_row, ai_col,screen)
                        wb1 = "AI"
                        wb = "black"
                        check(ai_row, ai_col, wb1,screen)

def check(x, y, wb1,screen):
    xx = x
    yy = y
    while True:
        # 从最上边的棋子开始检查，记录颜色相同得棋子数量
        # 先找到最同一条线上最上边的同色棋子
        if xx == 0:
            if alist[xx][yy] != alist[x][y]:
                xx += 1
            break
        elif alist[xx][yy] != alist[x][y]:
            xx += 1
            break
        else:
            xx -= 1
    num = 0
    while True:
        if xx == 18:
            if alist[xx][yy] == alist[x][y]:
                num += 1
            break
        elif alist[xx][yy] != alist[x][y]:
            break
        else:
            xx += 1
            num += 1
    if num >= 5:
        win(wb1, screen)
    # 从最边的棋子开始检查，记录颜色相同得棋子数量
    # 先找到最同一条线上最左边的同色棋子
    xx = x
    yy = y
    while True:
        if yy == 0:
            if alist[xx][yy] != alist[x][y]:
                yy += 1

            break
        elif alist[xx][yy] != alist[x][y]:
            yy += 1
            break
        else:
            yy -= 1
    num = 0
    while True:
        if yy == 18:
            if alist[xx][yy] == alist[x][y]:
                num += 1
            break
        elif alist[xx][yy] != alist[x][y]:
            break
        else:
            yy += 1
            num += 1
    if num >= 5:
        win(wb1, screen)

    # 从左上方的棋子开始检查，记录颜色相同得棋子数量

    # 先找到最同一条线上左上方的同色棋子
    xx = x
    yy = y
    while True:
        if xx == 0:
            if alist[xx][yy] != alist[x][y]:
                xx += 1
                yy += 1
            break
        elif yy == 0:
            if alist[xx][yy] != alist[x][y]:
                xx += 1
                yy += 1
            break
        elif alist[xx][yy] != alist[x][y]:
            xx += 1
            yy += 1
            break
        else:
            xx -= 1
            yy -= 1
    num = 0
    while True:
        if xx == 18:
            if alist[xx][yy] == alist[x][y]:
                num += 1

            break
        elif yy == 18:
            if alist[xx][yy] == alist[x][y]:
                num += 1
            break
        elif alist[xx][yy] != alist[x][y]:
            break
        else:
            xx += 1
            yy += 1
            num += 1
    if num >= 5:
        win(wb1, screen)

    # 从右上方的棋子开始检查，记录颜色相同得棋子数量

    # 先找到最同一条线上右上方的同色棋子
    xx = x
    yy = y
    while True:
        if xx == 0:
            if alist[xx][yy] != alist[x][y]:
                xx += 1
                yy -= 1
            break
        elif yy == 18:
            if alist[xx][yy] != alist[x][y]:
                xx += 1
                yy -= 1
            break
        elif alist[xx][yy] != alist[x][y]:
            xx += 1
            yy -= 1
            break
        else:
            xx -= 1
            yy += 1
    num = 0
    while True:
        if xx == 18:
            if alist[xx][yy] == alist[x][y]:
                num += 1
            break
        elif yy == 0:
            if alist[xx][yy] == alist[x][y]:
                num += 1
            break
        elif alist[xx][yy] != alist[x][y]:
            break
        else:
            xx += 1
            yy -= 1
            num += 1
    if num >= 5:
        win(wb1, screen)


def win(wb1,screen):
    font = pygame.font.Font(None, 70)
    text = font.render(f"{wb1} won", True, (255, 255, 255))
    screen.blit(text, ((655 - text.get_width()) / 2, (665 - text.get_height()) / 2))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                init()
                text = font.render("Start the game", True, (255, 255, 255))
                screen.blit(text, ((655 - text.get_width()) / 2, (665 - text.get_height()) / 2))
                pygame.display.update()
                pygame.time.wait(500)
                init()
                do("black")


def main():
    pygame.init()
    screen = pygame.display.set_mode((615, 615))
    pygame.display.set_caption('五子棋')

    # 绘制开始屏幕
    start_button_rect = draw_start_screen(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # 获取鼠标位置
                if start_button_rect.collidepoint(mouse_pos):
                    # 进入游戏模式
                    init(screen)
                    do('black', screen)

if __name__ == "__main__":
    main()



