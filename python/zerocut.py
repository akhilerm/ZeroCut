import sys
import pygame
from pygame.locals import *

FPS = 30
SCREENWIDTH = SCREENHEIGHT = 512

#The game matrix initialized with None, False for O and True for X, Posession_Matrix stores which all submatrices is possessed by O and X
Game_Matrix = [[None for x in range(9)] for y in range(9)]
Posession_MatrixO = [[None for x in range(3)] for y in range (3)]
Posession_MatrixX = [[None for x in range(3)] for y in range (3)]
Active_Matrix = [[True for x in range(3)] for y in range(3)]
IMAGES, SOUNDS = {},{}
player = True

#Function to convert pixel coordinates into game coordinates -- matrix indices
def get_index(value):
    index = [0,0,0,0]
    #row conversion
    if 0<=value[1]<=163:
        index[0] = 0
        if 0<=value[1]<=51:
            index[2] = 0
        elif 56<=value[1]<=107:
            index[2] = 1
        elif 112<=value[1]<=163:
            index[2] = 2
        else:
            return None
    elif 174<=value[1]<=337:
        index[0] = 1
        if 174<=value[1]<=225:
            index[2] = 0
        elif 230<=value[1]<=281:
            index[2] = 1
        elif 286<=value[1]<=337:
            index[2] = 2
        else:
            return None
    elif 348<=value[1]<=511:
        index[0] = 2
        if 348<=value[1]<=399:
            index[2] = 0
        elif 404<=value[1]<=455:
            index[2] = 1
        elif 460<=value[1]<=511:
            index[2] = 2
        else:
            return None
    else:
        return None

    #column conversion
    if 0<=value[0]<=163:
        index[1] = 0
        if 0 <= value[0] <= 51:
            index[3] = 0
        elif 56 <= value[0] <= 107:
            index[3] = 1
        elif 112 <= value[0] <= 163:
            index[3] = 2
        else:
            return None
    elif 174 <= value[0] <= 337:
        index[1] = 1
        if 174 <= value[0] <= 225:
            index[3] = 0
        elif 230 <= value[0] <= 281:
            index[3] = 1
        elif 286 <= value[0] <= 337:
            index[3] = 2
        else:
            return None
    elif 348 <= value[0] <= 511:
        index[1] = 2
        if 348 <= value[0] <= 399:
            index[3] = 0
        elif 404 <= value[0] <= 455:
            index[3] = 1
        elif 460 <= value[0] <= 511:
            index[3] = 2
        else:
            return None
    else:
        return None

    return index

#Function to check whether the given matrix is clickable
def is_active(value):
    index = get_index(value)
    if index is None:
        return False
    if (Active_Matrix[index[0]][index[1]] == False):
        return False
    return True

#Function to check whether a 3x3 matrix has got 3 in a row
def check(matrix):
    #print matrix
    ret = {'O':False,'X':False}
    i=j=f1=f2=0
    for i in range(3):
        if matrix[i][j] == matrix[i][j+1] == matrix[i][j+2]:
            if matrix[i][j] is False:
                f1 = 1
            elif matrix[i][j] is True:
                f2 = 1
            #break
    i=0
    for j in range(3):
        if matrix[i][j] == matrix[i+1][j] == matrix[i+2][j]:
            if matrix[i][j] is False:
                f1 = 1
            elif matrix[i][j] is True:
                f2 = 1
            #break
    j=0
    if matrix[i][j] == matrix[i+1][j+1] == matrix[i+2][j+2]:
        if matrix[i][j] is False:
            f1 = 1
        elif matrix[i][j] is True:
            f2 = 1

    j=2
    if matrix[i][j] == matrix[i+1][j-1] == matrix[i+2][j-2]:
        if matrix[i][j] is False:
            f1 = 1
        elif matrix[i][j] is True:
            f2 = 1

    if f1 == 1:
        ret['O']=True
    if f2 == 1:
        ret['X']=True
    return ret


