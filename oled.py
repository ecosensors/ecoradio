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
from PIL import Image, ImageDraw, ImageFont
# 128x64 OLED Display
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear the display.
display.fill(0)
display.show()
# Get the LCD size
WIDTH = display.width
HEIGHT = display.height
BORDER = 5

def oled():
    '''
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
    time.sleep(3)
    '''

    display.fill(0)
    display.show()

    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    image = Image.new("1", (WIDTH, HEIGHT))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a white background
    draw.rectangle((0, 0, WIDTH, HEIGHT), outline=255, fill=255)

    # Draw a smaller inner rectangle
    draw.rectangle(
         (BORDER, BORDER, WIDTH - BORDER - 1, HEIGHT - BORDER - 1),
         outline=0,
         fill=0,
    )

    # Load default font.
    font = ImageFont.load_default()

    # Draw Some Text
    text = "EcoSensors.ch"
    (font_width, font_height) = font.getsize(text)
    draw.text(
        (WIDTH // 2 - font_width // 2, HEIGHT // 2 - font_height // 2),
        text,
        font=font,
        fill=255,
    )

    # Display image
    display.image(image)
    display.show()


oled()
