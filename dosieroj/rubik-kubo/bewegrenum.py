#!/usr/bin/env python3
import farbscan
from time import sleep
import os

taste = farbscan.Button()
ton = farbscan.Sound()
fl = farbscan.fl
pos_ti = farbscan.pos_ti
pos_gd = farbscan.pos_gd
pos_gv = farbscan.pos_gv
global k

def tisch_kor(): # korrigiert die Position des Tisches
    akt_pos = farbscan.tischdreh.position
    bew = abs(pos_ti-akt_pos)
    if bew == (pos_ti-akt_pos):
        vorz = 1
    else:
        vorz = -1
    if bew%90 < 45:
        sol = akt_pos + vorz*(bew%90)
    else:
        sol = akt_pos - vorz*(90-bew%90)
    dif = sol - akt_pos
    #print ("tischpos", pos_ti, akt_pos, sol, dif)
    #taste.wait_for_bump('left')
    if dif < 0:
        dif = dif - 5
    else: dif = dif + 5
    if abs(dif) < 7:
        pass
    else:
        farbscan.tischdreh.on_for_degrees(20, dif)

def fl_unten_dr_r(r):  # der Tisch dreht die untere Fläche
    farbscan.gabelvors.on_for_degrees(30, 77)
    if r == 0:
        farbscan.tischdreh.on_for_degrees(30, 100)
    elif r == 1:
        farbscan.tischdreh.on_for_degrees(30, 95)
    else:
        farbscan.tischdreh.on_for_degrees(30, 90)
    #tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv) 

def fl_unten_dr_l(r):
    farbscan.gabelvors.on_for_degrees(30, 77)
    if r == 0:
        farbscan.tischdreh.on_for_degrees(30, -100)
    elif r == 1:
        farbscan.tischdreh.on_for_degrees(30, -95)
    else:
        farbscan.tischdreh.on_for_degrees(30, -90)
    #tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv)

def flaech_renum_l(i): # redefiniert die Farben auf der nach links gedrehten Fläche
    farblist = [fl[i][0], fl[i][1], fl[i][2], fl[i][3], fl[i][4], fl[i][5], fl[i][6], fl[i][7]]
    farblist.append(farblist.pop(0))
    farblist.append(farblist.pop(0))
    for j in range (8):
	    fl[i][j] = farblist[j]

def flaech_renum_r(i): # redefiniert die Farben auf der nach rechts gedrehten Fläche
    farblist = [fl[i][0], fl[i][1], fl[i][2], fl[i][3], fl[i][4], fl[i][5], fl[i][6], fl[i][7]]
    n = 6
    while n > 0:
        n -= 1
        farblist.append(farblist.pop(0))        
    for j in range (8):
	    fl[i][j] = farblist[j]
   
def renum_unten_r():   # redefiniert die Farben wenn unten nach rechts gedreht wird
    flaech_renum_r(2)
    farbliseit = [fl[4][0], fl[4][1], fl[4][2], fl[1][2], fl[1][3], fl[1][4], fl[5][0], fl[5][1], fl[5][2], fl[3][6], fl[3][7], fl[3][0]]
    farbliseit.append(farbliseit.pop(0))
    farbliseit.append(farbliseit.pop(0))
    farbliseit.append(farbliseit.pop(0))
    for j in range(3):
        fl[4][j] = farbliseit[j]
    for j in range(2,5):
        fl[1][j] = farbliseit[j+1]
    for j in range(3):
        fl[5][j] = farbliseit[j+6]
    fl[3][6] = farbliseit[9]
    fl[3][7] = farbliseit[10]
    fl[3][0] = farbliseit[11]

def renum_unten_l():   # redefiniert die Farben wenn unten nach links gedreht wird
    flaech_renum_l(2)
    farbliseit = [fl[3][0], fl[3][7], fl[3][6], fl[5][2], fl[5][1], fl[5][0], fl[1][4], fl[1][3], fl[1][2], fl[4][2], fl[4][1], fl[4][0]]
    farbliseit.append(farbliseit.pop(0))
    farbliseit.append(farbliseit.pop(0))
    farbliseit.append(farbliseit.pop(0))
    for j in range(3):
        fl[4][j] = farbliseit[11-j]
    for j in range(2,5):
        fl[1][j] = farbliseit[11-(j+1)]
    for j in range(3):
        fl[5][j] = farbliseit[11-(j+6)]
    fl[3][6] = farbliseit[2]
    fl[3][7] = farbliseit[1]
    fl[3][0] = farbliseit[0]
    
