# from wifi import Cell, Scheme
# import subprocess

# def get_wifi_list():
#     cells = Cell.all('wlan0')
#     for cell in cells:
#         print(cell.ssid)
    
#     try:
#         result = subprocess.check_output(["iwgetid", "-r"])
#         print("현재 연결된 WiFi의 SSID:", result.decode().strip())
#         # self.current_wifi_label.config(text=result.decode().strip())
#         for cell in cells:
#             print(cell.ssid)
#         # 여기서 gui update해줘야한다.
#     except:
#         result = ''
        
#     # self.current_wifi_label.after(1000, self.get_wifi_list)
    
# get_wifi_list()

import wifi
import subprocess
def Search():
    wifilist = []

    cells = wifi.Cell.all('wlan0')

    for cell in cells:
        wifilist.append(cell)

    return wifilist


def FindFromSearchList(ssid):
    wifilist = Search()

    for cell in wifilist:
        if cell.ssid == ssid:
            return cell

    return False


def FindFromSavedList(ssid):
    cell = wifi.Scheme.find('wlan0', ssid)

    if cell:
        return cell

    return False


def Connect(ssid, password=None):
    cell = FindFromSearchList(ssid)

    if cell:
        savedcell = FindFromSavedList(cell.ssid)

        # Already Saved from Setting
        if savedcell:
            savedcell.activate()
            return cell

        # First time to conenct
        else:
            if cell.encrypted:
                if password:
                    scheme = Add(cell, password)

                    try:
                        scheme.activate()

                    # Wrong Password
                    except wifi.exceptions.ConnectionError:
                        Delete(ssid)
                        return False

                    return cell
                else:
                    return False
            else:
                scheme = Add(cell)

                try:
                    scheme.activate()
                except wifi.exceptions.ConnectionError:
                    Delete(ssid)
                    return False

                return cell
    
    return False


def Add(cell, password=None):
    if not cell:
        return False

    scheme = wifi.Scheme.for_cell('wlan0', cell.ssid, cell, password)
    scheme.save()
    return scheme


def Delete(ssid):
    if not ssid:
        return False

    cell = FindFromSavedList(ssid)

    if cell:
        cell.delete()
        return True

    return False


if __name__ == '__main__':
    # Search WiFi and return WiFi list
    # print Search()

    # # Connect WiFi with password & without password
    # print Connect('OpenWiFi')
    # print Connect('ClosedWiFi', 'password')

    # # Delete WiFi from auto connect list
    # print Delete('DeleteWiFi')
    # print(Search())
    Connect('sangsanglab', '0327107179')