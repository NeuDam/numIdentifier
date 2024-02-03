#!/usr/bin/python3

import sys, os, json
from colorama import Fore, init
from modules.requests_operators import movistar_checker, wom_checker, tigo_checker, claro_checker

clearConsole = lambda: os.system('cls' if os.name == 'nt' else 'clear')

init()

#COLOURS 
RED_COLOR = Fore.LIGHTRED_EX
GREEN_COLOR = Fore.LIGHTGREEN_EX
PURPLE_COLOR = Fore.MAGENTA
CYAN_COLOR = Fore.LIGHTCYAN_EX
DEFAULT_COLOR = Fore.RESET

def banner_text():

  text = f''' {PURPLE_COLOR}
 ▐ ▄ ▄• ▄▌• ▌ ▄ ·. ▪  ·▄▄▄▄  ▄▄▄ . ▐ ▄ ▄▄▄▄▄▪  ·▄▄▄▪  ▄▄▄ .▄▄▄  
•█▌▐██▪██▌·██ ▐███▪██ ██▪ ██ ▀▄.▀·•█▌▐█•██  ██ ▐▄▄·██ ▀▄.▀·▀▄ █·
▐█▐▐▌█▌▐█▌▐█ ▌▐▌▐█·▐█·▐█· ▐█▌▐▀▀▪▄▐█▐▐▌ ▐█.▪▐█·██▪ ▐█·▐▀▀▪▄▐▀▀▄ 
██▐█▌▐█▄█▌██ ██▌▐█▌▐█▌██. ██ ▐█▄▄▌██▐█▌ ▐█▌·▐█▌██▌.▐█▌▐█▄▄▌▐█•█▌
▀▀ █▪ ▀▀▀ ▀▀  █▪▀▀▀▀▀▀▀▀▀▀▀•  ▀▀▀ ▀▀ █▪ ▀▀▀ ▀▀▀▀▀▀ ▀▀▀ ▀▀▀ .▀  ▀
'''

  print(text)

def main(p):

  print(GREEN_COLOR)

  print(f'{CYAN_COLOR}Checking: {DEFAULT_COLOR}1/4', end='\r')

  res_movistar = movistar_checker(p)

  if res_movistar:
    exit(f'{GREEN_COLOR}{res_movistar}')

  print(f'{CYAN_COLOR}Checking: {DEFAULT_COLOR}2/4', end='\r')

  res_wom = wom_checker(p)

  if res_wom:
    exit(f'{GREEN_COLOR}{res_wom}')

  print(f'{CYAN_COLOR}Checking: {DEFAULT_COLOR}3/4', end='\r')

  res_tigo = tigo_checker(p)

  if res_tigo:
    exit(f'{GREEN_COLOR}{res_tigo}')


  print(f'{CYAN_COLOR}Checking: {DEFAULT_COLOR}4/4', end='\r')

  res_claro = claro_checker(p)

  if res_claro:
    exit(f'{GREEN_COLOR}{res_claro}')

  print(RED_COLOR+'\n\nSorry, the phone number has not been found, check it or try again later\n')

if __name__ == '__main__':

  clearConsole()

  banner_text()

  if len(sys.argv) != 2:
    print(RED_COLOR +  f'\nError, use: python main.py <phone_number>\n')
    sys.exit(1)
  else:
    if len(sys.argv[1]) != 10:
      print(RED_COLOR+'\nError bad number format, len 10\n')
      sys.exit(1)

  main(sys.argv[1])