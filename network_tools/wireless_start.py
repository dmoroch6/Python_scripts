###########FIRST SCRIPT OF MY LIFE, IM SO HAPPY AND HONESTLY I'LL LOVE TO SEE WHAT THE FUTURE ME THINK OF MY FIRST TRY################
###This script was created to solve a Prox Mox wireless conection, since it's a server it's made to work mainly wired and I've been running the same wpa_script every single time it reset or give up ip. 
###I'm doing a OOP course online and that's why the style of the code instead of a simplier amd cleaner code. Still, I'm learning and want to see my progress over time. 
###NOTE: IMPROVE THE CODE SO IT'S EASIER TO MANAGE, AND LOOK PROFESSIONAL. --> LEARN OF IT.
import subprocess

import subprocess

interface_name = str(input(f"\n[+] Using command 'ip a' type the interface name: "))

class ConfigureConnection:
    def __init__(self, interface):
        self.interface = interface
        self.interface_alias = {interface:"home_wifi_card"}

    def interface_rename(self):
        interface_to_rename = str(input(f"\nType the interface to rename: "))
        
        if interface_to_rename in self.interface_alias:
                self.interface_alias[interface_to_rename] = str(input("Type the new name: "))
        else:
                print("Please write a valid interface.")
           

    def interface_wireless_connection(self):
        subprocess.run(["touch", "/etc/network/wpa_supplicant/wpa_supplicant.conf"],check=True)
        subprocess.run(['wpa_supplicant', '-B',
                       '-i', self.interface,
                       '-c', '/etc/network/wpa_supplicant/wpa_supplicant.conf'],check=True)
    
    def interface_show(self):
        for interface,alias in self.interface_alias.items():
            print(f"\nInterface -> {interface}\nAlias -> {alias}")


a = ConfigureConnection(interface_name)

print(f'\n--> Showing interface before assigning alias:')
a.interface_show()
a.interface_rename()
print(f'\n--> Showing interface after assigning alias:')
a.interface_show()
a.interface_wireless_connection()
