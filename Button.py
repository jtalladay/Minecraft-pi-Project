from gpiozero import *
from mcpi.minecraft import Minecraft
import subprocess
from time import sleep

mc = Minecraft.create()
BUTTON_PIN1 = Button(16)
BUTTON_PIN2 = Button(20)
BUTTON_PIN3 = Button(21)
x, y, z = mc.player.getPos()

while True :
    x, y, z = mc.player.getPos()
    
    BUTTON_PIN1.wait_for_press()
    mc.setBlock(x+1, y, z, 46, 1)
    
    BUTTON_PIN2.wait_for_press()
    mc.player.setPos(x, y ,z+10) 
    
    
GPIO.cleanup()