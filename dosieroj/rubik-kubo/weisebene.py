#!/usr/bin/env python3

import farbscan
import bewegrenum
from time import sleep
import os

taste = farbscan.Button()
ton = farbscan.Sound()
fl = farbscan.fl
pos_ti = farbscan.pos_ti
pos_gd = farbscan.pos_gd
pos_gv = farbscan.pos_gv

def weis_kant_o(): # sucht weiße Kanten auf der Oberseite und bringt sie nach unten 
    if fl[0][1] != 6 and fl[0][3] != 6 and fl[0][5] != 6 and fl[0][7] != 6: 
        pass 
    else:
        for i in range (4):
            #print ("  ")
            #farbscan.schreib_farb()
            #print ("in weiskant_o dr li Tast!")
            #taste.wait_for_bump('left')
            if fl[0][1] != 6:
                if i == 0:
                    farbscan.tischdreh.on_for_degrees(30, -96)
                else:
                    farbscan.tischdreh.on_for_degrees(30, -90)
                sleep(.1)
                bewegrenum.renum_wue_dr_l()
                farbscan.gabelvors.on_for_degrees(30, 78)
                bewegrenum.tisch_kor()
                sleep(.1)
                farbscan.gabelvors.on_to_position(30, pos_gv)
            elif fl[2][1] != 6:
                for j in range (2):
                    farbscan.flaech_dreh_l()
                    bewegrenum.renum_flae_dr_l()
                    sleep(0.1)
            else:
                if i == 0 or i == 1:
                    bewegrenum.fl_unten_dr_r(i)
                else:
                    bewegrenum.fl_unten_dr_r(2)
                sleep(0.1)    
                bewegrenum.renum_unten_r()             
            

def weis_kant_v(): # sucht weiße Kanten auf der Vorderseite und bringt sie nach unten
    for i in range (4):
        #print ("  ")
        #farbscan.schreib_farb()
        #print ("in weiskant_v dr li Tast!")
        #taste.wait_for_bump('left')
        if fl[4][1] != 6 and fl[4][3] != 6 and fl[4][5] != 6 and fl[4][7] != 6:
            if i == 0:
                farbscan.tischdreh.on_for_degrees(30, -95)
            else:
                farbscan.tischdreh.on_for_degrees(30, -90)
            bewegrenum.renum_wue_dr_l()
            farbscan.gabelvors.on_for_degrees(30, 78)
            bewegrenum.tisch_kor()
            sleep(.1)
            farbscan.gabelvors.on_to_position(30, pos_gv)      
        else:
            for j in range (1,8,2):
                #print ("  ")
                #farbscan.schreib_farb()
                #print ("weiskant_v j",j," dr li Tast!")
                #taste.wait_for_bump('left')                    
                if fl[4][j] != 6:
                    pass
                elif j == 1:
                    if fl[2][3] != 6:
                        farbscan.flaech_dreh_l()
                        bewegrenum.renum_flae_dr_l()
                        bewegrenum.dreh_seite_rl()
                        sleep(.1)
                        farbscan.tischdreh.on_for_degrees(30, 93)
                        bewegrenum.renum_wue_dr_r()
                        farbscan.gabelvors.on_for_degrees(30, 78)
                        bewegrenum.tisch_kor()
                        sleep(.1)
                        farbscan.gabelvors.on_to_position(30, pos_gv)
                        farbscan.flaech_dreh_r()
                        bewegrenum.renum_flae_dr_r()
                    elif fl[2][7] != 6:
                        farbscan.flaech_dreh_r()
                        bewegrenum.renum_flae_dr_r()
                        bewegrenum.dreh_seite_lr()
                        farbscan.tischdreh.on_for_degrees(30, -93)
                        bewegrenum.renum_wue_dr_l()
                        farbscan.gabelvors.on_for_degrees(30, 78)
                        bewegrenum.tisch_kor()
                        sleep(.1)
                        farbscan.gabelvors.on_to_position(30, pos_gv)
                        farbscan.flaech_dreh_l()
                        bewegrenum.renum_flae_dr_l()
                    else:
                        farbscan.flaech_dreh_r()
                        bewegrenum.renum_flae_dr_r()
                        bewegrenum.fl_unten_dr_r(1)
                        bewegrenum.renum_unten_r()

                elif j == 3:
                    if fl[2][7] != 6:
                        bewegrenum.dreh_seite_lr()
                        farbscan.tischdreh.on_for_degrees(30, -93)
                        bewegrenum.renum_wue_dr_l()
                        farbscan.gabelvors.on_for_degrees(30, 78)
                        bewegrenum.tisch_kor()
                        sleep(.1)
                        farbscan.gabelvors.on_to_position(30, pos_gv)
                    else:
                        bewegrenum.fl_unten_dr_r(1)
                        sleep(.1)
                        bewegrenum.renum_unten_r()   
                elif j == 5:
                    if fl[2][7] != 6:
                        farbscan.flaech_dreh_l()
                        bewegrenum.renum_flae_dr_l()
                        bewegrenum.dreh_seite_lr()
                        farbscan.tischdreh.on_for_degrees(30, -93)
                        bewegrenum.renum_wue_dr_l()
                        farbscan.gabelvors.on_for_degrees(30, 78)
                        bewegrenum.tisch_kor()
                        sleep(.1)
                        farbscan.gabelvors.on_to_position(30, pos_gv)
                        farbscan.flaech_dreh_r()
                        bewegrenum.renum_flae_dr_r()
                    elif fl[2][3] != 6:
                        farbscan.flaech_dreh_r()
                        bewegrenum.renum_flae_dr_r()
                        bewegrenum.dreh_seite_rl()
                        farbscan.tischdreh.on_for_degrees(30, 93)
                        bewegrenum.renum_wue_dr_r()
                        farbscan.gabelvors.on_for_degrees(30, 78)
                        bewegrenum.tisch_kor()
                        sleep(.1)
                        farbscan.gabelvors.on_to_position(30, pos_gv)
                        farbscan.flaech_dreh_l()
                        bewegrenum.renum_flae_dr_l()
                    elif fl[2][1] != 6:
                        farbscan.flaech_dreh_r()
                        bewegrenum.renum_flae_dr_r()
                        bewegrenum.fl_unten_dr_r(1)
                        bewegrenum.renum_unten_r()
                        bewegrenum.dreh_seite_rl()
                        farbscan.tischdreh.on_for_degrees(30, 93)
                        bewegrenum.renum_wue_dr_r()
                        farbscan.gabelvors.on_for_degrees(30, 78)
                        bewegrenum.tisch_kor()
                        sleep(.1)
                        farbscan.gabelvors.on_to_position(30, pos_gv)
                        farbscan.flaech_dreh_l()
                        bewegrenum.renum_flae_dr_l()
                    else:
                        bewegrenum.fl_unten_dr_r(1)
                        bewegrenum.renum_unten_r()                     
                elif j == 7:
                    if fl[2][3] != 6:
                        farbscan.gabelvors.on_for_degrees(30, 78)
                        bewegrenum.tisch_kor()
                        sleep(.1)
                        farbscan.gabelvors.on_to_position(30, pos_gv)
                        bewegrenum.dreh_seite_rl()
                        farbscan.tischdreh.on_for_degrees(30, 92)
                        bewegrenum.renum_wue_dr_r()
                        farbscan.gabelvors.on_for_degrees(30, 78)
                        bewegrenum.tisch_kor()
                        sleep(.1)
                        farbscan.gabelvors.on_to_position(30, pos_gv)
                    else:
                        bewegrenum.fl_unten_dr_r(2)
                        bewegrenum.renum_unten_r() 
        farbscan.gabelvors.on_for_degrees(30, 78)
        bewegrenum.tisch_kor()
        sleep(.1)
        farbscan.gabelvors.on_to_position(30, pos_gv)
                        