#Function to display the winner
def won(player):
    SOUNDS['win'].play()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN or event.type == MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                if 309 <pos[1]<329 and 184 <pos[0]<340:
                    return
                # drawing the screen
        SCREEN.blit(IMAGES['gamebg'], (0, 0))
        coord = [None, None]
        for i in range(9):
            for j in range(9):
                if Game_Matrix[i][j] is not None:
                    if i == 0:
                        coord[0] = 0
                    elif i == 1:
                        coord[0] = 56
                    elif i == 2:
                        coord[0] = 112
                    elif i == 3:
                        coord[0] = 174
                    elif i == 4:
                        coord[0] = 230
                    elif i == 5:
                        coord[0] = 286
                    elif i == 6:
                        coord[0] = 348
                    elif i == 7:
                        coord[0] = 404
                    else:
                        coord[0] = 460

                    if j == 0:
                        coord[1] = 0
                    elif j == 1:
                        coord[1] = 56
                    elif j == 2:
                        coord[1] = 112
                    elif j == 3:
                        coord[1] = 174
                    elif j == 4:
                        coord[1] = 230
                    elif j == 5:
                        coord[1] = 286
                    elif j == 6:
                        coord[1] = 348
                    elif j == 7:
                        coord[1] = 404
                    else:
                        coord[1] = 460
                    if Game_Matrix[i][j] == True:
                        SCREEN.blit(IMAGES['X'], (coord[1], coord[0]))
                    else:
                        SCREEN.blit(IMAGES['O'], (coord[1], coord[0]))
        if player == True:
            SCREEN.blit(IMAGES['X_win'], (0, 162))
        else:
            SCREEN.blit(IMAGES['O_win'], (0, 162))
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def check_full(matrix):
    for i in range(3):
        for j in range(3):
            if matrix[i][j] is None:
                return False
    return True

