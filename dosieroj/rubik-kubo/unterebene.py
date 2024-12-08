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

def beweg_gelb_kr(): # bringt gelbe Kante in Position
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv) 
    farbscan.flaech_dreh_r()    # dreht Vorderseite nach rechts
    bewegrenum.renum_flae_dr_r()
    bewegrenum.fl_unten_dr_r(1)  # dreht Unterseite nach rechts
    bewegrenum.renum_unten_r()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv) 
    bewegrenum.dreh_seite_lr()  # dreht linke Seite nach rechts
    farbscan.tischdreh.on_for_degrees(30, -95) # dreht Tisch
    bewegrenum.renum_wue_dr_l()
    bewegrenum.tisch_kor()
    bewegrenum.fl_unten_dr_l(1) # dreht Unterseite nach links
    bewegrenum.renum_unten_l()
    bewegrenum.dreh_seite_ll() # dreht linke Seite nach links
    farbscan.tischdreh.on_for_degrees(30, -95) # dreht Tisch
    bewegrenum.renum_wue_dr_l()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv) 
    farbscan.flaech_dreh_l()    # dreht Vorderseite nach links
    bewegrenum.renum_flae_dr_l()
   
def beweg_gelbeck_ul(): # bringt gelbe Ecken in mit gelb nach unten
    bewegrenum.dreh_seite_lr()  # dreht linke Seite nach rechts
    farbscan.tischdreh.on_for_degrees(30, -92) # dreht Tisch
    bewegrenum.renum_wue_dr_l()
    bewegrenum.tisch_kor()
    bewegrenum.fl_unten_dr_r(1) # dreht Unterseite nach rechts
    bewegrenum.renum_unten_r()
    bewegrenum.dreh_seite_ll() # dreht linke Seite nach links
    farbscan.tischdreh.on_for_degrees(30, -92) # dreht Tisch
    bewegrenum.renum_wue_dr_l()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv) 
    bewegrenum.fl_unten_dr_r(1)  # dreht Unterseite nach rechts
    bewegrenum.renum_unten_r()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv) 
    bewegrenum.dreh_seite_lr()  # dreht linke Seite nach rechts
    farbscan.tischdreh.on_for_degrees(30, -92) # dreht Tisch
    bewegrenum.renum_wue_dr_l()
    bewegrenum.tisch_kor()
    bewegrenum.fl_unten_dr_r(1) # dreht Unterseite nach rechts
    bewegrenum.renum_unten_r()
    bewegrenum.fl_unten_dr_r(1) # dreht Unterseite nach rechts
    bewegrenum.renum_unten_r()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv) 
    bewegrenum.dreh_seite_ll() # dreht linke Seite nach links
    farbscan.tischdreh.on_for_degrees(30, -92) # dreht Tisch
    bewegrenum.renum_wue_dr_l()
    #farbscan.gabelvors.on_for_degrees(30, 78)
    #bewegrenum.tisch_kor()
    #sleep(.1)
    #farbscan.gabelvors.on_to_position(30, pos_gv)

def beweg_gelbeck_ur(): # bringt gelbe Ecken in mit gelb nach unten
    bewegrenum.dreh_seite_rl()  # dreht rechte Seite nach links
    farbscan.tischdreh.on_for_degrees(30, 92) # dreht Tisch
    bewegrenum.renum_wue_dr_r()
    bewegrenum.tisch_kor()
    bewegrenum.fl_unten_dr_l(1) # dreht Unterseite nach links
    bewegrenum.renum_unten_l()
    bewegrenum.dreh_seite_rr() # dreht rechte Seite nach rechts
    farbscan.tischdreh.on_for_degrees(30, 92) # dreht Tisch
    bewegrenum.renum_wue_dr_r()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv) 
    bewegrenum.fl_unten_dr_l(1)  # dreht Unterseite nach links
    bewegrenum.renum_unten_l()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv) 
    bewegrenum.dreh_seite_rl()  # dreht rechte Seite nach links
    farbscan.tischdreh.on_for_degrees(30, 92) # dreht Tisch
    bewegrenum.renum_wue_dr_r()
    bewegrenum.tisch_kor()
    bewegrenum.fl_unten_dr_l(1) # dreht Unterseite nach links
    bewegrenum.renum_unten_l()
    bewegrenum.fl_unten_dr_l(1) # dreht Unterseite nach links
    bewegrenum.renum_unten_l()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv) 
    bewegrenum.dreh_seite_rr() # dreht rechte Seite nach rechts
    farbscan.tischdreh.on_for_degrees(30, 92) # dreht Tisch
    bewegrenum.renum_wue_dr_r()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv) 

