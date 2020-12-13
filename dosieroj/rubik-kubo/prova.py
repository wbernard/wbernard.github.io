#!/usr/bin/env python3

import farbscan
import bewegrenum
import weisebene
import mittebene
import unterebene
#import farbscan_einfach
from time import sleep
import os

taste = farbscan.Button()
ton = farbscan.Sound()
fl = farbscan.fl
pos_ti = farbscan.pos_ti
pos_gd = farbscan.pos_gd
pos_gv = farbscan.pos_gv

farbscan.farb_kontrol()

print ("    ")
farbscan.schreib_farb()
print ("Farben dr li Tast!")
taste.wait_for_bump('left')

while not ((fl[0][1] == fl[0][3] == fl[0][5] == fl[0][7] == 6) and (fl[4][5] == fl[4][8]) and 
(fl[1][7] == fl[1][8]) and (fl[5][5] == fl[5][8]) and (fl[3][3] == fl[3][8])):
    weisebene.weiskreuz()

print ("    ")
farbscan.schreib_farb()
print ("nach weiskr dr li Tast!")
taste.wait_for_bump('left')

while not ((fl[0][0] == fl[0][2] == fl[0][4] == fl[0][6] == 6) and (fl[4][4] == fl[4][8]) and 
(fl[1][6] == fl[1][8]) and (fl[5][4] == fl[5][8]) and (fl[3][2] == fl[3][8])):
    weisebene.weisse_ecken()
'''farbscan.gabelvors.on_for_degrees(20, 75)
bewegrenum.tisch_kor()
sleep(.1)
farbscan.gabelvors.on_to_position(20, pos_gv)'''     

print ("    ")
farbscan.schreib_farb()
print ("nach weiseck dr li Tast!")
taste.wait_for_bump('left')

while not ((fl[4][3]==fl[4][7]==fl[4][8]) and (fl[1][1]==fl[1][5]==fl[1][8]) and (fl[5][3]==fl[5][7]==fl[5][8]) and (fl[3][1]==fl[3][5]==fl[3][8])):
    mittebene.mitt_eben_komp()

print ("    ")
farbscan.schreib_farb()
print ("nach mittebene dr li Tast!")
taste.wait_for_bump('left')

while not (fl[2][1] == fl[2][3] == fl[2][5] == fl[2][7] == 4):
    unterebene.gelb_kreuz()
    
#farbscan.schreib_farb()
#print ("nach gelbkr_unt dr li Tast!")
#taste.wait_for_bump('left')

while not (fl[2][0] == fl[2][2] == fl[2][4] == fl[2][6] == 4):
    unterebene.gelb_ecken()
    sleep(.1)
    
print ("    ")
farbscan.schreib_farb()
print ("gelb komplett_unt dr li Tast!")
taste.wait_for_bump('left')

while not ((fl[1][3] == fl[1][8]) and (fl[4][1] == fl[4][8]) and (fl[3][7] == fl[3][8]) and (fl[5][1] == fl[5][8])):
    unterebene.ordne_gelbkanten()
    
print ("    ")
farbscan.schreib_farb()
print ("gelbkant ok dr li Tast!")
taste.wait_for_bump('left')

while not ((fl[1][2] == fl[1][4] == fl[1][8]) and (fl[4][0] == fl[4][2] == fl[4][8]) and 
    (fl[3][0] == fl[3][6] == fl[3][8]) and (fl[5][0] == fl[5][2] == fl[5][8])):
    unterebene.ordne_gelbecken()

print ("    ")
farbscan.schreib_farb()
print ("alles komplett dr li Tast!")
taste.wait_for_bump('left')

ton.beep()