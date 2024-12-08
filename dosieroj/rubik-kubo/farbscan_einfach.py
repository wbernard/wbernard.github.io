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


def oben_lesen(i): # iest die farben der obenliegenden Flächen
    farbscan.tischdreh.on_for_degrees(20, 47)
    for j in range(8): # liest oben
        sleep(0.15)
        farb_num = farbscan.farbsens.color
        if farb_num == 7:  # rot wird manchmal als braun erkannt
            farb_num = 5
        fl[i][7-j] = farb_num
        if j == 0:
            farbscan.tischdreh.on_for_degrees(30, -45)
        else:
            farbscan.tischdreh.on_for_degrees(30, -45.5)
    farbscan.tischdreh.on_to_position(40, pos_ti)

def alle_flaechen():
    i = -1
    while True:
        i += 1
        if i == 6:
            break
        oben_lesen(i)
        #print ("lese i =", i)
        #taste.wait_for_bump('left')
        print ("F", i, fl[i][0], fl[i][1], fl[i][2], fl[i][3], fl[i][4], fl[i][5], fl[i][6], fl[i][7], fl[i][8])
        print ("Wenn richtig druecke linke Taste,")
        print ("wenn nicht halte rechte Taste gedruckt und dann linke Taste")        
        taste.wait_for_bump('left')       
        if taste.right:
            i -= 1
            #print ("falsch i =", i)
            #taste.wait_for_bump('left')
        else:
            pass

