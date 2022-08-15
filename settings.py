import pygame
import math
pygame.init()
W = 902
H = 900
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Calc")
FPS = 30
clock = pygame.time.Clock()

calc = pygame.image.load('materials/calc.png').convert()
calc = pygame.transform.scale(calc, (calc.get_width()*9, calc.get_height()*9))
block = pygame.image.load('materials/block.png').convert_alpha()
block = pygame.transform.scale(block, (block.get_width()*9, block.get_height()*9))
pos = pygame.mouse.get_pos()

f_sys = pygame.font.SysFont('calibri', 100)
f_sys2 = pygame.font.SysFont('calibri', 120)
win_textpoint = f_sys.render(str("."), 4, (0, 0, 0))
win_text0 = f_sys.render(str("0"), 4, (0, 0, 0))
win_text1 = f_sys.render(str("1"), 4, (0, 0, 0))
win_text2 = f_sys.render(str("2"), 4, (0, 0, 0))
win_text3 = f_sys.render(str("3"), 4, (0, 0, 0))
win_text4 = f_sys.render(str("4"), 4, (0, 0, 0))
win_text5 = f_sys.render(str("5"), 4, (0, 0, 0))
win_text6 = f_sys.render(str("6"), 4, (0, 0, 0))
win_text7 = f_sys.render(str("7"), 4, (0, 0, 0))
win_text8 = f_sys.render(str("8"), 4, (0, 0, 0))
win_text9 = f_sys.render(str("9"), 4, (0, 0, 0))
win_textplus = f_sys.render(str("+"), 4, (0, 0, 0))
win_textminus = f_sys.render(str("-"), 4, (0, 0, 0))
win_textdivide = f_sys.render(str("/"), 4, (0, 0, 0))
win_textmultiply = f_sys.render(str("x"), 4, (0, 0, 0))
win_textsqr = f_sys.render(str("Х²"), 4, (0, 0, 0))
win_textsqrt = f_sys.render(str("√X"), 4, (0, 0, 0))
win_textc = f_sys.render(str("C"), 4, (0, 0, 0))
win_textback = f_sys.render(str("<="), 4, (0, 0, 0))
win_textequals = f_sys.render(str("="), 4, (0, 0, 0))


coordx1 = [12, 235, 460, 12, 235, 460, 12, 235, 460, 12, 235, 460, 12, 235, 460, 710, 710, 710, 710, 720]
coordx2 = [220, 430, 670, 220, 430, 670, 220, 430, 670, 220, 430, 670, 220, 430, 670, 880, 880, 880, 880, 890]
coordy1 = [220, 220, 220, 365, 365, 365, 510, 510, 510, 670, 670, 670, 785, 785, 785, 220, 430, 643, 768, 20]
coordy2 = [340, 340, 340, 486, 486, 486, 630, 630, 630, 766, 766, 766, 880, 880, 880, 400, 620, 750, 880, 190]
coords = [(90, 240) , (310, 240), (540, 240), (90, 385), (310, 385), (540, 385), (90, 530), (310, 530), (540, 530),\
(90, 675), (325, 675), (535, 675), (90, 785), (325, 785), (535, 790), (760, 270), (750, 490), (770, 655), (770, 800), (770, 70)]
win_symbols = [win_text7, win_text8, win_text9, win_text4, win_text5, win_text6, win_text1, win_text2, win_text3,\
win_textplus, win_textminus, win_textsqr, win_textmultiply, win_textdivide, win_textsqrt, win_textc, win_textback, win_text0, win_textpoint, win_textequals]
symbols = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '+', '-', 'Х²', 'x', '/', '√X', 'C', '<=', '0', '.', '=']

fNum = ''
fNum1 = ''
SNum = ''
SNum1 = ''
do = ''
numbers = ''
result = ''
fDone = 0
sDone = 0



strpos1 = 40



pick = 0