def renum_flae_dr_r(): # redefiniert die Farben wenn vorne nach rechts gedreht wird
    flaech_renum_r(4)
    farbliseit = [fl[0][0], fl[0][1], fl[0][2], fl[1][0], fl[1][1], fl[1][2], fl[2][0], fl[2][1], fl[2][2], fl[3][0], fl[3][1], fl[3][2]]
    farbliseit.append(farbliseit.pop(0))
    farbliseit.append(farbliseit.pop(0))
    farbliseit.append(farbliseit.pop(0))
    for i in range(4):
        for j in range(3):
            fl[i][j] = farbliseit[j+3*i]

def renum_flae_dr_l(): # redefiniert die Farben wenn vorne nach links gedreht wird
    flaech_renum_l(4)
    farbliseit = [fl[3][2], fl[3][1], fl[3][0], fl[2][2], fl[2][1], fl[2][0], fl[1][2], fl[1][1], fl[1][0], fl[0][2], fl[0][1], fl[0][0]]
    farbliseit.append(farbliseit.pop(0))
    farbliseit.append(farbliseit.pop(0))
    farbliseit.append(farbliseit.pop(0))
    for i in range(4):
        for j in range(3):
            fl[i][j] = farbliseit[11-(j+3*i)]

def renum_wue_dr_l(): # redefiniert die Farben wenn der ganze Würfel nach rechts gedreht wird
    flaech_renum_l(2) # unten
    flaech_renum_r(0) # oben
    f_seit = [fl[3][4], fl[3][5], fl[3][6], fl[3][3], fl[3][8], fl[3][7], fl[3][2], fl[3][1], fl[3][0], 
    fl[5][6], fl[5][7], fl[5][0], fl[5][5], fl[5][8], fl[5][1], fl[5][4], fl[5][3], fl[5][2],
    fl[1][0], fl[1][1], fl[1][2], fl[1][7], fl[1][8], fl[1][3], fl[1][6], fl[1][5], fl[1][4], 
    fl[4][6], fl[4][7], fl[4][0], fl[4][5], fl[4][8], fl[4][1], fl[4][4], fl[4][3], fl[4][2]] 
    for n in range(9):
        f_seit.append(f_seit.pop(0))
    #print (f_seit)
    fl[3][4]=f_seit[0]; fl[3][5]=f_seit[1]; fl[3][6]=f_seit[2]; fl[3][3]=f_seit[3]; fl[3][8]=f_seit[4]; fl[3][7]=f_seit[5]; fl[3][2]=f_seit[6]; fl[3][1]=f_seit[7]; fl[3][0]=f_seit[8]
    fl[5][6]=f_seit[9]; fl[5][7]=f_seit[10]; fl[5][0]=f_seit[11]; fl[5][5]=f_seit[12]; fl[5][8]=f_seit[13]; fl[5][1]=f_seit[14]; fl[5][4]=f_seit[15]; fl[5][3]=f_seit[16]; fl[5][2]=f_seit[17]
    fl[1][0]=f_seit[18]; fl[1][1]=f_seit[19]; fl[1][2]=f_seit[20]; fl[1][7]=f_seit[21]; fl[1][8]=f_seit[22]; fl[1][3]=f_seit[23]; fl[1][6]=f_seit[24]; fl[1][5]=f_seit[25]; fl[1][4]=f_seit[26] 
    fl[4][6]=f_seit[27]; fl[4][7]=f_seit[28]; fl[4][0]=f_seit[29]; fl[4][5]=f_seit[30]; fl[4][8]=f_seit[31]; fl[4][1]=f_seit[32]; fl[4][4]=f_seit[33]; fl[4][3]=f_seit[34]; fl[4][2]=f_seit[35]
    
