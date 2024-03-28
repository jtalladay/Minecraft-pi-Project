from mcpi.minecraft import Minecraft

#Import relevant libraries
from gpiozero import *
from time import sleep

#Set pin numbers
#ldr = LightSensor(4)
#led_1 = LED(22)
#led_2 = LED(4)
#rgb = RGBLED(red=14, green=17, blue=27)
button_1 = Button(18)
button_2 = Button(19)
button_3 = Button(20)
button_4 = Button(21)

# Creates connection to running Minecraft game
mc = Minecraft.create()

# Saves starting poistion in world as respawn point
home_x, home_y, home_z = mc.player.getPos()

#variables
lava = 10
water = 8
air = 0
tnt = 46

# Some functions to use when pressing buttons
def respawn_teleport():
    print("teleporting back to respawn point")
    mc.postToChat("Respawn Button pressed")                                         
    mc.player.setPos(home_x, home_y, home_z)

def tnt_blocks():
    mc.postToChat("TNT Button Pressed")
    x, y, z = mc.player.getPos()
    mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, tnt, 1)

def create_lava():
    mc.postToChat("Lava Button Pressed") 
    x, y, z = mc.player.getPos()
    mc.setBlock(x+3, y+3, z, lava)
    sleep(10)
    mc.setBlock(x+3, y+5, z, water)
    sleep(4)
    mc.setBlock(x+3, y+5, z, air)
    
# can turn this function on if the light value is higher 
def drop_flowers():
        grass = 2
        flower = 38

        while True:
            x, y, z = mc.player.getPos()  # player position (x, y, z)
            block_beneath = mc.getBlock(x, y-1, z)  # block ID

            if block_beneath == grass:
                mc.setBlock(x, y, z, flower)
            sleep(0.1)
            
def giant_stone_cube():
    mc.postToChat("Stone Button Pressed") 
    x, y, z = mc.player.getPos()
    mc.setBlocks(x+1, y+1, z+1, x+6, y+6, z+6, 1)
    
while True:
   
    #print(ldr.value)

  # calls a function when a button is pressed
    if button_1.is_pressed:
        print("button 1")
        respawn_teleport()
        button_1.wait_for_release()
    if button_2.is_pressed:
        print("button 2")
        tnt_blocks()
        button_2.wait_for_release()
    if button_3.is_pressed:
        print("button 3")
        giant_stone_cube()
        button_3.wait_for_release()
    if button_4.is_pressed:
        print("button 4")
        create_lava()
        button_4.wait_for_release()

