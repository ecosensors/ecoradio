# EcoRadio
LoRaWAN HAT for Raspberry and EcoBoard with LCD,  I2C and UART connectors.

EcoRadio is a very usefull LoRaWAN HAT for EcoBoard and compatible with Raspberry boards.
The board has an U.FL connector for the Antenna and a I2C and UART connector to connect sensors.
You can easly connect a LCD OLED 128x64 to display messages

The board will be available current June 2020 and in the meantime, some C++ and Python script will be uploaded to let you easly start with the board

## LCD OLED
If you are using the 128x64 OLED LCD, you have to activate the I2C bus

```
sudo raspi-config
```
Then choose and activate it

* 5 Interface Options
* P5 i2C

### Installation of the libary
Update your Bustar OS, install pip3 and the needed packages

```
sudo apt update && sudo apt upgrade
sudo apt install python3-pip
sudo pip3 install adafruit-circuitpython-ssd1306
sudo apt install python3-pil
```
### Examples
[Here](https://github.com/ecosensors/ecoradio/tree/master/oled) are come example to start

## LED
The EcoRadio board conatins 3 LED. Beside of the LEDs, there are 3 jumbers to be soldered to use the LEDs. Note LED 18 (GPIO18) only works if you use the EcoRadio board with a Raspberry.
The two other LEDs work with a Raspberry or the [EcoBoard](https://github.com/ecosensors/ecoboard) board.

## How to use the LEDs with Raspberry
Colse jumper SJ18 to activate D18
Colse jumper SJ19 to activate D19
Close jumper SJ10 to activate D20.

D18 is connected to GPIO18
D19 is connected to GPIO19
D20 is connected to GPIO20

You can also connect LED without resistance, to the connector J3 if you need an external LED. R20 is a 330Ω connected to the Anode of D20. 

You need to import DigitalInput

```
from digitalio import DigitalInOut, Direction, Pull
```

then add the following lines

```
d18Output = DigitalInOut(board.D18)
d18Output.direction = Direction.OUTPUT
d18Output.value = False

d19Output = DigitalInOut(board.D19)
d19Output.direction = Direction.OUTPUT
d19Output.value = False

d20Output = DigitalInOut(board.D20)
d20Output.direction = Direction.OUTPUT
d20Output.value = False
```

To turn on a LED

```
d18Output.value = 1
```

To turn off a LEDD

```
d18Output.value = 0
```


## RFM95 radio (LoRaWAN)
### Installation of the tiny-lora python library

```
sudo pip3 install adafruit-circuitpython-tinylora
```
### Examples
[Here is](https://github.com/ecosensors/ecoradio/tree/master/lorawan) a python script example, but do not miss to prepare a device at TTN

### Preparation of your device at TTN
We assume, you have created an account at [The Things Network (TTN)](https://www.thethingsnetwork.org)

Let's go to [your console](https://console.thethingsnetwork.org/) and let's create an application

![Add application](assets/ttn-application.png "Add TTN application")

Now, you will need to create a device. Return to your application view

![Application view](assets/ttn-application-view.png "Application view")

click on the application you just created, select the "Device" tab

![Add a device](assets/ttn-new-devise.png "Add a device")

At the field **Device EUI**, make sure you can read *this field will be generated* or give an unique identifier.

Finaly, click **register**.

Now, edit your new device and go to the **settings** tab

![Settings](assets/ttn-device-setting-tab.png "Settings")

and modify the following settings

![Settings](assets/ttn-device-settings.png "Settings")

* Activation Method => ABP
* Frame Counter Width => 16 bit
* Frame Counter Check => uncheck it

and save it.

You will later need the keys of the **Device Address**, the **Network Session Key** and the **App Session Key** 


Have a fun and do not miss the python example script.
