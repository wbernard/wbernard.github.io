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

def beweg_um_l(): # bringt Kante von unten Mitte nach links Mitte oder 
    # von links Mitte nach unten Mitte hinten
    bewegrenum.fl_unten_dr_r(1)  # dreht Unterseite nach rechts
    bewegrenum.renum_unten_r()
    bewegrenum.dreh_seite_lr()  # dreht linke Seite nach rechts
    sleep(.1)
    farbscan.tischdreh.on_for_degrees(20, -98) # dreht Tisch zurück
    bewegrenum.renum_wue_dr_l()
    #bewegrenum.tisch_kor()
    sleep(.1)
    bewegrenum.fl_unten_dr_l(1) # dreht Unterseite nach links
    bewegrenum.renum_unten_l()
    bewegrenum.dreh_seite_ll() # dreht linke Seite nach links
    sleep(.1)
    farbscan.tischdreh.on_for_degrees(20, -95) # dreht Tisch zurück
    bewegrenum.renum_wue_dr_l()
    sleep(.1)
    bewegrenum.fl_unten_dr_l(1)  # dreht Unterseite nach links
    bewegrenum.renum_unten_l()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv) 
    farbscan.flaech_dreh_l()    # dreht Vorderseite nach links
    bewegrenum.renum_flae_dr_l()
    sleep(.1)
    bewegrenum.fl_unten_dr_r(0)  # dreht Unterseite nach rechts
    bewegrenum.renum_unten_r()
    farbscan.flaech_dreh_r()  # dreht Vorderseite nach rechts
    bewegrenum.renum_flae_dr_r()
    #farbscan.schreib_farb()
    #print ("bew_um_l  dr li Tast!")
    #taste.wait_for_bump('left')  

def beweg_um_r(): # bringt Kante von unten Mitte nach rechts Mitte oder
    # von rechts Mitte nach unten Mitte hinten
    bewegrenum.fl_unten_dr_l(1)  # dreht Unterseite nach links
    bewegrenum.renum_unten_l()
    bewegrenum.dreh_seite_rl()  # dreht rechte Seite nach links
    sleep(.1)
    farbscan.tischdreh.on_for_degrees(30, 98) # dreht Tisch zurück
    bewegrenum.renum_wue_dr_r()
    bewegrenum.tisch_kor()
    bewegrenum.fl_unten_dr_r(1) # dreht Unterseite nach rechts
    bewegrenum.renum_unten_r()
    bewegrenum.dreh_seite_rr() # dreht rechte Seite nach rechts
    sleep(.1)
    farbscan.tischdreh.on_for_degrees(30, 95) # dreht Tisch zurück
    bewegrenum.renum_wue_dr_r()
    bewegrenum.fl_unten_dr_r(1)  # dreht Unterseite nach rechts
    bewegrenum.renum_unten_r()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv)  
    farbscan.flaech_dreh_r()    # dreht Vorderseite nach rechts
    bewegrenum.renum_flae_dr_r()
    bewegrenum.fl_unten_dr_l(0)  # dreht Unterseite nach links
    bewegrenum.renum_unten_l()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv) 
    farbscan.flaech_dreh_l()  # dreht Vorderseite nach links
    bewegrenum.renum_flae_dr_l()
    #farbscan.schreib_farb()
    #print ("bew_um_r  dr li Tast!")
    #taste.wait_for_bump('left')  

def mitt_kant_unt(): # stellt Kanten von unten auf mittlere Ebene
    for i in range (4):
        if ((fl[4][3] == fl[4][8] == fl[4][7]) and (fl[1][5] == fl[1][8] == fl[1][1]) and (fl[5][3] == fl[5][8] == fl[5][7]) and (fl[3][1] == fl[3][8] == fl[3][5])):
            break
        else:
            for j in range(4):
                if ((fl[4][3] == fl[4][8] == fl[4][7]) and (fl[1][5] == fl[1][8] == fl[1][1]) and (fl[5][3] == fl[5][8] == fl[5][7]) and (fl[3][1] == fl[3][8] == fl[3][5])):
                    break
                elif (fl[4][1] == fl[4][8]) and (fl[2][1] == fl[1][8]):
                    beweg_um_l()
                elif (fl[4][1] == fl[4][8]) and (fl[2][1] == fl[3][8]):
                    beweg_um_r()
                else:
                    if j == 0 or j == 1:
                        bewegrenum.fl_unten_dr_r(j+1)  # dreht Unterseite nach rechts
                    else:
                        bewegrenum.fl_unten_dr_r(2) 
                    bewegrenum.renum_unten_r()         
        farbscan.tischdreh.on_for_degrees(30, -93)
        bewegrenum.renum_wue_dr_l()
        
        farbscan.gabelvors.on_for_degrees(30, 78)
        bewegrenum.tisch_kor()
        sleep(.1)
        farbscan.gabelvors.on_to_position(30, pos_gv)
       

def mitt_kant_fals(): # stellt falsche Kanten von mittlerer Ebene nach unten
    for i in range(4):
        #farbscan.schreib_farb()
        #print ("mit_kant f3,1 f3,8", fl[3][1], fl[3][8], " dr li Tast!")
        #taste.wait_for_bump('left')
        if ((fl[4][3] == fl[4][8] == fl[4][7]) and (fl[1][1] == fl[1][8] == fl[1][5]) and (fl[5][3] == fl[5][8] == fl[5][7]) and (fl[3][5] == fl[3][8] == fl[3][1])):
            break
        else: 
            if (fl[4][3] != fl[4][8]) or (fl[1][1] != fl[1][8]):
                beweg_um_l()
            elif (fl[4][7] != fl[4][8]) or (fl[3][1] != fl[3][8]):
                beweg_um_r()
            else:
                farbscan.tischdreh.on_for_degrees(30, -92)
                bewegrenum.renum_wue_dr_l()
                farbscan.gabelvors.on_for_degrees(30, 78)
                bewegrenum.tisch_kor()
                sleep(.1)
                farbscan.gabelvors.on_to_position(30, pos_gv)
  
def mitt_eben_komp():
    mitt_kant_unt()
    #farbscan.schreib_farb()
    #print ("nach unt_kant dr li Tast!")
    #taste.wait_for_bump('left')
    if ((fl[4][3] == fl[4][8] == fl[4][8]) and (fl[1][1] == fl[1][8] == fl[1][5]) and (fl[5][3] == fl[5][8] == fl[5][7]) and (fl[3][5] == fl[3][8] == fl[3][1])):
        pass
    else:
        mitt_kant_fals()
       
        




