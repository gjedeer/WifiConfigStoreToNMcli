import qrcode
import os
import xml.etree.ElementTree as ET

def createQR(ssid, password, encryption, hidden="false"):
    #WIFI:S:<SSID>;T:<WEP|WPA|blank>;P:<PASSWORD>;H:<true|false|blank>;;
    # Create the string using the variables
    connection_string = f"WIFI:S:{ssid};T:{encryption};P:{password};H:{hidden};"
    print(connection_string)

    # Create the QR code
    img = qrcode.make(connection_string)

    # Save the QR code
    image_name = f"{ssid}.png"
    
    # Skip if the name has a *
    if "*" in image_name:
        return
    
    # Skip if the file already exists
    if not os.path.exists(image_name):
        img.save("QR/" + image_name)
    
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
    networks = extractNetwork("WifiConfigStore.xml")
    
    for wifi in networks:
        # SSID, PASSWORD, ENCRYPTION
        createQR(wifi[0], wifi[1], wifi[2])


if __name__ == "__main__":
    main()