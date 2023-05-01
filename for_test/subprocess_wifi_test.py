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

# nmcli dev wifi connect "network-ssid" password "network-password"
'''
'''

[['olleh_GiGA_WiFi_05A8', -52], ['olleh_WiFi_05A8', -40], ['U+NetF230', -67], 
 ['AT_410_AFAN_910604_WW_ee0e', -49], ['AP-408-701', -50], ['U+Net479C', -62]
// Good (Green)
 00:07:89:30:05:AB  olleh_WiFi_05A8             Infra  4     130 Mbit/s>   -40
40:B0:34:58:ED:74  DIRECT-76-HP OfficeJet 7510  Infra  4     65 Mbit/s >    
64:CB:E9:3F:EE:0E  AT_410_AFAN_910604_WW_ee0e   Infra  11    65 Mbit/s >    -49
E8:54:84:14:34:7C  AP-408-701                   Infra  5     270 Mbit/s>    -50
// Soso (Yellow)
00:07:89:30:05:AC  olleh_GiGA_WiFi_05A8         Infra  149   270 Mbit/s>    -52
08:5D:DD:84:47:9B  U+Net479C                    Infra  10    130 Mbit/s>    -62
// Bad (PInk)
08:5D:DD:AC:F2:2F  U+NetF230                    Infra  9     130 Mbit/s>    -67
'''