def playgame():
    global Active_Matrix
    global player

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                player = True
                return
            if event.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                index1 = get_index(pos)
                if is_active(pos) == False or (is_active(pos) == True and Game_Matrix[index1[0]*3+index1[2]][index1[1]*3+index1[3]] is not None):
                    SOUNDS['error'].play()
                else :
                    #valid movement
                    index = index1
                    Game_Matrix[index[0] * 3 + index[2]][index[1] * 3 + index[3]] = player
                    #print 'check 1'
                    #print 'index'
                    #print index
                    status = check([row[index[1]*3:index[1]*3+3] for row in Game_Matrix[index[0]*3:index[0]*3+3]]) #'O','X'
                    #print status
                    Active_Matrix = [[False for x in range(3)] for y in range(3)]
                    Active_Matrix[index[2]][index[3]] = True
                    if check_full([row[index[3]*3:index[3]*3+3] for row in Game_Matrix[index[2]*3:index[2]*3+3]]) is True:
                        #print 'Full poi'
                        Active_Matrix = [[True for x in range(3)] for y in range(3)]
                    if status['O'] == True and player == False:
                        #print 'in O'
                        Posession_MatrixO[index[0]][index[1]] = True
                        #print Posession_MatrixO
                        #print 'check 2'
                        win_status = check(Posession_MatrixO)
                        if win_status['X'] == True:    #win_status['X'] is used since both posession matrices use true to represent possesed ...
                            #print 'Ojayichu'
                            won(False)
                            return
                        player = not player
                        continue
                    if status['X'] == True and player == True:
                        #print 'in X'
                        Posession_MatrixX[index[0]][index[1]] = True
                        #print Posession_MatrixX
                        #print 'check 2'
                        win_status = check(Posession_MatrixX)
                        if win_status['X'] == True:
                            #print 'Xjayichu'
                            won(True)
                            return
                        player = not player
                        continue
                    #do all operations and change player
                    player = not player
        #drawing the screen
        SCREEN.blit(IMAGES['gamebg'],(0,0))
        coord = [None, None]
        for i in range(9):
           for j in range(9):
                if Game_Matrix[i][j] is not None:
                    if i == 0:
                        coord[0]=0
                    elif i == 1:
                        coord[0]=56
                    elif i == 2:
                        coord[0]=112
                    elif i == 3:
                        coord[0]=174
                    elif i == 4:
                        coord[0]=230
                    elif i == 5:
                        coord[0]=286
                    elif i == 6:
                        coord[0]=348
                    elif i == 7:
                        coord[0]=404
                    else:
                        coord[0]=460
                    
                    if j == 0:
                        coord[1]=0
                    elif j == 1:
                        coord[1]=56
                    elif j == 2:
                        coord[1]=112
                    elif j == 3:
                        coord[1]=174
                    elif j == 4:
                        coord[1]=230
                    elif j == 5:
                        coord[1]=286
                    elif j == 6:
                        coord[1]=348
                    elif j == 7:
                        coord[1]=404
                    else:
                        coord[1]=460
                    if Game_Matrix[i][j] == True:
                        SCREEN.blit(IMAGES['X'],(coord[1],coord[0]))
                    else:
                        SCREEN.blit(IMAGES['O'], (coord[1], coord[0]))
                    

        #setting the shadow for inactive matrices
        if all(Active_Matrix[0]) == all(Active_Matrix[1]) == all(Active_Matrix[2]) == False:
            if(index[2] == 1 and index[3] == 1):
                if player is True:
                    SCREEN.blit(IMAGES['wc_shad'],(0,0))
                else:
                    SCREEN.blit(IMAGES['bc_shad'], (0, 0))
            elif index[2] == 1 or index[3] == 1:
                if player is True:
                    shad = 'wm_shad'
                else:
                    shad = 'bm_shad'
                if index[2] == 1 and index[3] == 2:
                    SCREEN.blit(pygame.transform.rotate(IMAGES[shad],270),(0,0))
                elif index[2] == 2 and index[3] == 1:
                    SCREEN.blit(pygame.transform.rotate(IMAGES[shad], 180), (0, 0))
                elif index[2] == 1 and index[3] == 0:
                    SCREEN.blit(pygame.transform.rotate(IMAGES[shad], 90), (0, 0))
                else:
                    SCREEN.blit(IMAGES[shad], (0, 0))
            else:
                if player is True:
                    shad = 'ws_shad'
                else:
                    shad = 'bs_shad'
                if index[2] == 0 and index[3] == 2:
                    SCREEN.blit(pygame.transform.rotate(IMAGES[shad], 270), (0, 0))
                elif index[2] == 2 and index[3] == 2:
                    SCREEN.blit(pygame.transform.rotate(IMAGES[shad], 180), (0, 0))
                elif index[2] == 2 and index[3] == 0:
                    SCREEN.blit(pygame.transform.rotate(IMAGES[shad], 90), (0, 0))
                else:
                    SCREEN.blit(IMAGES[shad], (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS)



def main():
    global SCREEN, FPSCLOCK,Game_Matrix,Posession_MatrixO,Posession_MatrixX,Active_Matrix
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    logo = pygame.image.load('assets/images/ic_launcher_32.png')
    SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))#,pygame.NOFRAME)
    pygame.display.set_caption('ZeroCut')
    pygame.display.set_icon(logo)

    IMAGES['gamebg'] = pygame.image.load('assets/images/game.png').convert()
    IMAGES['welcome'] = pygame.image.load('assets/images/bg.png').convert()
    IMAGES['bc_shad'] = pygame.image.load('assets/images/bshadowc.png').convert_alpha()
    IMAGES['bm_shad'] = pygame.image.load('assets/images/bshadowm.png').convert_alpha()
    IMAGES['bs_shad'] = pygame.image.load('assets/images/bshadows.png').convert_alpha()
    IMAGES['wc_shad'] = pygame.image.load('assets/images/wshadowc.png').convert_alpha()
    IMAGES['wm_shad'] = pygame.image.load('assets/images/wshadowm.png').convert_alpha()
    IMAGES['ws_shad'] = pygame.image.load('assets/images/wshadows.png').convert_alpha()
    IMAGES['O'] = pygame.image.load('assets/images/O.png').convert_alpha()
    IMAGES['X'] = pygame.image.load('assets/images/X.png').convert_alpha()
    IMAGES['X_win'] = pygame.image.load('assets/images/winx.png').convert_alpha()
    IMAGES['O_win'] = pygame.image.load('assets/images/wino.png').convert_alpha()

    #sounds
    if 'win' in sys.platform:
        soundExt = '.wav'
    else:
        soundExt = '.ogg'

    SOUNDS['error'] = pygame.mixer.Sound('assets/audio/err'+soundExt)
    SOUNDS['win'] = pygame.mixer.Sound('assets/audio/win'+soundExt)

    #Overall game loop
    while True:

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                Game_Matrix = [[None for x in range(9)] for y in range(9)]
                Posession_MatrixO = [[None for x in range(3)] for y in range(3)]
                Posession_MatrixX = [[None for x in range(3)] for y in range(3)]
                Active_Matrix = [[True for x in range(3)] for y in range(3)]
                pos = pygame.mouse.get_pos()
                if  147 < pos[0] <366 and 368 < pos [1] < 420 :
                    playgame()

        SCREEN.blit(IMAGES['welcome'], (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
        main()
