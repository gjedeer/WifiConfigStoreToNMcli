# WifiConfigStoreToNMcli
This program turns your WiFiConfigStore.xml file extracted from an Android phone into a batch file configuring NetworkManager to add found networks.

## Writeup
This is based on WifiConfigStoreToQR. To see more detail into how this program was developed and how to extract the WiFiConfigStore.xml file, check out [Antonio's blog post](https://blog.antoniosolismz.com/?p=97)

## Usage
Run `python3 ConvertToQR.py /path/to/WiFiConfigStore.xml`

Example of the script output:

```
#!/bin/sh
# Wi-Fi configuration file created from WifiConfigStore.xml by ConvertToNMCli.py at 2023-05-12T18:31:38.147201

DEVICE=wlan0

nmcli c add type wifi con-name HOTSPOT ssid HOTSPOT ifname $DEVICE
nmcli c add type wifi con-name openwireless.org ssid open ifname $DEVICE
nmcli c add type wifi con-name LibreELEC-AP ssid LibreELEC-AP ifname $DEVICE
nmcli c modify LibreELEC-AP wifi-sec.key-mgmt wpa-psk wifi-sec.psk aabbccddeeff

```
