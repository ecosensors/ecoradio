'''
We assume you already created a aplication and a devise at TTN console
'''

import os
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
dev_id = "sds011-12"
# Add here the Device Address
devaddr = [0x26, 0x01, 0x26, 0x26]
# Add here the Network Session Key
nwkey = [0x09, 0x0F, 0xCE, 0x03, 0x26, 0x26, 0x26, 0x26, 0x26, 0x26, 0x26, 0x26, 0x26, 0x26, 0x26, 0x26]
# Add here the App Session Key
app = [0x09, 0x0F, 0xCE, 0x03, 0x26, 0x26, 0x26, 0x26, 0x26, 0x26, 0x26, 0x26, 0x26, 0x26, 0x26, 0x26]
