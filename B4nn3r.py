import socket
from colorama import Fore as f
import os
os.system("cls||clear")
class main:
    def banner(self,domain):
        try:
            ip=socket.gethostbyname(domain)
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect_ex((ip,80))
            s.send("GET /HTTP/1.1/\r\n\r\n".encode("utf-8"))
            by=s.recv(2048)
            return str(by)
        except Exception as e:
            print(f"[!]{f.RED}{e}")
            s.close()
        finally:
            s.close()
v=main()
print(f"{f.LIGHTGREEN_EX}###########        #        ###        ##")
print(f"{f.LIGHTGREEN_EX}##        #      ## ##      ## ##      ##")
print(f"{f.LIGHTGREEN_EX}##        #     ##   ##     ##   ##    ##")
print(f"{f.LIGHTGREEN_EX}###########    #########    ##    ##   ##")
print(f"{f.RED}!!        !   !!      !!    !!     !!  !!")
print(f"{f.RED}!!        !  !!        !!   !!      !! !!")
print(f"{f.RED}!!!!!!!!!!! !!          !!  !!       !!!!")
print(f"{f.BLUE} ---- A Unit of 10 tools of code ----\n{f.LIGHTCYAN_EX}[!] A Banner grabbing tool\n{f.LIGHTMAGENTA_EX}[!]created by pratv3")
grab=v.banner(input(f"{f.LIGHTCYAN_EX}[+]Enter the site address:-{f.GREEN}"))
print(f"{f.YELLOW}[!]Banner Grabbed:-\n{f.CYAN}{grab}")
