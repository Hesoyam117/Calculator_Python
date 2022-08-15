import pygame
import math
from settings import *
pygame.init()

def drawWindow():
    global numbers
    global result
    global strpos1
    win.blit(calc, (0, 0))
    win_stringtext = f_sys.render(str(numbers), 4, (0, 0, 0))
    win_result = f_sys.render(str(result), 4, (0, 0, 0))
    numbers = fNum + do
    numbers = numbers + SNum
    if sDone == 0 and do != 'Х²' and do != '√X':
        win.blit(win_stringtext, (strpos1, 40))
    elif sDone == 1 or do == 'Х²' or do == '√X':
        win.blit(win_result, (strpos1, 40))
    win.blit(block, (0, 0))
    for i in range (0, 20):
        if pick != i:
            win_symbols[i] = f_sys.render(str(symbols[i]), 4, (0, 0, 0))
            win.blit(win_symbols[i], (coords[i]))
        elif pick == i:
            win_symbols[i] = f_sys2.render(str(symbols[i]), 4, (0, 0, 0))
            win.blit(win_symbols[i], (coords[i]))
    pygame.display.flip()

def calculation():
    global do
    global fNum
    global SNum
    global result
    global numbers
    if sDone == 1:
        if fNum.find('.') == -1 and SNum.find('.') == -1:
            if do == '+':
                result = int(fNum) + int(SNum)
            elif do == '-':
                result = int(fNum) - int(SNum)
            elif do == 'x':
                result = int(fNum) * int(SNum)
            elif do == '/':
                result = int(fNum) / int(SNum)
            result = str(result)
            if result[-1] == '0' and result[-2] == '.':
                result = result[0:-2]
            if len(result) > 13:
                result = result[0:10] + '...'
        else:
            if do == '+':
                result = float(fNum) + float(SNum)
            elif do == '-':
                result = float(fNum) - float(SNum)
            elif do == 'x':
                result = float(fNum) * float(SNum)
            elif do == '/':
                result = float(fNum) / float(SNum)
            result = str(result)
            if result[-1] == '0' and result[-2] == '.':
                result = result[0:-2]
            if len(result) > 13:
                result = result[0:10] + '...'
    elif fDone == 1 and sDone == 0:
        if fNum.find('.') == -1 and SNum.find('.') == -1:
            if do == 'Х²':
                result = int(fNum) ** 2
                result = str(result)
                if len(result) > 13:
                    result = result[0:10] + '...'

            if do == '√X':
                result = math.sqrt(int(fNum))
                result = str(result)
                if result[-1] == '0' and result[-2] == '.':
                    result = result[0:-2]
                if len(result) > 13 and (result.find('.') != -1):
                    result = result[0:13]
                if len(result) > 13:
                    result = result[0:10] + '...'
        else:
            if do == 'Х²':
                result = float(fNum) ** 2
                result = str(result)
                if len(result) > 13:
                    result = result[0:10] + '...'
            if do == '√X':
                result = math.sqrt(float(fNum))
                result = str(result)
                if result[-1] == '0' and result[-2] == '.':
                    result = result[0:-2]
                if len(result) > 13 and (result.find('.') != -1):
                    result = result[0:13] + '...'
                if len(result) > 13:
                    result = result[0:10] + '...'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEMOTION:
            #print(event.pos)
            for i in range (0, 20):
                if event.pos[0] >= coordx1[i] and event.pos[0] <= coordx2[i] and event.pos[1] >= coordy1[i] and event.pos[1] <= coordy2[i]:
                    pick = i
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if (pick >= 0 and pick <= 8) or pick == 17:
                    if fDone == 0:
                        fNum1 = symbols[pick]
                        fNum = fNum + fNum1
                    elif fDone == 1:
                        SNum1 = symbols[pick]
                        SNum = SNum + SNum1
                elif pick >= 9 and pick <= 14:
                    if fDone == 0:
                        fDone = 1
                        do = symbols[pick]
                elif pick == 19:
                    if sDone == 0:
                        sDone = 1
                elif pick == 15:
                    fNum = ''
                    fNum1 = ''
                    SNum = ''
                    SNum1 = ''
                    do = ''
                    numbers = ''
                    result = ''
                    fDone = 0
                    sDone = 0
                elif pick == 18:
                    if fDone == 0:
                        fNum1 = symbols[pick]
                        fNum = fNum + fNum1
                    elif fDone == 1:
                        SNum1 = symbols[pick]
                        SNum = SNum + SNum1
                elif pick == 16:
                    if fDone == 0:
                        fNum = fNum[0:-1]
                    if fDone == 1 and sDone == 0 and do != '':
                        SNum = SNum[0:-1]
                        if SNum == '':
                            fDone = 0
                            sDone = 0
                            do = ''

    calculation()
    drawWindow()
    clock.tick(FPS)
