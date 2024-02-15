#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pin_to_light_circuit = 7
pin_to_led1 = 11
pin_to_led2 = 13
pin_to_led3 = 15

# need three variables to store light value ranges
# need gpio pins for three leds
light_low = 2
light_medium = 5
light_high = 10
GPIO.setup(pin_to_led1, GPIO.OUT)
GPIO.setup(pin_to_led2, GPIO.OUT)
GPIO.setup(pin_to_led3, GPIO.OUT)
def light_measure():
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_light_circuit, GPIO.OUT)
    GPIO.output(pin_to_light_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_light_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_light_circuit) == GPIO.LOW):
        count += 1

    return 1000000*(1/count)

def turn_off_leds():
    GPIO.output(pin_to_led1, GPIO.LOW)
    GPIO.output(pin_to_led2, GPIO.LOW)	
    GPIO.output(pin_to_led3, GPIO.LOW)
    
#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    while True:
        # need to turn led on based on a range of light values
        if light_measure() < light_low:
            turn_off_leds()
            GPIO.output(pin_to_led1, GPIO.HIGH)
        if light_measure() < light_medium and light_measure() > light_low:
            turn_off_leds()
            GPIO.output(pin_to_led2, GPIO.HIGH)
        if light_measure() > light_medium:
            turn_off_leds()
            GPIO.output(pin_to_led3, GPIO.HIGH)

        print(light_measure())
      
        
except KeyboardInterrupt:
    pass
finally:
    turn_off_leds()
    GPIO.cleanup()
