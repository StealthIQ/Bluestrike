import random
import string
import time
import re
import os

# OUI Map of Top companies
OUI_MAP = {
        "Apple": "00:1F:7F",
        "Dell": "00:14:5F",
        "HP": "00:4C:6F",
        "Lenovo": "00:50:C2",
        "Microsoft": "00:0C:29",
        "Samsung": "00:1C:42",
        "Sony": "00:0A:95",
        "Acer": "00:26:A9",
        "Asus": "00:19:D8",
        "Google": "08:00:27",
        "HTC": "00:1F:B5",
        "Intel": "00:19:5D",
        "LG": "00:1C:61",
        "Motorola": "00:1F:42",
        "Toshiba": "00:1E:67",
        "Xiaomi": "00:26:A8",
    }

def generate_mac_address(brand):
    # Generate the last 3 bytes of the MAC address
    last_bytes = [random.randint(0x00, 0xff) for _ in range(3)]
    # Concatenate the OUI and the last 3 bytes to form the MAC address
    mac_address = get_oui(brand) + ":" + ":".join('{:02x}'.format(byte) for byte in last_bytes)
    return mac_address

# Gets the OUI for the specified brand.
def get_oui(brand):
    return OUI_MAP.get(brand, None)

if __name__ == "__main__":
    try:
        os.system("clear||cls")
        srNO = 0
        print("-- Avalible Devices --")
        for key in OUI_MAP:
            srNO+=1
            print(" ", srNO,"-", key)
        brand = input("\nEnter the brand name of your device: ")

        # Verifying the mac adress according to the standard
        mac = generate_mac_address(brand)
        while  not re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower()):
            print("Generated Invalid Mac Adress :", mac)
            mac = generate_mac_address(brand)
        print(mac)
    except KeyboardInterrupt:
        time.sleep(0.1)
        print('\nAborted!!!')
        exit()
