#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_A
from ev3dev2.motor import MediumMotor, OUTPUT_C
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from time import sleep
import os

os.system('setfont Lat15-TerminusBold14')

tischdreh = LargeMotor(OUTPUT_A)
gabeldreh = LargeMotor(OUTPUT_B)
gabelvors = MediumMotor(OUTPUT_C)

farbsens = ColorSensor()
taste = Button()
ton = Sound()

# ungeordnet1
fl = [[2, 4, 5, 6, 3, 3, 6, 2, 6], [2, 1, 4, 3, 5, 2, 5, 1, 2], [3, 2, 5, 3, 6, 4, 2, 1, 4], [6, 6, 1, 5, 1, 5, 1, 5, 3], [3, 4, 1, 2, 6, 5, 4, 3, 1], [4, 1, 2, 6, 3, 4, 4, 6, 5]]
# ungeordnet2
#fl = [[5, 1, 2, 2, 5, 2, 4, 2, 6], [1, 4, 3, 6, 4, 6, 4, 4, 2], [6, 1, 5, 3, 5, 1, 2, 5, 4], [4, 3, 3, 1, 3, 4, 6, 5, 3], [2, 6, 1, 5, 6, 3, 6, 6, 1], [1, 4, 2, 3, 1, 5, 3, 2, 5]]
# ungeordnet3
#fl = [[6, 2, 1, 6, 3, 2, 1, 2, 6], [2, 4, 6, 5, 1, 5, 5, 2, 2], [1, 6, 2, 3, 4, 1, 2, 4, 4], [6, 4, 5, 1, 4, 6, 5, 6, 3], [5, 5, 3, 3, 4, 4, 3, 1, 1], [6, 3, 2, 1, 3, 5, 4, 3, 5]]
# weißes Kreuz fertig
#fl = [[4, 6, 5, 6, 1, 6, 3, 6, 6], [1, 5, 3, 4, 5, 4, 2, 2, 2], [4, 3, 2, 3, 1, 1, 2, 1, 4], [6, 1, 6, 3, 6, 2, 2, 4, 3], [5, 5, 5, 2, 4, 1, 3, 3, 1], [4, 2, 6, 4, 3, 5, 1, 5, 5]]
# weiße Ebene fertig
#fl = [[6, 6, 6, 6, 6, 6, 6, 6, 6], [2, 2, 3, 4, 4, 5, 2, 2, 2], [4, 4, 4, 4, 3, 2, 5, 3, 4], [1, 3, 3, 3, 3, 3, 4, 2, 3], [2, 1, 5, 1, 1, 1, 1, 1, 1], [2, 5, 1, 5, 5, 5, 5, 4, 5]]
# bis weiße Ebene 
#fl = [[6, 6, 6, 6, 6, 6, 6, 6, 6], [5, 3, 5, 2, 5, 2, 5, 2, 2], [4, 4, 4, 4, 4, 4, 4, 5, 4], [1, 3, 3, 3, 2, 2, 1, 5, 3], [2, 1, 2, 5, 2, 1, 1, 1, 1], [3, 3, 3, 1, 1, 5, 3, 4, 5]]
# bis gelbe Fläche unten fertig 
#fl = [[6, 6, 6, 6, 6, 6, 6, 6, 6], [2, 2, 2, 5, 2, 2, 2, 2, 2], [4, 4, 4, 4, 4, 4, 4, 4, 4], [3, 3, 3, 3, 3, 3, 3, 3, 3], [1, 2, 1, 1, 1, 1, 1, 1, 1], [5, 1, 5, 5, 5, 5, 5, 5, 5]]
#fl = [[0, 0, 0, 0, 0, 0, 0, 0, 6], [0, 0, 0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 4], [0, 0, 0, 0, 0, 0, 0, 0, 3], [0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 5]]
#Reihenfolge der Flächen: Oben, Links, Unten, Rechts, Vorne, Hinten von der Gabel aus

tischdreh.on_for_degrees(30, 2)   # Tisch steht mit Vorderseite senkrecht zur Gabel und ist blockiert
sleep(.1)
pos_ti = tischdreh.position         

