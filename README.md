paru -Sy --noconfirm --needed bluez bluez-utils
# Bluestrike

- Opensource python tool for jamming bluetooth signals (in the making)
- Successful in jamming bluetooth speakers
- Does not work on Airpods or any other bluetooth devices yet ...


## Tool Preview

![Imgur](https://i.imgur.com/qQloXdx.png)


## ⚠️ Note

- **This is an educational research project; I do not endorse or support the utilization of this tool for any illegal purposes.**

## Installation

1. Clone the repo and install basic requirements
```
git clone https://github.com/StealthIQ/Bluestrike.git
cd Bluestrike
pip3 install -r requirements.txt
```
2. Install necessary packages
```
paru -Sy --noconfirm --needed bluez bluez-utils
```

## Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file:

```plaintext
.env 
```
keep the .env file under `/utils`.

## Table of Contents
1. Working of Bluetooth
2. Security Risks
3. Security Tips for Using Bluetooth
4. Applications Used
5. Malicious Attack
6. Attack Detection
7. Prevention Method
8. How AirPods Block Requests from Devices

### Working of Bluetooth

- Bluetooth uses radio waves to transmit data in the 2.4 to 2.4835 GHz. frequency band.
	- Which is also used by other devices such as *Wi-Fi and microwave ovens*. 

- Bluetooth devices use a technique called **Frequency hopping to avoid interference from other devices**. This means that the radio waves used by Bluetooth are ***constantly changing frequencies***, which makes it more difficult for other devices to intercept the data being transmitted.

- Bluetooth devices are typically paired with each other before they can communicate. This is done by ***entering a passcode*** on each device. Once the devices are paired, they can communicate with each other ***without the need for a passcode***.

- Bluetooth devices can communicate with each other up to a **range of 10 meters.**
---
### Security Risks

From a security perspective, Bluetooth is a relatively secure technology. However, there are some security risks associated with Bluetooth, such as:

- **Man-in-the-middle attacks:** This is a type of attack where an attacker intercepts the data being transmitted between two Bluetooth devices. This can be done by using a device that is broadcasting a fake Bluetooth signal.
- **Bluejacking:** This is a type of attack where an attacker sends unsolicited messages to a Bluetooth device. These messages can be used to spam the user or to install malware on the device.
- **Bluesnarfing:** This is a type of attack where an attacker steals data from a Bluetooth device. This can be done by connecting to the device and accessing the files that are stored on it.
---
#### Security tips for using Bluetooth:

- **Turn off Bluetooth when you are not using it.** This will help to prevent unauthorized devices from connecting to your device.
- **Use a Bluetooth security solution.** There are a number of Bluetooth security solutions available that can help to protect your device from unauthorized access.
- **Be aware of the risks associated with using Bluetooth.** Bluetooth is a convenient technology, but it is important to be aware of the security risks associated with it.

---
#### Applications Used 
- Bluetooth is used for a variety of applications, including:
    - Wireless headphones
    - Wireless speakers
    - Wireless keyboards
    - Wireless mice
    - Car kits
    - Printers
    - File transfer
    - Gaming
    - Internet of Things (IoT)

### Malicious Attack 
AirPods **can block requests from a device** if it is **sending multiple requests**. This is to prevent a Denial-of-Service (DoS) attack, which is an **attempt to make a service unavailable by sending it too many requests.**

### Attack Detection
When AirPods detect that a device is sending repeated requests, they will first try to ignore the requests. If the requests continue, AirPods will eventually block the device from connecting.

### Prevention Method
- This is a security feature that is designed to protect AirPods users from malicious attacks.

1. **How AirPods block requests from devices that are sending repeated requests**?

- **Rate limiting:** AirPods use rate limiting to prevent devices from sending too many requests in a given amount of time. This is done by keeping track of the number of requests that a device has sent in a certain period of time, and then blocking any further requests if the device exceeds a certain threshold. This helps to prevent devices from overloading the AirPods with too many requests, which can cause performance issues.
- **Packet filtering:** AirPods also use packet filtering to block requests from devices that are sending repeated requests. This is done by inspecting network traffic and looking for packets that are from the same device and that contain the same data. If a packet is found to match this criteria, it is blocked from being processed by the AirPods. This helps to prevent devices from flooding the AirPods with repeated requests, which can also cause performance issues.

These two techniques work together to help ensure that AirPods can handle a large number of requests without experiencing performance issues.

#### Bypass rate limiting and packet filtering in Bluetooth security:

1. Fragmentation attacks: The attacker can split up packets into smaller fragments that fall below the rate limit threshold. Each fragment on its own is allowed, but when reassembled they exceed the limit.
    
2. Spoofing source addresses: The attacker can spoof the source address of packets to make it appear they are coming from a different device. This can bypass address-based filters.
    
3. Flooding attacks: The attacker can generate a very large number of packets in a short period of time, overwhelming the rate limiting mechanism and forcing it to allow some packets through.
    
4. Protocol tunneling: The attacker can tunnel non-Bluetooth protocols over the Bluetooth connection. Since the packet filters only inspect Bluetooth packets, the tunneled traffic can bypass the filters.
    
5. Exploiting vulnerabilities: If there are vulnerabilities in the Bluetooth software stack, the attacker may be able to exploit them to disable or circumvent the rate limiting and packet filtering mechanisms.

1, Generate a MAC address with a specific OUI using the built-in `random` module in Python. 

2. List of Standard OUI
https://standards-oui.ieee.org/

3. IEEE is the Institute of Electrical and Electronics Engineers. They are a professional association that promotes technological innovation and excellence.

- **Some key things about IEEE related to MAC addresses:**

1. IEEE manages the registration and assignment of MAC address Organizationally Unique Identifiers (OUIs).
    
2. Companies and organizations register with IEEE and are assigned a unique 3-byte OUI prefix to use when generating their MAC addresses.
    
3. The IEEE maintains a database of all registered OUIs, which currently contains over 22,000 entries.
    
4. For MAC addresses to be considered valid, they must have an OUI that is registered in the IEEE database. Unregistered OUIs will not work in practice.
    
5. The mac_address library that we used in the code example has a copy of the IEEE OUI database. This allows it to generate realistic MAC addresses using registered OUIs.
    
So in summary, IEEE assigns and manages the OUIs that form the first 3 bytes of MAC addresses. This ensures globally unique MAC addresses and proper functioning of networking protocols.

- Specified OUI ("00:50:C2"):

```python
import random

TARGET_OUI = "00:50:C2"

def generate_mac_address(oui):
    # Generate the last 3 bytes of the MAC address
    last_bytes = [random.randint(0x00, 0xff) for _ in range(3)]
    # Concatenate the OUI and the last 3 bytes to form the MAC address
    mac_address = oui + ":" + ":".join('{:02x}'.format(byte) for byte in last_bytes)
    return mac_address

# Generate a MAC address with the specified OUI
mac_with_oui = generate_mac_address(TARGET_OUI)
print(mac_with_oui)
```

### FAQ

#### Your Question?
- Answer


### Feedback

If you have any feedback or suggestions, please reach out to me via email at stealthiq[at]protonmail[.]com or [Twitter](https://twitter.com/StealthIQQ).

### Author

- [@Stealthiq](https://www.github.com/stealthiq)

### License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

