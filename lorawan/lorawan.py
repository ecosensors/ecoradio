#get!/usr/bin/env python

'''
Here is an exemple to use LoRaWAN library with EcoRadio board. This example works fine with another radio board as long as you 
double check the pin TinyLoRa Configuration. You may have to adapt it following of you connection
'''

'''
Do not forget to edit the ttnkeys.py file and change the keys according to the devise you recorded at TTN
'''

from adafruit_tinylora.adafruit_tinylora import TTN, TinyLoRa
# TinyLoRa Configuration
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = DigitalInOut(board.CE1)
irq = DigitalInOut(board.D5)
rst = DigitalInOut(board.D25)

# TTN Device Address, 4 Bytes, MSB
# Check to ttnskeays.py file
devaddr = bytearray(ttnkeys.devaddr)
# TTN Network Key, 16 Bytes, MSB
nwkey = bytearray(ttnkeys.nwkey)
# TTN Application Key, 16 Bytess, MSB
app = bytearray(ttnkeys.app)


# Initialize ThingsNetwork configuration
ttn_config = TTN(devaddr, nwkey, app, country='EU')
lora = TinyLoRa(spi, cs, irq, rst, ttn_config)
# 2b array to store sensor data
data_pkt = bytearray(2)
# time to delay periodic packet sends (in seconds)
data_pkt_delay = 5.0



# Sending with LoRa
def send_data(data):
    print('[INFO] Sending data with LoRa')
    data_pkt = bytearray(data, 'utf-8')
    try:
         lora.send_data(data_pkt, len(data_pkt),lora.frame_counter)
         lora.frame_counter += 1
    except:
         print("[ERROR] Something went wrong")

    print('[INFO] Data have been send')
    time.sleep(0.5)


location = 'Watter jet of Geneva'
lat = 46.2070734
lon = 6.1563833

payload = 'a' + location + 'b' + str(int(lat * 10000)) + 'c' + str(int(lon * 10000))

print('[DEBUG] payload:' + payload)
send_data(payload)

print('Check now your TtN consol and try it again')