gabeldreh.on_for_degrees(30, -2)  # Gabel ist bis zum Anschlag nach links gedreht 
sleep(.1)
pos_gd = gabeldreh.position + 67   # 67° ist die Mitte zu der die Gabel stets zurückkehrt

gabelvors.on_for_degrees(30, -2)  # Gabel ist hinten am Anschlag
sleep(.1)
pos_gv = gabelvors.position         # Gabel ist ganz hinten

print ("Blockierung von Tisch entfernen")
print ("dann linke Taste druecken!")

taste.wait_for_bump('left')

gabeldreh.on_to_position(30, pos_gd)  #Gabel wird auf Mitte gestellt
sleep(0.1)

def flaech_dreh_r():  #dreht vordere Fläche im Uhrzeigersinn
    gabeldreh.on_to_position(30, pos_gd)
    gabeldreh.on_for_degrees(21,-60)
    gabelvors.on_for_degrees(30, 77)
    gabeldreh.on_for_degrees(30, 93)
    gabeldreh.on_to_position(30, pos_gd)
    gabelvors.on_to_position(30, pos_gv)

def flaech_dreh_l():  #dreht vordere Fläche im Gegenuhrzeigersinn
    gabeldreh.on_to_position(30, pos_gd)
    gabeldreh.on_for_degrees(21, 60)
    gabelvors.on_for_degrees(30, 77)
    gabeldreh.on_for_degrees(30,-93)
    gabeldreh.on_to_position(30, pos_gd)
    gabelvors.on_to_position(30, pos_gv) 

def oben_lesen(i): # liest die farben der obenliegenden Flächen
    tischdreh.on_for_degrees(30, 50)
    for j in range(8): # liest oben
        sleep(0.1)
        farb_num = farbsens.color
        if farb_num == 7:  # rot wird manchmal als braun erkannt
            farb_num = 5
        fl[i][7-j] = farb_num
        if j == 0:
            tischdreh.on_for_degrees(30, -50)
        else:
            tischdreh.on_for_degrees(30, -45)
        sleep(0.1)
    tischdreh.on_to_position(40, pos_ti)
    sleep(0.1)

def lies_kant_v():
    for i in range(4): # liest Kanten von Vorderseite links, unten, rechts
        if i != 0:
            tischdreh.on_for_degrees(30, 85)
            sleep(0.1)
            farb_num = farbsens.color 
            fl[i][0] = farb_num 
            tischdreh.on_for_degrees(30, 55)
            sleep(0.1)
            farb_num = farbsens.color 
            fl[i][1] = farb_num
            tischdreh.on_for_degrees(30, 35)
            sleep(0.1)
            farb_num = farbsens.color 
            fl[i][2] = farb_num     
            tischdreh.on_to_position(40, pos_ti)
            sleep(.1)
        flaech_dreh_r()

def lies_kant_h(): # liest Kanten von Hinterseite links, unten, rechts
    tischdreh.on_for_degrees(30, 180)
    sleep(.1)
    for i in range(4): 
        if i != 0:
            tischdreh.on_for_degrees(30, 85)
            sleep(0.1)
            farb_num = farbsens.color 
            fl[4-i][4] = farb_num 
            tischdreh.on_for_degrees(30, 55)
            sleep(0.1)
            farb_num = farbsens.color 
            fl[4-i][5] = farb_num
            tischdreh.on_for_degrees(30, 35)
            sleep(0.1)
            farb_num = farbsens.color 
            fl[4-i][6] = farb_num     
            tischdreh.on_for_degrees(40, -175)
            sleep(.1)
        flaech_dreh_r()

