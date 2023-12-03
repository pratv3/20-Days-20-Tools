import scapy.all as scapy
from colorama import Fore as f
import os
os.system("cls||clear")
class main:
    def scanner(self,ip,packinfo=False):
        l=scapy.ARP(pdst=str(ip))
        brd=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
# that "/" operator is dividing operator but in scapy this 
# fn is overloaded and named as the joining oprator
        print(f"{f.LIGHTGREEN_EX} IP Address\t\tMAC Address\n--------------------------------------")
        k=brd/l
        n=scapy.srp(k,timeout=1,verbose=0)
        if packinfo==True:
            print(scapy.ls(l))
        b=0
        try:
            for dev in n[0][0]:
                b+=1
                print(f"{f.WHITE}[{b}] {f.LIGHTRED_EX}{dev[1].psrc}\t\t{f.LIGHTYELLOW_EX}{dev[1].hwsrc}")
            print(f"{f.LIGHTGREEN_EX}[!]Total Devices fount in {ip} are {b}")
        except Exception as e:
            print(e)
demon=main()
print(f"*"*100)
print(f"{f.LIGHTYELLOW_EX}          [HACKED]           [IP-STACKING]      [MAC-IDENTIFYING]    ")
print(f"{f.LIGHTMAGENTA_EX}---------------------------A UNIT OF 20 DAYS 20 TOOLS---------------------------------                     ")
print(f"{f.LIGHTYELLOW_EX}!!!!!!!!!!!!!!!!!! TOOL 2:- THE R-FINDER!!!!!!!!!!!!!!!!!!                 ")
print(f"{f.LIGHTCYAN_EX}A FORENSIC TOOLKIT USED FOR CHECKING OUT  ACTIVE DEVICES IN NETWORK \n{f.YELLOW}[!] devloped by pratv3  \n            ")
print(f"{f.LIGHTBLUE_EX}      ##########################")
print(f"{f.LIGHTBLUE_EX}      ########          #########")
print(f"{f.LIGHTBLUE_EX}     ######### {f.WHITE}R-FINDER{f.LIGHTBLUE_EX} #########")
print(f"{f.LIGHTBLUE_EX}    ##########          #########")
print(f"{f.LIGHTBLUE_EX}   ##############################")
print(f"{f.LIGHTBLUE_EX}  ###############################")
print(f"{f.LIGHTBLUE_EX} ################################")
print(f"{f.LIGHTBLUE_EX} ################################")
print(f"{f.LIGHTBLUE_EX} ################################")
print(f"{f.LIGHTBLUE_EX} #########                       ")
print(f"{f.LIGHTBLUE_EX} ########  {f.WHITE}&&&& speaks &&&&&& {f.LIGHTCYAN_EX}[!!!! Kaam Chal Raha Doosri se !!!!]{f.LIGHTBLUE_EX}")
print(f"{f.LIGHTBLUE_EX}   ######                        ")
print(f"{f.LIGHTBLUE_EX}    ##############################")
print(f"{f.LIGHTBLUE_EX}     #############################")
print(f"{f.LIGHTBLUE_EX}      ############################")
print(f"*"*100)
b=str(input(f"{f.LIGHTYELLOW_EX}[!] Enter the ip Address or range:-"))
demon.scanner(b)