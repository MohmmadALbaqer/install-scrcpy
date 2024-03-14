import os
from colorama import Fore, Style
os.system("clear")

print(f'''   
{Fore.GREEN}                         
  _________________ ___________________ _______________ ___ 
 /   _____/_   ___ \\______   \_   ___ \\______   \__  |   |
 \_____  \/    \  \/ |       _/    \  \/ |     ___//   |   |
 /        \     \____|    |   \     \____|    |    \____   |
/_______  /\______  /|____|_  /\______  /|____|    / ______|
        \/        \/        \/        \/           \/    

{Fore.RED}+------------------------------------------------------------------+
{Fore.RED}|{Fore.GREEN} GitHub{Fore.WHITE} : {Fore.BLUE}MohmmadALbaqer {Fore.WHITE}|{Fore.YELLOW} https://www.github.com/MohmmadALbaqer/ {Fore.RED}|
{Fore.RED}|{Fore.GREEN} Instagram{Fore.WHITE} :{Fore.BLUE} r94xs {Fore.WHITE}      |{Fore.YELLOW} https://www.instagram.comr94xs/        {Fore.RED}|
{Fore.RED}+------------------------------------------------------------------+
{Style.RESET_ALL}''')    



def connect_via_usb():
    input(f"[*] Go to {Fore.MAGENTA}---> {Fore.YELLOW}Settings {Fore.MAGENTA}---> {Fore.YELLOW}Developer Options {Fore.MAGENTA}---> {Fore.YELLOW}USB debugging {Fore.MAGENTA}---> {Fore.WHITE}If complete click {Fore.GREEN}[Enter]{Style.RESET_ALL}")
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
    print(f"{Fore.WHITE}[{Fore.GREEN}1{Fore.WHITE}] {Fore.BLUE}Connect via USB{Style.RESET_ALL}")
    print(f"{Fore.WHITE}[{Fore.GREEN}2{Fore.WHITE}] {Fore.BLUE}Connect via TCP/IP{Style.RESET_ALL}")

    choice = input(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.YELLOW}Enter the option (1 or 2): {Style.RESET_ALL}")
    print(f"{Style.RESET_ALL}")
    if choice == "1":
        connect_via_usb()
    elif choice == "2":
        input(f"[*] Go to {Fore.YELLOW}Settings {Fore.MAGENTA}---> {Fore.YELLOW}About Phone {Fore.MAGENTA}---> {Fore.YELLOW}Status information {Fore.WHITE}takeing {Fore.YELLOW}IP arrress {Fore.WHITE}If complete click {Fore.GREEN}[Enter]{Style.RESET_ALL}")
        device_ip = input(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.YELLOW}Enter the IP address of the device: {Style.RESET_ALL}")
        connect_via_wifi(device_ip)
    else:
        print(f"{Fore.YELLOW}[{Fore.RED}!{Fore.YELLOW}] {Fore.RED}Invalid option{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