def lies_kant_l():   # liest ganze Kanten von linker Seite hinten, unten, vorn
    tischdreh.on_for_degrees(30, -90)
    sleep(.1)
    for i in range(4): 
        if i != 0:
            tischdreh.on_for_degrees(30, 85)
            sleep(0.1)
            farb_num = farbsens.color
            if i == 1:  # hinten ist oben
                fl[5][6] = farb_num 
            elif i == 2:         
                fl[2][6] = farb_num
            else:
                fl[4][2] = farb_num
            tischdreh.on_for_degrees(30, 55)
            sleep(0.1)
            farb_num = farbsens.color 
            if i == 1:  
                fl[5][7] = farb_num 
            elif i == 2:         
                fl[2][7] = farb_num
            else:
                fl[4][3] = farb_num                 
            tischdreh.on_for_degrees(30, 35)
            sleep(0.1)
            farb_num = farbsens.color 
            if i == 1:  
                fl[5][0] = farb_num 
            elif i == 2:         
                fl[2][0] = farb_num
            else:
                fl[4][4] = farb_num 
            tischdreh.on_for_degrees(40, -175)
            sleep(.1)
        flaech_dreh_r()
    

def lies_kant_r():  # liest Kanten von rechter Seite vorn, unten, hinten 
    #tischdreh.on_to_position(40, pos_ti) 
    tischdreh.on_for_degrees(30, -180)
    sleep(.1)  
    for i in range(4): 
        if i != 0:
            tischdreh.on_for_degrees(30, 85)
            sleep(0.1)
            farb_num = farbsens.color
            if i == 1:  # vorne ist oben
                fl[4][6] = farb_num 
            elif i == 2:         
                fl[2][2] = farb_num
            else:
                fl[5][2] = farb_num
            tischdreh.on_for_degrees(30, 55)
            sleep(0.1)
            farb_num = farbsens.color 
            if i == 1:  
                fl[4][7] = farb_num 
            elif i == 2:         
                fl[2][3] = farb_num
            else:
                fl[5][3] = farb_num                 
            tischdreh.on_for_degrees(30, 35)
            sleep(0.1)
            farb_num = farbsens.color 
            if i == 1:  
                fl[4][0] = farb_num 
            elif i == 2:         
                fl[2][4] = farb_num
            else:
                fl[5][4] = farb_num 
            tischdreh.on_for_degrees(40, -175)
            sleep(.1)
        flaech_dreh_r()

def lies_kante_vh(vh): #liest Farbe der Kanten vorn (4,1 und 4,5) und hinten (5,1 und 5,5)

    flaech_dreh_r()
    tischdreh.on_for_degrees(30, -90)
    sleep(.1)
    flaech_dreh_r() 
    tischdreh.on_for_degrees(30, 140)
    sleep(0.1)
    farb_num = farbsens.color 
    fl[vh][5] = farb_num

    tischdreh.on_for_degrees(30, 45)
    sleep(.1)
    flaech_dreh_l()
    tischdreh.on_for_degrees(30, 140)
    sleep(0.1)
    farb_num = farbsens.color 
    fl[vh][1] = farb_num 
    tischdreh.on_for_degrees(30, -140)
    sleep(.1)
    flaech_dreh_r()
    tischdreh.on_for_degrees(30, -185)
    sleep(.1)
    flaech_dreh_l()
    tischdreh.on_for_degrees(30, 90)
    sleep(.1)
    flaech_dreh_l()

def lies_kante_lr(lr): #liest Farbe der Kanten links (1,3 und 1,7) und rechts (3,3 und 3,7)
    #tischdreh.on_to_position(40, pos_ti)
    #tischdreh.on_for_degrees(30, 90)
    flaech_dreh_r()
    tischdreh.on_for_degrees(30, -90)
    sleep(.1)
    flaech_dreh_r() 
    tischdreh.on_for_degrees(30, 140)
    sleep(0.1)
    farb_num = farbsens.color 
    if lr == 1:
        fl[lr][7] = farb_num
    else:
        fl[lr][3] = farb_num 

    tischdreh.on_for_degrees(30, 45)
    sleep(.1)
    flaech_dreh_l()
    tischdreh.on_for_degrees(30, 140)
    sleep(0.1)
    farb_num = farbsens.color 
    if lr == 1:
        fl[lr][3] = farb_num
    else:
        fl[lr][7] = farb_num
    tischdreh.on_for_degrees(30, -140)
    sleep(.1)
    flaech_dreh_r()
    tischdreh.on_for_degrees(30, -185)
    sleep(.1)
    flaech_dreh_l()
    tischdreh.on_for_degrees(30, 90)
    sleep(.1)
    flaech_dreh_l()  
    #tischdreh.on_to_position(40, pos_ti)

