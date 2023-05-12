# WifiConfigStoreToNMcli
This program turns your WiFiConfigStore.xml file extracted from an Android phone into a batch file configuring NetworkManager to add found networks.

## Writeup
This is based on WifiConfigStoreToQR. To see more detail into how this program was developed and how to extract the WiFiConfigStore.xml file, check out [Antonio's blog post](https://blog.antoniosolismz.com/?p=97)

## Usage
Run `python3 ConvertToQR.py /path/to/WiFiConfigStore.xml`

Example of the script output:

```
#!/bin/sh
# Wi-Fi configuration file created from WifiConfigStore.xml by ConvertToNMCli.py at 2023-05-12T11:21:54.552360

nmcli d wifi connect HOTSPOT
nmcli d wifi connect openwireless.org
nmcli d wifi connect LibreELEC-AP password aabbccddeeff
```
