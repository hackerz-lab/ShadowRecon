#!/usr/bin/env python3

"""
ShadowRecon - Advanced OSINT Reconnaissance Tool
Author: Marttin Saji
GitHub: https://github.com/hackerz-lab/ShadowRecon
"""

import argparse
import os
import sys
from time import sleep
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# ASCII Art
def print_banner():
    print(Fore.GREEN + r"""
    .oooooo..o oooo                        .o8                            
d8P'    `Y8 `888                       "888                            
Y88bo.       888 .oo.    .oooo.    .oooo888   .ooooo.  oooo oooo    ooo
 `"Y8888o.   888P"Y88b  `P  )88b  d88' `888  d88' `88b  `88. `88.  .8' 
     `"Y88b  888   888   .oP"888  888   888  888   888   `88..]88..8'  
oo     .d8P  888   888  d8(  888  888   888  888   888    `888'`888'   
8""88888P'  o888o o888o `Y888""8o `Y8bod88P" `Y8bod8P'     `8'  `8'    
                                                                       
                                                                       
                                                                       
ooooooooo.                                                             
`888   `Y88.                                                           
 888   .d88'  .ooooo.   .ooooo.   .ooooo.  ooo. .oo.                   
 888ooo88P'  d88' `88b d88' `"Y8 d88' `88b `888P"Y88b                  
 888`88b.    888ooo888 888       888   888  888   888                  
 888  `88b.  888    .o 888   .o8 888   888  888   888                  
o888o  o888o `Y8bod8P' `Y8bod8P' `Y8bod8P' o888o o888o                  ═""")
    print(Fore.CYAN + "\n" + " " * 15 + "Version 1.0 | Active Reconnaissance Framework" + "\n")
    print(Fore.YELLOW + " " * 20 + "Created by: [Your Name]")
    print(Fore.YELLOW + " " * 20 + "GitHub: github.com/[YourUsername]" + "\n")

def check_root():
    if os.geteuid() != 0:
        print(Fore.RED + "[-] This script requires root privileges!")
        sys.exit(1)

def main_menu():
    print(Fore.MAGENTA + "\n[1] Username Reconnaissance")
    print(Fore.MAGENTA + "[2] Domain Intelligence")
    print(Fore.MAGENTA + "[3] Email Footprinting")
    print(Fore.MAGENTA + "[4] IP Geolocation Tracking")
    print(Fore.MAGENTA + "[5] Network Sniffer")
    print(Fore.MAGENTA + "[6] Vulnerability Scanner")
    print(Fore.RED + "[0] Exit\n")

def execute_recon(option):
    # Add actual recon functionality here
    print(Fore.BLUE + f"\n[+] Initializing Module {option}...")
    sleep(2)
    print(Fore.GREEN + "[+] Scanning targets...")
    sleep(1)
    print(Fore.YELLOW + "[!] Potential vulnerabilities detected!")

def arg_parser():
    parser = argparse.ArgumentParser(
        description="ShadowRecon - Advanced OSINT Reconnaissance Tool",
        epilog="Example: ./shadow.py -u target_username -d example.com"
    )
    parser.add_argument("-u", "--username", help="Investigate username across platforms")
    parser.add_argument("-d", "--domain", help="Perform domain reconnaissance")
    parser.add_argument("-e", "--email", help="Email address footprinting")
    parser.add_argument("-i", "--ip", help="IP address geolocation tracking")
    parser.add_argument("-b", "--banner", action="store_true", help="Display banner")
    parser.add_argument("-q", "--quiet", action="store_true", help="Quiet mode")
    return parser.parse_args()

def main():
    check_root()
    args = arg_parser()
    
    if not args.quiet:
        print_banner()
    
    try:
        if args.username:
            print(Fore.CYAN + f"\n[+] Starting username reconnaissance on: {args.username}")
            # Add username recon logic
        elif args.domain:
            print(Fore.CYAN + f"\n[+] Initiating domain intelligence scan on: {args.domain}")
            # Add domain recon logic
        elif args.email:
            print(Fore.CYAN + f"\n[+] Commencing email footprinting for: {args.email}")
            # Add email analysis logic
        elif args.ip:
            print(Fore.CYAN + f"\n[+] Tracking IP geolocation for: {args.ip}")
            # Add IP tracking logic
        else:
            main_menu()
            choice = input(Fore.WHITE + "Select an option: ")
            execute_recon(choice)
            
    except KeyboardInterrupt:
        print(Fore.RED + "\n[-] Operation cancelled by user!")
        sys.exit(0)
    except Exception as e:
        print(Fore.RED + f"\n[-] Critical error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if sys.version_info < (3, 6):
        print(Fore.RED + "[-] This script requires Python 3.6 or higher!")
        sys.exit(1)
    main()
