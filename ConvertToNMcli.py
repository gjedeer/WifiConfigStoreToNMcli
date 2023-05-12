#!/usr/bin/python3

import datetime
import os
import pipes
import sys
import xml.etree.ElementTree as ET

def emitCommand(ssid, password, encryption, hidden=False, device=None, outfile=None):
    if encryption == "nopass":
        command_string = "nmcli d wifi connect %s" % (pipes.quote(ssid),)
    elif encryption == "WPA":
        command_string = "nmcli d wifi connect %s password %s" % (pipes.quote(ssid), pipes.quote(password))

    outfile.write('%s\n' % command_string)
    
def extractNetwork(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    networks = []
    
    for wificonfig in root.iter('WifiConfiguration'):
        # Clear the variables
        ssid = None
        password = None
        
        for string in wificonfig.findall('string'):
            #print(string.text)
            # Get SSID
            if string.attrib['name'] == 'SSID':
                ssid = string.text
                # Remove the quotes
                ssid = ssid[1:-1]
            # Get Password
            if string.attrib['name'] == 'PreSharedKey':
                password = string.text
                # Remove the quotes
                password = password[1:-1]
        
        #print(ssid)
        #print(password)
        #print("-----------------")
        
        # Check if it is an open network
        if password == None:
            # Open network
            # Add to dictionary
            # SSID, PASSWORD, ENCRYPTION
            networks.append([ssid, "", "nopass"])
        else:
            # Closed network
            # Add to dictionary
            # SSID, PASSWORD, ENCRYPTION
            networks.append([ssid, password, "WPA"])
        
    return networks

def main():
    # Parse XML file
    networks = extractNetwork(sys.argv[1])
    
    with open('nmcli-wifi.sh', 'w') as f:
        f.write('#!/bin/sh\n')
        f.write('# Wi-Fi configuration file created from %s by ConvertToNMCli.py at %s\n\n' % (sys.argv[1], datetime.datetime.now().isoformat()))
        for wifi in networks:
            # SSID, PASSWORD, ENCRYPTION
            emitCommand(wifi[0], wifi[1], wifi[2], outfile=f)

    print('Saved script at %s' % os.path.abspath('nmcli-wifi.sh'))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: %s /path/to/WifiConfigStore.xml' % sys.argv[0])
        sys.exit(1)
    main()