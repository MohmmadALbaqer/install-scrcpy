import os
from colorama import Fore, Style, Back
os.system("clear")

print(f'''   
{Fore.GREEN}                                               
  ___ __ _ _ __ _ __ _  _ 
 (_-</ _| '_/ _| '_ \ || |
 /__/\__|_| \__| .__/\_, |
               |_|   |__/      

{Fore.RED}+------------------------------------------------------------------+
{Fore.RED}|{Fore.GREEN} GitHub{Fore.WHITE} : {Fore.BLUE}MohmmadALbaqer {Fore.WHITE}|{Fore.YELLOW} https://www.github.com/MohmmadALbaqer/ {Fore.RED}|
{Fore.RED}|{Fore.GREEN} Instagram{Fore.WHITE} :{Fore.BLUE} r94xs {Fore.WHITE}      |{Fore.YELLOW} https://www.instagram.comr94xs/        {Fore.RED}|
{Fore.RED}+------------------------------------------------------------------+{Style.RESET_ALL}''')    

def connect_via_usb():
    print(f"""{Fore.YELLOW}     
         _   
 _ _ ___| |_ 
| | |_ -| . |
|___|___|___|           
{Style.RESET_ALL}""")
    input(f"""{Fore.WHITE}[{Fore.MAGENTA}*{Fore.WHITE}] {Fore.BLUE}Following Tracks About {Fore.GREEN}[{Fore.YELLOW}USB{Fore.GREEN}] {Style.RESET_ALL}
+----+-------------------+
| {Fore.MAGENTA}ID{Style.RESET_ALL} | {Fore.GREEN}Tracking{Style.RESET_ALL}          |
+----+-------------------+
| {Fore.BLUE}1{Style.RESET_ALL}  | {Fore.YELLOW}Settings{Style.RESET_ALL}          |
| {Fore.BLUE}2{Style.RESET_ALL}  | {Fore.YELLOW}Developer Options{Style.RESET_ALL} |
| {Fore.BLUE}3{Style.RESET_ALL}  | {Fore.YELLOW}USB debugging{Style.RESET_ALL}     |
+----+-------------------+
{Fore.WHITE}[{Fore.MAGENTA}*{Fore.WHITE}] If complete click {Fore.GREEN}[Enter]{Style.RESET_ALL}""")
    os.system("pkill scrcpy")
    os.system("adb kill-server")
    os.system("adb start-server")
    os.system("adb devices")
    os.system("scrcpy -d")

def connect_via_wifi(device_ip):
    os.system("pkill scrcpy")
    os.system("adb tcpip 5555")
    os.system(f"adb connect {device_ip}:5555")
    os.system(f"scrcpy -b 2M --max-size 800 --display {device_ip}")
    os.system("scrcpy -e")
def main():
    print(f"{Fore.WHITE}[{Fore.BLUE}*{Fore.WHITE}] {Fore.YELLOW}Choose the method:{Style.RESET_ALL}")
    print(f"{Fore.WHITE}[{Fore.GREEN}1{Fore.WHITE}] {Fore.BLUE}Connect By USB{Style.RESET_ALL}")
    print(f"{Fore.WHITE}[{Fore.GREEN}2{Fore.WHITE}] {Fore.BLUE}Connect By TCP/IP{Style.RESET_ALL}")

    choice = input(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.YELLOW}Enter the option (1 or 2): {Fore.BLUE}")
    print(f"{Style.RESET_ALL}")
    if choice == "1":
        connect_via_usb()
    elif choice == "2":
        print(f"""{Fore.YELLOW}
 ___
__H__        _            
 [{Back.RED}:{Style.RESET_ALL}{Fore.YELLOW}] ___   _| |_ ___ ___ 
 [{Back.RED}:{Style.RESET_ALL}{Fore.YELLOW}]| . | |_   _|  _| . |
 [{Back.RED}.{Style.RESET_ALL}{Fore.YELLOW}]|  _|   | | |___|  _|
  V |_|     |_|     |_|         
{Style.RESET_ALL}""")
        input(f"""{Fore.WHITE}[{Fore.MAGENTA}*{Fore.WHITE}] {Fore.BLUE}Following Tracks About {Fore.GREEN}[{Fore.YELLOW}IP/TCP{Fore.GREEN}] {Style.RESET_ALL}
+----+--------------------+
| {Fore.MAGENTA}ID{Style.RESET_ALL} | {Fore.GREEN}Tracking{Style.RESET_ALL}           |
+----+--------------------+
| {Fore.BLUE}1{Style.RESET_ALL}  | {Fore.YELLOW}Settings{Style.RESET_ALL}           |
| {Fore.BLUE}2{Style.RESET_ALL}  | {Fore.YELLOW}About Phone{Style.RESET_ALL}        |
| {Fore.BLUE}3{Style.RESET_ALL}  | {Fore.YELLOW}Status information{Style.RESET_ALL} |
| {Fore.BLUE}4{Style.RESET_ALL}  | {Fore.YELLOW}IP arrress{Style.RESET_ALL}         |
+----+--------------------+
{Fore.WHITE}[{Fore.MAGENTA}*{Fore.WHITE}] If complete click {Fore.GREEN}[Enter]{Style.RESET_ALL}""")
        device_ip = input(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.YELLOW}Enter the IP address of the device: {Fore.MAGENTA}")
        print(f"{Style.RESET_ALL}")
        connect_via_wifi(device_ip)
    else:
        print(f"{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}] {Fore.RED}Invalid option{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