def renum_wue_dr_r(): # redefiniert die Farben wenn der ganze Würfel nach rechts gedreht wird
    flaech_renum_r(2) # unten
    flaech_renum_l(0) # oben
    f_seit = [fl[3][4], fl[3][5], fl[3][6], fl[3][3], fl[3][8], fl[3][7], fl[3][2], fl[3][1], fl[3][0], 
    fl[4][6], fl[4][7], fl[4][0], fl[4][5], fl[4][8], fl[4][1], fl[4][4], fl[4][3], fl[4][2], 
    fl[1][0], fl[1][1], fl[1][2], fl[1][7], fl[1][8], fl[1][3], fl[1][6], fl[1][5], fl[1][4], 
    fl[5][6], fl[5][7], fl[5][0], fl[5][5], fl[5][8], fl[5][1], fl[5][4], fl[5][3], fl[5][2]]
    for n in range(9):
        f_seit.append(f_seit.pop(0))
    #print (f_seit)
    fl[3][4]=f_seit[0]; fl[3][5]=f_seit[1]; fl[3][6]=f_seit[2]; fl[3][3]=f_seit[3]; fl[3][8]=f_seit[4]; fl[3][7]=f_seit[5]; fl[3][2]=f_seit[6]; fl[3][1]=f_seit[7]; fl[3][0]=f_seit[8]
    fl[4][6]=f_seit[9]; fl[4][7]=f_seit[10]; fl[4][0]=f_seit[11]; fl[4][5]=f_seit[12]; fl[4][8]=f_seit[13]; fl[4][1]=f_seit[14]; fl[4][4]=f_seit[15]; fl[4][3]=f_seit[16]; fl[4][2]=f_seit[17]
    fl[1][0]=f_seit[18]; fl[1][1]=f_seit[19]; fl[1][2]=f_seit[20]; fl[1][7]=f_seit[21]; fl[1][8]=f_seit[22]; fl[1][3]=f_seit[23]; fl[1][6]=f_seit[24]; fl[1][5]=f_seit[25]; fl[1][4]=f_seit[26] 
    fl[5][6]=f_seit[27]; fl[5][7]=f_seit[28]; fl[5][0]=f_seit[29]; fl[5][5]=f_seit[30]; fl[5][8]=f_seit[31]; fl[5][1]=f_seit[32]; fl[5][4]=f_seit[33]; fl[5][3]=f_seit[34]; fl[5][2]=f_seit[35]

def dreh_seite_rr(): # dreht Tisch und dann Frontfläche (d.h. gedreht wird die ursprünglich rechte Seite)
    farbscan.tischdreh.on_for_degrees(20, -98)
    tisch_kor()
    renum_wue_dr_l()
    #farbscan.gabelvors.on_for_degrees(30, 77)
    #tisch_kor()
    sleep(.1)
    #farbscan.gabelvors.on_to_position(30, pos_gv)
    farbscan.flaech_dreh_r()
    renum_flae_dr_r()

def dreh_seite_rl(): # dreht Tisch und dann Frontfläche (d.h. gedreht wird die ursprünglich rechte Seite)
    farbscan.tischdreh.on_for_degrees(20, -98)
    renum_wue_dr_l()
    farbscan.gabelvors.on_for_degrees(30, 77)
    tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv)
    farbscan.flaech_dreh_l()
    renum_flae_dr_l()

def dreh_seite_lr(): # dreht Tisch und dann Frontfläche (d.h. gedreht wird die ursprünglich linke Seite)
    farbscan.tischdreh.on_for_degrees(20, 98)
    renum_wue_dr_r()
    #farbscan.gabelvors.on_for_degrees(30, 77)
    #tisch_kor()
    sleep(.1)
    #farbscan.gabelvors.on_to_position(30, pos_gv)
    farbscan.flaech_dreh_r()
    renum_flae_dr_r()

def dreh_seite_ll(): # dreht Tisch und dann Frontfläche (d.h. gedreht wird die ursprünglich linke Seite)
    farbscan.tischdreh.on_for_degrees(20, 98)
    renum_wue_dr_r()
    farbscan.gabelvors.on_for_degrees(30, 77)
    tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv)
    farbscan.flaech_dreh_l()
    renum_flae_dr_l()
    