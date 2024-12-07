#!/usr/bin/env python3

from __future__ import absolute_import
from ev3dev.ev3 import *
from roberta.ev3 import Hal
from ev3dev2.motor import LargeMotor, MediumMotor
from ev3dev2.motor import MoveSteering, OUTPUT_A, OUTPUT_D
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_D
from ev3dev2.sound import Sound
from ev3dev import ev3 as ev3dev

#lm = LargeMotor(OUTPUT_A)
#rm = LargeMotor(OUTPUT_D)
mm = MediumMotor(OUTPUT_B)

sound = Sound()
opts = '-a 200 -s 130 -v'

text = 'Saluton amikoj, mi estas Robi! mi sxatas muziki kaj danci'
sound.speak(text, espeak_opts=opts+'eo')

class BreakOutOfALoop(Exception): pass
class ContinueLoop(Exception): pass

_brickConfiguration = {
    'wheel-diameter': 5.6,
    'track-width': 18.0,
    'actors': {
        'A':Hal.makeLargeMotor(ev3dev.OUTPUT_A, 'on', 'foreward', 'right'),
        'D':Hal.makeLargeMotor(ev3dev.OUTPUT_D, 'on', 'foreward', 'left'),
    }
}
hal = Hal(_brickConfiguration)

def s3():
    mm.on(20)
    hal.rotateDirectionRegulated('D', 'A', False, 'right', 30)
    hal.playTone(float(220), float(250))
    hal.stopMotors('D', 'A')
    mm.off()
    mm.on(-20)
    hal.regulatedDrive('D', 'A', False, 'foreward', 30)
    hal.playTone(float(246.942), float(250))
    hal.stopMotors('D', 'A')
    mm.off()
    mm.on(20)
    hal.rotateDirectionRegulated('D', 'A', False, 'left', 30)
    hal.playTone(float(261.626), float(250))
    hal.stopMotors('D', 'A')
    mm.off()
    mm.on(-20)
    hal.regulatedDrive('D', 'A', False, 'backward', 30)
    hal.playTone(float(174.614), float(250))
    hal.stopMotors('D', 'A')
    mm.off()

def s1():
    mm.on(20)
    hal.regulatedDrive('D', 'A', False, 'foreward', 30)
    hal.playTone(float(174.614), float(250))
    hal.stopMotors('D', 'A')
    mm.off()
    mm.on(-20)
    hal.rotateDirectionRegulated('D', 'A', False, 'left', 30)
    hal.playTone(float(174.614), float(250))
    hal.stopMotors('D', 'A')
    mm.off()
    mm.on(10)
    hal.regulatedDrive('D', 'A', False, 'backward', 30)
    hal.playTone(float(174.614), float(500))
    hal.stopMotors('D', 'A')
    mm.off()

def s2():
    mm.on(-20)
    hal.rotateDirectionRegulated('D', 'A', False, 'right', 30)
    hal.playTone(float(195.998), float(250))
    hal.stopMotors('D', 'A')
    mm.off()
    mm.on(20)
    hal.regulatedDrive('D', 'A', False, 'foreward', 30)
    hal.playTone(float(195.998), float(250))
    hal.stopMotors('D', 'A')
    mm.off()
    mm.on(-10)
    hal.rotateDirectionRegulated('D', 'A', False, 'left', 30)
    hal.playTone(float(195.998), float(500))
    hal.stopMotors('D', 'A')
    mm.off()

def s4():
    hal.rotateDirectionRegulated('D', 'A', False, 'right', 30)
    mm.on(-20)
    hal.playTone(float(164.814), float(250))
    hal.stopMotors('D', 'A')
    mm.off()
    mm.on(20)
    hal.regulatedDrive('D', 'A', False, 'foreward', 30)
    hal.playTone(float(174.614), float(250))
    hal.stopMotors('D', 'A')
    mm.off()
    mm.on(-10)
    hal.rotateDirectionRegulated('D', 'A', False, 'left', 30)
    hal.playTone(float(195.998), float(250))
    hal.stopMotors('D', 'A')
    mm.off()
    mm.on(10)
    hal.regulatedDrive('D', 'A', False, 'backward', 30)
    hal.playTone(float(130.813), float(250))
    hal.stopMotors('D', 'A')
    mm.off()

def s8():
    mm.on(10)
    hal.rotateDirectionRegulated('D', 'A', False, 'right', 30)
    hal.playTone(float(195.998), float(250))
    hal.stopMotors('D', 'A')
    mm.off()
    mm.on(-15)
    hal.regulatedDrive('D', 'A', False, 'foreward', 30)
    hal.playTone(float(164.814), float(250))
    hal.stopMotors('D', 'A')
    mm.off()
    mm.on(10)
    hal.rotateDirectionRegulated('D', 'A', False, 'left', 30)
    hal.playTone(float(174.614), float(500))
    hal.stopMotors('D', 'A')
    mm.off()

def run():
    s1()
    s2()
    s3()
    s4()
    s1()
    s2()
    s3()
    s8()

def main():
    try:
        run()
    except Exception as e:
        hal.drawText('Fehler im EV3', 0, 0)
        hal.drawText(e.__class__.__name__, 0, 1)
        hal.drawText(str(e), 0, 2)
        hal.drawText('Press any key', 0, 4)
        while not hal.isKeyPressed('any'): hal.waitFor(500)
        raise

if __name__ == "__main__":
    main()