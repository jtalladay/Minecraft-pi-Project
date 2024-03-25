from mcpi.minecraft import Minecraft

#Import relevant libraries
from gpiozero import *
from time import sleep

#Set pin numbers
#ldr = LightSensor(4)
#led_1 = LED(22)
#led_2 = LED(4)
#rgb = RGBLED(red=14, green=17, blue=27)
button_1 = Button(24)
button_2 = Button(2)

# Creates connection to running Minecraft game
mc = Minecraft.create()

# Saves starting poistion in world as respawn point
home_x, home_y, home_z = mc.player.getPos()

# Some functions to use when pressing buttons
def respawn_teleport():
        print("teleporting back to respawn point")
        mc.postToChat("Respawn Button pressed")                                         
        mc.player.setPos(home_x,home_y,home_z)

def tnt_blocks():
        tnt = 46
        mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, tnt, 1)

#def create_lava():
    
def giant_stone_cube():
    x, y, z = mc.player.getPos()
    mc.setBlocks(x+1, y+1, z+1, x+6, y+6, z+6, 1)
    
while True:
     #print(ldr.value)

  # calls a function when a button is pressed
    button_1.wait_for_press()
    respawn_teleport()
    sleep(1)
    
    button_2.wait_for_press()
    giant_stone_cube()
    sleep(1)

