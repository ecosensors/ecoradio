#get!/usr/bin/env python

'''
Here are simple examples to easly start with OLED LCD and RFM95 module radio used for LoRaWAN
'''

'''
OLED libraries
'''
import time
import board, busio
# Create the I2C interface
i2c = busio.I2C(board.SCL, board.SDA)
# Import SSD1306
import adafruit_ssd1306
# 128x64 OLED Display
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear the display.
display.fill(0)
display.show()
# Get the LCD size
width = display.width
height = display.height

def oled():
    #display.poweron()
    # Clear screen
    display.fill(0)
    # print the buffer
    display.show()
    # Add some text in the buffer at the position x=0 y=0
    display.text('ECO-SENSORS.CH', 0, 0, 1)
    # Add new text in the buffer at the position x=0, y=8
    display.text('Smart Air Quality', 0, 8, 1)
    # Show the text from the buffer
    display.show()
    # On/Off l'écran
    #display.poweroff()


oled()
