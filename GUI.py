import pygame
import board_generator
import solver

pygame.font.init()
Window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Sudoku")
x = 0
z = 0
cube_size = 500 / 9
value = 0
color1 = (255, 255, 0)

grid = board_generator.generate()

font = pygame.font.SysFont("comicsans", 40)
font1 = pygame.font.SysFont("comicsans", 20)


def cord(pos):
    global x
    x = pos[0]
    global z
    z = pos[1]


def highlightBox():
    for i in range(2):
        pygame.draw.line(Window, (100, 0, 0), (x * cube_size - 3, (z + i) * cube_size),
                         (x * cube_size + cube_size + 3, (z + i) * cube_size), 7)
        pygame.draw.line(Window, (100, 0, 0), ((x + i) * cube_size, z * cube_size),
                         ((x + i) * cube_size, z * cube_size + cube_size), 7)


def makeGrid():
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                pygame.draw.rect(Window, (255, 255, 255), (i * cube_size, j * cube_size, cube_size + 1, cube_size + 1))
                text1 = font.render(str(grid[i][j]), 1, (0, 0, 0))
                Window.blit(text1, (i * cube_size + 15, j * cube_size))
    for k in range(10):
        if k % 3 == 0:
            pygame.draw.line(Window, (0, 0, 0), (0, k * cube_size), (500, k * cube_size), 7)
            pygame.draw.line(Window, (0, 0, 0), (k * cube_size, 0), (k * cube_size, 500), 7)

        else:
            pygame.draw.line(Window, (0, 0, 0), (0, k * cube_size), (500, k * cube_size), 2)
            pygame.draw.line(Window, (0, 0, 0), (k * cube_size, 0), (k * cube_size, 500), 2)


def fillValue(value):
    text1 = font.render(str(value), 1, (0, 0, 0))
    Window.blit(text1, (x * cube_size + 15, z * cube_size + 15))


def wrongInput():
    text1 = font.render("wrong!", 1, (0, 0, 0))
    Window.blit(text1, (20, 570))


def wrongInput1():
    text1 = font.render("wrong! Enter a valid key!", 1, (0, 0, 0))
    Window.blit(text1, (20, 570))


def gameresult():
    text1 = font.render("game finished", 1, (0, 0, 0))
    Window.blit(text1, (20, 570))


run = True
isCellSelected = False
isCheckSolutionRequested = False
result = 0
error = 0

while run:
    Window.fill((255, 182, 193))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            isCellSelected = True
            pos = pygame.mouse.get_pos()
            cord(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x == 0:
                    x = 0
                else:
                    x -= 1
                isCellSelected = 1
            if event.key == pygame.K_RIGHT:
                if x == 8:
                    x = 8
                else:
                    x += 1
                isCellSelected = 1
            if event.key == pygame.K_UP:
                if z == 0:
                    z = 0
                else:
                    z -= 1
                isCellSelected = 1
            if event.key == pygame.K_DOWN:
                if z == 8:
                    z = 8
                else:
                    z += 1
                isCellSelected = 1
            if event.key == pygame.K_1:
                value = 1
            if event.key == pygame.K_2:
                value = 2
            if event.key == pygame.K_3:
                value = 3
            if event.key == pygame.K_4:
                value = 4
            if event.key == pygame.K_5:
                value = 5
            if event.key == pygame.K_6:
                value = 6
            if event.key == pygame.K_7:
                value = 7
            if event.key == pygame.K_8:
                value = 8
            if event.key == pygame.K_9:
                value = 9
            if event.key == pygame.K_RETURN:
                isCheckSolutionRequested = True
            if event.key == pygame.K_r:
                result = 0
                error = 0
                isCheckSolutionRequested = False
                defaultgrid = grid
            if event.key == pygame.K_d:
                grid = solver.solve(grid)
                result = 0
                error = 0
                isCheckSolutionRequested = False
                defaultgrid = grid

    if isCheckSolutionRequested:
        if not solver.solve(grid):
            error = 1
        else:
            result = 1
        isCheckSolutionRequested = False
    if value != 0 and isCellSelected:
        fillValue(value)
        if solver.valid(grid, value, (int(x), int(z))):
            grid[int(x)][int(z)] = value
            isCellSelected = False
        else:
            grid[int(x)][int(z)] = 0
        value = 0

    if error == 1:
        wrongInput()
    if result == 1:
        gameresult()
    makeGrid()
    if isCellSelected:
        highlightBox()
    pygame.display.update()

pygame.quit()