def lies_farben1(): # liest die Farbe Oben Unten und von den Kanten
    
    oben_lesen(0)

    #print ("nach oben l dr. linke Taste!")
    #taste.wait_for_bump('left')
    lies_kant_v()

    #print ("nach kant_v dr linke Taste!")
    #taste.wait_for_bump('left')
    
    lies_kant_h()

    #print ("nach kant_h dr linke Taste!")
    #taste.wait_for_bump('left')

    
    lies_kant_l()

    #print ("nach kant_l linke Taste!")
    #taste.wait_for_bump('left')

    lies_kant_r()

    #schreib_farb()
    #print ("nach kant_r linke Taste!")
    #taste.wait_for_bump('left')


def lies_farben2(): # liest die Farbe der seitlichen Ecken
    tischdreh.on_to_position(30, pos_ti)
    sleep(.1)
    lies_kante_vh(4)

    #print ("nach kanten_vh4 linke Taste!")
    #taste.wait_for_bump('left')
  
    tischdreh.on_for_degrees(30, -180)
    sleep(.1)
    lies_kante_vh(5)

    #schreib_farb()
    #print ("nach kanten_vh5 linke Taste!")
    #taste.wait_for_bump('left')

    tischdreh.on_for_degrees(30, -90)
    sleep(.1)
    lies_kante_lr(1)  

    tischdreh.on_for_degrees(30, 180)
    sleep(.1)
    
    lies_kante_lr(3)
    

def farbe_einles():  # liest die Farben ein
    lies_farben1()
    sleep(0.1)
    lies_farben2()
    tischdreh.on_to_position(40, pos_ti)
    sleep(.1)
    schreib_farb()
    #print ("nach fa-einl dr li Tast!")
    #taste.wait_for_bump('left')
    #farb_kontrol()

def farb_kontrol():  # kontrolliert ob Farben richtig sind
    sw = bl = gr = ge = ro = we = 0
    for i in range(6):
        for j in range(8):
            if fl[i][j] == 7:  # rot wird manchmal als braun erkannt
                fl[i][j] = 5
    for i in range(6):
        for j in range(8):
            if fl[i][j] == 1:
                sw = sw + 1
            elif fl[i][j] == 2:
                bl = bl + 1    
            elif fl[i][j] == 3:
                gr = gr + 1
            elif fl[i][j] == 4:
                ge = ge + 1
            elif fl[i][j] == 5:
                ro = ro + 1
            elif fl[i][j] == 6:
                we = we + 1
            else:
                print ("farbe falsch wh dr li Tast!")
                taste.wait_for_bump('left')
                farbe_einles()
    if sw == bl == gr == ge == ro == we == 8:
        pass
    else:
        print (sw, bl, gr, ge, ro, we,"summe falsch wh dr li Tast!")
        taste.wait_for_bump('left')
        farbe_einles()
        farb_kontrol()
    
  
def schreib_farb():
    print('O: ', fl[0][0], fl[0][1], fl[0][2], fl[0][3], fl[0][4], fl[0][5], fl[0][6], fl[0][7], fl[0][8])
    print('L: ', fl[1][0], fl[1][1], fl[1][2], fl[1][3], fl[1][4], fl[1][5], fl[1][6], fl[1][7], fl[1][8])
    print('U: ', fl[2][0], fl[2][1], fl[2][2], fl[2][3], fl[2][4], fl[2][5], fl[2][6], fl[2][7], fl[2][8]) 
    print('R: ', fl[3][0], fl[3][1], fl[3][2], fl[3][3], fl[3][4], fl[3][5], fl[3][6], fl[3][7], fl[3][8])
    print('V: ', fl[4][0], fl[4][1], fl[4][2], fl[4][3], fl[4][4], fl[4][5], fl[4][6], fl[4][7], fl[4][8])
    print('H: ', fl[5][0], fl[5][1], fl[5][2], fl[5][3], fl[5][4], fl[5][5], fl[5][6], fl[5][7], fl[5][8])