def bew_gelbe_eck(): # bringt gelbe Ecken in die richtige Position
    bewegrenum.dreh_seite_rr()  # dreht rechte Seite nach rechts
    farbscan.tischdreh.on_for_degrees(30, 95) # dreht Tisch
    bewegrenum.renum_wue_dr_r()
    bewegrenum.tisch_kor()
    farbscan.flaech_dreh_l()    # dreht Vorderseite nach links
    bewegrenum.renum_flae_dr_l()
    bewegrenum.dreh_seite_rr() # dreht rechte Seite nach rechts, 
    #rechte Seite ist jetzt vorne
    farbscan.tischdreh.on_for_degrees(30, -92) # dreht Tisch - hintere Seite ist vorn
    bewegrenum.renum_wue_dr_l()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv)
    #print ("Pause dr li Tast!")
    #taste.wait_for_bump('left')
    farbscan.flaech_dreh_l()    # dreht ex-Hinterseite nach links
    bewegrenum.renum_flae_dr_l()
    sleep(.1)
    farbscan.flaech_dreh_l()    # dreht ex-Hinterseite nach links
    bewegrenum.renum_flae_dr_l()
    farbscan.tischdreh.on_for_degrees(30, 93) # dreht Tisch zurück
    bewegrenum.renum_wue_dr_r()
    farbscan.tischdreh.on_for_degrees(30, 93) # dreht Tisch zurück
    bewegrenum.renum_wue_dr_r()
    bewegrenum.tisch_kor()
    bewegrenum.dreh_seite_rl() # dreht rechte Seite nach links
    farbscan.tischdreh.on_for_degrees(30, 92) # dreht Tisch
    bewegrenum.renum_wue_dr_r()
    farbscan.flaech_dreh_r()    # dreht Vorderseite nach rechts
    bewegrenum.renum_flae_dr_r()
    bewegrenum.dreh_seite_rr() # dreht rechte Seite nach rechts
    farbscan.tischdreh.on_for_degrees(30, -92) # dreht Tisch
    bewegrenum.renum_wue_dr_l()
    bewegrenum.tisch_kor()
    #print ("Pause2 dr li Tast!")
    #taste.wait_for_bump('left')
    farbscan.flaech_dreh_l()    # dreht ex-Hinterseite nach links
    bewegrenum.renum_flae_dr_l()
    sleep(.1)
    farbscan.flaech_dreh_l()    # dreht ex-Hinterseite nach links
    bewegrenum.renum_flae_dr_l()
    farbscan.tischdreh.on_for_degrees(30, 93) # dreht Tisch zurück
    bewegrenum.renum_wue_dr_r()
    farbscan.tischdreh.on_for_degrees(30, 93) # dreht Tisch zurück
    bewegrenum.renum_wue_dr_r()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv)
    #print ("Pause3 dr li Tast!")
    #taste.wait_for_bump('left')
    bewegrenum.dreh_seite_rl()  # dreht rechte Seite nach links
    sleep(.1)
    farbscan.flaech_dreh_l()    # dreht rechte Seite nochmals nach links
    bewegrenum.renum_flae_dr_l()
    farbscan.tischdreh.on_for_degrees(30, 95) # dreht Tisch zurück
    bewegrenum.renum_wue_dr_r()
    bewegrenum.tisch_kor()    