def weiskreuz():  # bringt das weiße Kreuz nach oben
    while not (fl[2][1] == 6 and fl[2][3] == 6 and fl[2][5] == 6 and fl[2][7] == 6):        
        weis_kant_o()
        
        weis_kant_v()

        #print ("  ")
        #farbscan.schreib_farb()
        #print ("in weiskreuz dr li Tast!")
        #taste.wait_for_bump('left')
    while not (fl[0][1] == 6 and fl[0][3] == 6 and fl[0][5] == 6 and fl[0][7] == 6):
        for i in range (4):
            for j in range (4):
                #print ("  ") 
                #farbscan.schreib_farb()
                #print ("in weiskr", i, j, "dr li Tast!")
                #taste.wait_for_bump('left')
                if fl[0][1] == 6:
                    break
                elif (fl[4][1] == fl[4][8]) and fl[2][1] == 6:                    
                    for k in range (2):
                        farbscan.flaech_dreh_l()
                        bewegrenum.renum_flae_dr_l()
                        sleep(0.1)                    
                else: 
                    if j == 0 or j == 1:
                        bewegrenum.fl_unten_dr_r(j)
                    else:
                        bewegrenum.fl_unten_dr_r(2)
                    bewegrenum.renum_unten_r()                
                    farbscan.gabelvors.on_for_degrees(30, 78)
                    bewegrenum.tisch_kor()
                    sleep(.1)
                    farbscan.gabelvors.on_to_position(30, pos_gv)
            if i == 0:
                farbscan.tischdreh.on_for_degrees(30, 96)
            else:
                farbscan.tischdreh.on_for_degrees(30, 90)
            bewegrenum.renum_wue_dr_r()
            farbscan.gabelvors.on_for_degrees(30, 78)
            bewegrenum.tisch_kor()
            sleep(.1)
            farbscan.gabelvors.on_to_position(30, pos_gv)  

