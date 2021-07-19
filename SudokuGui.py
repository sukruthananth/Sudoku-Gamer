import pygame
import time
from SudokuOperation import *
pygame.font.init()
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
run = True
start_time = time.time()
width = 540
height = 600
x_time = 400
y_time = 560
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("SUDOKU")
win.fill((255,255,255))
class Sudoku():
    board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
    def __init__(self):
        self.position = None
        self.temp_model = self.board
        self.cube = [[Cube(self.board[j][i],j,i) for i in range(9)] for j in range(9)]
        self.temp_model = self.board

    def draw_existing_Sudoku(self,win):
        existing_font = pygame.font.SysFont("Comicsans",24)
        half_gap = 60/2
        for i in range(9):
            for j in range(9):
                if self.cube[i][j].value != 0:
                    self.cube[i][j].draw_cube(win)
                if self.cube[i][j].selected ==True:
                    self.cube[i][j].draw_cube(win)
    def set_position(self, position):
        self.position = position
        y_position = position[0]//60
        x_position = position[1]//60
        if self.cube[x_position][y_position].value ==0:
            self.cube[x_position][y_position].selected = True
            # self.cube[x_position][y_position].value = key

    def validate_key(self,key, position):
        y,x = position
        x = x//60
        y=y//60
        # self.temp_model[x][y] = key
        if valid(self.temp_model,key, (x,y)):
            self.temp_model[x][y] = key
            if sudoku_solver(self.temp_model):
                self.cube[x][y].value = key
                return True
            else:
                self.temp_model[x][y] = 0
                return False
        else:
            return False

    def clear_selection(self,x,y):
        # self.cube[y//60][x//60].value = 0
        for i in range(9):
            for j in range(9):
                self.cube[i][j].temp =0
                self.cube[i][j].selected = False
                # self.cube[i][j].value =0
    def is_solved(self):
        for i in range(9):
            for j in range(9):
                if self.cube[i][j].value ==0:
                    return False
        else:
            return True

def draw_sudoku_board(win, time, board, wrong_index):
    win.fill((255,255,255))
    font = pygame.font.SysFont("comicsans", 30)
    time_text = font.render("Time:"+convert_time(time),1,(0,0,0))
    win.blit(time_text, (x_time,y_time))
    wrong_text = font.render("X"*wrong_index,1,(255,0,0))
    win.blit(wrong_text,(20, 560))
    draw_grid(win)
    board.draw_existing_Sudoku(win)


def draw_grid(win):
    gap = 540/9
    for i in range(10):
        if i%3 ==0:
            thickness =4
        else:
            thickness = 1
        pygame.draw.line(win,(0,0,0),(0,gap*i),(540,gap*i),thickness)
    for j in range(10):
        if j%3==0:
            thickness = 4
        else:
            thickness = 1
        pygame.draw.line(win,(0,0,0),(gap*j,0),(gap*j,540),thickness)


def convert_time(sec):
    min = sec//60
    sec = sec%60
    return " "+str(min) + ":" +str(sec)

class Cube:
    def __init__(self,value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.temp = None
        self.selected = False
    def draw_cube(self,win):

        existing_font = pygame.font.SysFont("Comicsans", 24)
        if self.temp!=0 and self.value == 0:
            half_gap = 60 / 2
            existing_text = existing_font.render(str(self.temp), 1, (0, 0, 0))
            win.blit(existing_text, (self.y*60 +5, self.x*60 +5))

        elif self.value!=0:
            half_gap = 60 / 2
            existing_text = existing_font.render(str(self.value), 1, (0, 0, 0))
            win.blit(existing_text, (self.y * 60 + half_gap - (existing_text.get_width() / 2), self.x * 60 + half_gap - (existing_text.get_height() / 2)))
        if self.selected:
            pygame.draw.rect(win, (128, 128, 128), (self.y * 60, self.x * 60, 60, 60),3)
position=(0,0)
sudoku_board = Sudoku()
key = 0
wrong_index = 0
while run:
    playtime = round(time.time()-start_time)
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            key = 1
        if keys[pygame.K_2]:
            key = 2
        if keys[pygame.K_3]:
            key = 3
        if keys[pygame.K_4]:
            key = 4
        if keys[pygame.K_5]:
            key = 5
        if keys[pygame.K_6]:
            key = 6
        if keys[pygame.K_7]:
            key = 7
        if keys[pygame.K_8]:
            key = 8
        if keys[pygame.K_9]:
            key = 9
        if keys[pygame.K_RETURN]:
            if sudoku_board.validate_key(key, position):
                print("success")
            else:
                wrong_index +=1
            if sudoku_board.is_solved():
                run = False
                print("The board is solved")

        if events.type == pygame.MOUSEBUTTONDOWN:
            sudoku_board.clear_selection(position[0],position[1])
            position = pygame.mouse.get_pos()
            if position:
                sudoku_board.set_position(position)
            key =0


    draw_sudoku_board(win,playtime, sudoku_board, wrong_index)
    if key and position:
        sudoku_board.cube[position[1]//60][position[0]//60].temp = key

    pygame.display.update()