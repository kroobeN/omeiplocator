
import pyshark
import time
import json
from pyshark.capture.capture import Capture
import requests
from multiprocessing import Process

from requests.api import get

discord_ip = '188.122.76.54'
discord_ip2 = '213.163.95.7'
discord_ip3 = '213.163.87.171'
teamspeak_ip = '84.252.122.31'
homenetwork = '192.168.0.0/16'
valve_ip = '155.133.248.38'
target_ip = ''
displayfilter = '!(ip.src == ' + homenetwork +') && !(ip.addr == ' + teamspeak_ip +') && !(ip.addr == ' + discord_ip + ') && !(ip.addr == ' + valve_ip + ') && !(ip.addr == ' + discord_ip2 + ') && !(ip.addr == ' + discord_ip3 + ') && udp && !(mdns) && !(dns)'


def get_traffic():
    capture = pyshark.LiveCapture(interface='ethernet', display_filter=displayfilter)
    for packet in capture:
        if 'IP' in packet:
            global target_ip
            target_ip = packet.ip.src
        
            


def ip_geolocation(ip):
    json_data = requests.get('http://ip-api.com/json/'+ ip)
    output = json_data.json()
    print(output)
    print(ip)
    opfer_land = output['country']
    opfer_region = output['regionName']
    opfer_stadt = output['city']
    opfer_isp = output['isp']
    print(f'''
    -----------------------------
    Land: {opfer_land}
    Region: {opfer_region}
    Stadt: {opfer_stadt}
    ISP: {opfer_isp}
    -----------------------------
    ''')

def ip_loop():
    while True:
        print(target_ip)
        ip_geolocation(target_ip)
        time.sleep(2)



if __name__ == '__main__':
    Process(target=get_traffic).start()
    Process(target=ip_loop).start()