def bew_weiseck_r():  # für weiße Ecken rechts
    bewegrenum.dreh_seite_rl()
    farbscan.tischdreh.on_for_degrees(30, 92)
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv)
    bewegrenum.renum_wue_dr_r()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv)
    bewegrenum.fl_unten_dr_l(1)
    bewegrenum.renum_unten_l()  
    bewegrenum.dreh_seite_rr()
    farbscan.tischdreh.on_for_degrees(30, 92)
    bewegrenum.renum_wue_dr_r()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv)

def bew_weiseck_l():  # für weiße Ecken links
    bewegrenum.dreh_seite_lr()
    farbscan.tischdreh.on_for_degrees(30, -92)
    bewegrenum.renum_wue_dr_l()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv)
    bewegrenum.fl_unten_dr_r(2)
    bewegrenum.renum_unten_r()  
    bewegrenum.dreh_seite_ll()
    farbscan.tischdreh.on_for_degrees(30, -92)
    bewegrenum.renum_wue_dr_l()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv)

def weisse_ecken():
    for i in range (4):
        if ((fl[0][0] == fl[0][2] == fl[0][4] == fl[0][6] == 6) and (fl[4][4] == fl[4][8]) and 
        (fl[1][6] == fl[1][8]) and (fl[5][4] == fl[5][8]) and (fl[3][2] == fl[3][8])):
            pass
        else:    
            for j in range (4):
                # rechte Ecken
                if (fl[3][0] == 6) and (fl[4][0] == fl[4][8] and fl[2][2] == fl[3][8]) or (fl[4][0] == fl[3][8] and fl[2][2] == fl[4][8]):
                    bew_weiseck_r()
                elif (fl[2][2] == 6) and (fl[4][0] == fl[4][8] and fl[3][0] == fl[3][8]) or (fl[4][0] == fl[3][8] and fl[3][0] == fl[4][8]):
                    bew_weiseck_r()
                    sleep(.1)
                    bew_weiseck_r()
                    if j == 0 or j == 1:
                        bewegrenum.fl_unten_dr_r(j)
                    else:
                        bewegrenum.fl_unten_dr_r(2)
                    bewegrenum.renum_unten_r()
                    bew_weiseck_r()
                elif fl[4][0] == 6 and ((fl[2][2] == fl[4][8] and fl[3][0] == fl[3][8]) or (fl[2][2] == fl[3][8] and fl[3][0] == fl[4][8])):
                    farbscan.tischdreh.on_for_degrees(30, -99)
                    bewegrenum.renum_wue_dr_l()
                    farbscan.gabelvors.on_for_degrees(30, 78)
                    bewegrenum.tisch_kor()
                    sleep(.1)
                    farbscan.gabelvors.on_to_position(30, pos_gv)
                    bew_weiseck_l()
                elif (fl[4][6] != fl[4][8]) and ((fl[4][6] == 6) or (fl[0][0] == 6) or (fl[3][2] == 6)):
                    bew_weiseck_r()
                    # linke Ecken
                elif (fl[1][2] == 6) and ((fl[4][2] == fl[4][8] and fl[2][0] == fl[1][8]) or (fl[4][2] == fl[1][8] and fl[2][0] == fl[4][8])):
                    bew_weiseck_l()
                elif (fl[2][0] == 6) and ((fl[4][2] == fl[4][8] and fl[1][2] == fl[1][8]) or (fl[4][2] == fl[1][8] and fl[1][2] == fl[4][8])):
                    bew_weiseck_l()
                    sleep(.1)
                    bew_weiseck_l()
                    bewegrenum.fl_unten_dr_l(1)
                    bewegrenum.renum_unten_l()
                    bew_weiseck_l()
                elif (fl[4][2] == 6) and ((fl[2][0] == fl[4][8] and fl[1][2] == fl[1][8]) or (fl[2][0] == fl[1][8] and fl[1][2] == fl[4][8])):
                    farbscan.tischdreh.on_for_degrees(30, 98)
                    bewegrenum.renum_wue_dr_r()
                    farbscan.gabelvors.on_for_degrees(30, 78)
                    bewegrenum.tisch_kor()
                    sleep(.1)
                    farbscan.gabelvors.on_to_position(30, pos_gv)
                    bew_weiseck_r()
                elif (fl[4][4] != fl[4][8]) and ((fl[4][4] == 6) or (fl[0][2] == 6) or (fl[1][0] == 6)):
                    bew_weiseck_l()
                else:
                    if j == 0 or j == 1:
                        bewegrenum.fl_unten_dr_r(j)
                    else:
                        bewegrenum.fl_unten_dr_r(2)
                    bewegrenum.renum_unten_r()
                    farbscan.gabelvors.on_for_degrees(30, 78)
                    bewegrenum.tisch_kor()
                    sleep(.1)
                    farbscan.gabelvors.on_to_position(30, pos_gv)
        farbscan.tischdreh.on_for_degrees(30, -92)
        bewegrenum.renum_wue_dr_l()
        farbscan.gabelvors.on_for_degrees(30, 78)
        bewegrenum.tisch_kor()
        sleep(.1)
        farbscan.gabelvors.on_to_position(30, pos_gv)            