def beweg_kanten():
    bewegrenum.dreh_seite_ll()  # dreht linke Seite nach links
    farbscan.tischdreh.on_for_degrees(30, -98) # dreht Tisch zurück
    bewegrenum.renum_wue_dr_l()
    sleep(0.1)
    bewegrenum.fl_unten_dr_r(1) # dreht Unterseite nach rechts
    bewegrenum.renum_unten_r()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv)
    sleep(0.1)
    bewegrenum.dreh_seite_ll() # dreht linke Seite nach links
    farbscan.tischdreh.on_for_degrees(30, -93) # dreht Tisch
    bewegrenum.renum_wue_dr_l()
    sleep(0.1)
    bewegrenum.fl_unten_dr_l(1) # dreht Unterseite nach links
    bewegrenum.renum_unten_l()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv)
    bewegrenum.dreh_seite_ll()  # dreht linke Seite nach links
    farbscan.tischdreh.on_for_degrees(30, -93) # dreht Tisch zurück
    bewegrenum.renum_wue_dr_l()
    sleep(0.1)
    bewegrenum.fl_unten_dr_l(1) # dreht Unterseite nach links
    bewegrenum.renum_unten_l()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv)
    bewegrenum.dreh_seite_ll() # dreht linke Seite nach links
    farbscan.tischdreh.on_for_degrees(30, -95) # dreht Tisch
    bewegrenum.renum_wue_dr_l()
    sleep(0.1)
    bewegrenum.fl_unten_dr_r(1) # dreht Unterseite nach rechts
    bewegrenum.renum_unten_r()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv) 

def beweg_kant1():
    bewegrenum.dreh_seite_lr()  # dreht linke Seite nach links
    farbscan.tischdreh.on_for_degrees(30, -93) # dreht Tisch zurück
    bewegrenum.renum_wue_dr_l()
    sleep(0.1)
    bewegrenum.fl_unten_dr_r(1) # dreht Unterseite nach rechts
    bewegrenum.renum_unten_r()
    farbscan.gabelvors.on_for_degrees(30, 78)
    bewegrenum.tisch_kor()
    sleep(.1)
    farbscan.gabelvors.on_to_position(30, pos_gv)
    bewegrenum.dreh_seite_ll() # dreht linke Seite nach links
    farbscan.tischdreh.on_for_degrees(30, -93) # dreht Tisch
    bewegrenum.renum_wue_dr_l()
    sleep(0.1)  
    bewegrenum.dreh_seite_ll() # dreht linke Seite nach links
    farbscan.tischdreh.on_for_degrees(30, -95) # dreht Tisch
    bewegrenum.renum_wue_dr_l() 
    bewegrenum.tisch_kor()   
     
def gelb_kreuz():
    if ((fl[2][1] != 4) and (fl[2][3] != 4) and (fl[2][5] != 4) and (fl[2][7] != 4)): # keine gelbe Kante
        beweg_gelb_kr()
        bewegrenum.fl_unten_dr_r(1)  # dreht Unterseite nach rechts
        bewegrenum.renum_unten_r()
        farbscan.gabelvors.on_for_degrees(30, 78)
        bewegrenum.tisch_kor()
        sleep(.1)
        farbscan.gabelvors.on_to_position(30, pos_gv) 
    elif (fl[2][1] == fl[2][5] == 4): # gelbe Reihe vertikal
        farbscan.tischdreh.on_for_degrees(30, 98) # dreht Tisch damit gelbe Reihe horizontal
        bewegrenum.renum_wue_dr_r()
        bewegrenum.tisch_kor()
        #beweg_gelb_kr()
    elif (fl[2][1] == fl[2][3] == 4) or (fl[2][1] == fl[2][7] == 4) or (fl[2][7] == fl[2][5] == 4):
        farbscan.tischdreh.on_for_degrees(30, 95) # dreht Tisch damit gelbes L richtig positioniert wird
        bewegrenum.renum_wue_dr_r()
        bewegrenum.tisch_kor()
    else: # gelbe Reihe horizontal oder gelbes L richtig positioniert
        beweg_gelb_kr()

