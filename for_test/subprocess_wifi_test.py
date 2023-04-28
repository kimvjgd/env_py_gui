import subprocess
CHANGE_STATE = False
def get_wifi_list():
    cmd = 'nmcli dev wifi list'
    subprocess.call(cmd, shell=True)
    CHANGE_STATE = True

def connect_wifi(name, password):
    cmd = 'nmcli device wifi connect {} password {}'.format(name, password)
    subprocess.call(cmd, shell=True)


get_wifi_list()
connect_wifi('sangsanglab_5G', '0327107179')

'''
#####################################################################################
The Wi-Fi card on your Linux PC can't connect to the internet unless it's enabled. 
To see the status of all your network interfaces, use this command:

# nmcli dev status

#####################################################################################
If you don't know the name of your Wi-Fi access point, otherwise known as the SSID, 
you can find it by scanning for nearby Wi-Fi networks.

# nmcli dev wifi list

#####################################################################################
Replace network-ssid with the name of your network. 
If you have WEP or WPA security on your WI-Fi, 
you can specify the network password in the command as well.

# nmcli dev wifi connect network-ssid password "network-password"
'''