def gelb_ecken():
    if ((fl[2][0] == 4) or (fl[2][2] == 4) or (fl[2][4] == 4) or (fl[2][6] == 4)):
        #farbscan.schreib_farb()
        #print ("fl 4,0 - 4,2 ",fl[4][0], fl[4][2],"dr li Tast!")
        #taste.wait_for_bump('left')
        for i in range (4):
            sleep(.1)
            if (fl[2][2] == fl[4][2] == 4) and fl[2][6] != 4:  # fisch gelb links
                beweg_gelbeck_ul()
            elif fl[2][0] == fl[4][0] == 4 and fl[2][6] != 4:  # fisch gelb rechts
                beweg_gelbeck_ur()
            elif fl[2][0] == fl[4][0] == 4 and fl[2][4] == 4:  # acht
                beweg_gelbeck_ul()
            elif fl[4][2] == fl[4][0] == 4: # laser nach vorn
                beweg_gelbeck_ul()
            elif fl[4][0] == fl[2][0] == fl[2][6] == 4: # laser seitlich
                beweg_gelbeck_ul()
            else: 
                farbscan.tischdreh.on_for_degrees(30, 93) # dreht Tisch damit gelbe Ecke richtig positioniert wird
                bewegrenum.renum_wue_dr_r()
                bewegrenum.tisch_kor()
    else:
        for i in range (4):
            sleep(.1)
            if fl[4][2] == fl[5][0] == fl[3][0] == fl[3][6] == 4: # kreuz mit vertikal gelb
                beweg_gelbeck_ul()
            elif fl[1][4] == fl[1][2] == fl[3][0] == fl[3][6] == 4: # kreuz mit parallel gelb
                beweg_gelbeck_ul()
            else: 
                farbscan.tischdreh.on_for_degrees(30, 93) # dreht Tisch damit gelbe Ecke richtig positioniert wird
                bewegrenum.renum_wue_dr_r()
                bewegrenum.tisch_kor()                                   
    
def ordne_gelbkanten():
    while not ((fl[1][3] == fl[1][8]) and (fl[4][1] == fl[4][8]) and (fl[3][7] == fl[3][8]) and (fl[5][1] == fl[5][8])):
        #farbscan.schreib_farb()
        #print ("bew kant fl 4,1 ",fl[4][1], fl[4][8],"dr li Tast!")
        #taste.wait_for_bump('left')
        sleep(.1)
        if (fl[4][1] == fl[4][8]) and not ((fl[3][7] == fl[3][8]) or (fl[1][3] == fl[1][8])):
            beweg_kanten()
            sleep(.1)
            beweg_kant1()
        elif (fl[4][1] == fl[4][8]) and ((fl[3][7] == fl[3][8]) or (fl[1][3] == fl[1][8])) or ((fl[4][1] != fl[4][8]) and (fl[3][7] != fl[3][8]) and (fl[1][3] != fl[1][8]) and (fl[5][1] != fl[5][8])):
            bewegrenum.fl_unten_dr_l(2) # dreht Unterseite nach links
            bewegrenum.renum_unten_l()            
        else:        
            farbscan.tischdreh.on_for_degrees(30, 95) # dreht Tisch damit gelbes Eck richtig positioniert wird
            bewegrenum.renum_wue_dr_r()
            sleep(.1)
        farbscan.gabelvors.on_for_degrees(30, 78)
        bewegrenum.tisch_kor()
        sleep(.1)
        farbscan.gabelvors.on_to_position(30, pos_gv)               

def ordne_gelbecken():
    if (fl[1][2] == fl[1][3] == fl[1][4]) and (fl[4][0] == fl[4][1] == fl[4][2]) and (fl[3][0] == fl[3][6] == fl[3][7]) and (fl[5][0] == fl[5][1] == fl[5][2]):
        pass
    else:
        for i in range (4):
            sleep(.1)
            if (fl[1][2] == fl[1][3] == fl[1][4]) and (fl[4][0] == fl[4][1] == fl[4][2]) and (fl[3][0] == fl[3][6] == fl[3][7]) and (fl[5][0] == fl[5][1] == fl[5][2]):
                break
            elif (fl[1][2] == fl[1][8]) or  ((fl[4][8] != fl[4][0]) and (fl[3][8] != fl[3][6]) and (fl[5][8]
            != fl[5][0]) and (fl[1][8] != fl[1][2])):
                #farbscan.schreib_farb()
                #print ("richtige fl 5,0 ",fl[5][0], fl[5][8],"dr li Tast!")
                #taste.wait_for_bump('left')
                bew_gelbe_eck()
            else:
                for j in range(4):  
                    if j == 0:   # dreht Unterseite nach links
                        bewegrenum.fl_unten_dr_l(1) 
                    else:
                        bewegrenum.fl_unten_dr_l(2)
                    bewegrenum.renum_unten_l()
            farbscan.tischdreh.on_for_degrees(30, 95) # dreht Tisch damit gelbes Eck richtig positioniert wird
            bewegrenum.renum_wue_dr_r()
        farbscan.gabelvors.on_for_degrees(30, 78)
        bewegrenum.tisch_kor()
        sleep(.1)
        farbscan.gabelvors.on_to_position(30, pos_gv)
            
                
       


       
            
        


        




