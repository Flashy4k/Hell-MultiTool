################################################################

            # discord : bsyy
            # server  : https://discord.gg/QtBftsYhyR
            # dev     : bsyy, Oxbenz. And Space785
            # owner   : bsyy
            # github  : https://github.com/Flashy4k

#################################################################

import asyncio
from pystyle import *
from colorama import *
import os
import time
from utilities.Program import accountcleaner,frienddeleter, groupleaver,dmdeleter, friendsidscrapper,phonelookup, toolinfo,subdomainfinder, srcdumper, accnuker, iplookup, credits,hypesquadchanger, usernamesearcher, statuschanger, idtotoken, webhooksdeleter, webhookspammer,tokenchecker,py2exe,obf,tokenleaver,domainlookup,doxtool,dmall
import ctypes
import sys
import random
import requests
import subprocess
import seizcord
import seizhooks




green = Fore.GREEN
red = Fore.RED
magenta = Fore.MAGENTA
blue = Fore.BLUE
r = Fore.WHITE
lmagenta = Fore.LIGHTMAGENTA_EX
lred = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
cyan = Fore.CYAN
lgreen = Fore.LIGHTGREEN_EX
lblue = Fore.LIGHTBLUE_EX



def contitle(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

txt = "⭐ By Bsyy    |    Hell v3.1 🐬"


banner = """
                                                     
    @@@  @@@  @@@@@@@@  @@@       @@@       
    @@@  @@@  @@@@@@@@  @@@       @@@       
    @@!  @@@  @@!       @@!       @@!        PRESS ENTER
     !@!  @!@  !@!       !@!       !@!        
     @!@!@!@!  @!!!:!    @!!       @!!        V3
     !!!@!!!!  !!!!!:    !!!       !!!       
     !!:  !!!  !!:       !!:       !!:       
    :!:  !:!  :!:        :!:       :!:      
     ::   :::   :: ::::   :: ::::   :: ::::  
       :   : :  : :: ::   : :: : :  : :: : :  
                                                    
"""

banner1 = """
                                                     

     )       (     (     
   ( /(       )\ )  )\ )  
  )\()) (   (()/( (()/(  
  ((_)\  )\   /(_)) /(_)) 
  _((_)((_) (_))  (_))      PRESS ENTER
 | || || __|| |   | |       
 | __ || _| | |__ | |__     V3
 |_||_||___||____||____| 
                               

                                                    
"""


banner2 = """


          :::    ::: :::::::::: :::        :::  
        :+:    :+: :+:        :+:        :+:   
        +:+    +:+ +:+        +:+        +:+    
           +#++:++#++ +#++:++#   +#+        +#+     
          +#+    +#+ +#+        +#+        +#+          PRESS ENTER
          #+#    #+# #+#        #+#        #+#        
       ###    ### ########## ########## ##########     V3


"""


banner3 = """

=======================================================
 ====  ==        ==  ========  =======                  PRESS ENTER
 ====  ==  ========  ========  =======
  ====  ==  ========  ========  =======
  ====  ==  ========  ========  =======
=        ==      ====  ========  =======
  ====  ==  ========  ========  =======
  ====  ==  ========  ========  =======                 V3
  ====  ==  ========  ========  =======
  ====  ==        ==        ==        =
=======================================================

"""


bannermenu = rf"""
                                        ▄█    █▄       ▄████████  ▄█        ▄█       
                                       ███    ███     ███    ███ ███       ███       
                                       ███    ███     ███    █▀  ███       ███       
                                      ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███       ███       
                                     ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███       ███       
                                       ███    ███     ███    █▄  ███       ███       
                                       ███    ███     ███    ███ ███▌   ▄  ███▌   ▄ 
                                       ███   █▀      ██████████ █████▄▄██ █████▄▄██ 
                                                            ▀        ▀                               
[!] https://discord.gg/QtBftsYhyR                        
                                                        
[+] https://github.com/Flashy4k/Hell-MultiTool         [ UTILITIES ]
                                                                                                          Dev: bsyy
    ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
                                
              {lred}[1] SUBDOMAIN FINDER               {yellow}[5] PY TO EXE                {green}[9]  USERNAME TRACKER
                                                                                                                   
             {red} [2] SRC DUMPER                     {yellow}[6] OBFUSCATOR               {green}[10] DOX TOOL
                                                                                                                    
              {lred}[3] IP LOOKUP                      {yellow}[7] DOMAIN LOOKUP                
                                                                                                                   
             {red} [4] PHONE LOOKUP                   {yellow}[8] TOOLS INFOS              {red}[00] NEXT PAGE -->        
           
    ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

"""


bannermenu2 = rf"""
                                        ▄█    █▄       ▄████████  ▄█        ▄█       
                                       ███    ███     ███    ███ ███       ███       
                                       ███    ███     ███    █▀  ███       ███       
                                      ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███       ███       
                                     ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███       ███       
                                       ███    ███     ███    █▄  ███       ███       
                                       ███    ███     ███    ███ ███▌   ▄  ███▌   ▄ 
                                       ███   █▀      ██████████ █████▄▄██ █████▄▄██ 
                                                            ▀        ▀         

[!] https://discord.gg/QtBftsYhyR
                                                               
                                                        [ DISCORD ]
[+] https://github.com/Flashy4k/Hell-MultiTool                                                                 
                                                                                                         Dev: bsyy  
    ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
                                
              {blue}[11] WEBHOOK SPAMMER         {cyan}[15] ACCOUNT NUKER          {lmagenta}[19] GROUP LEAVER
                                                                                                                   
              {blue}[12] WEBHOOK DELETER         {cyan}[16] HYPESQUAD CHANGER      {lmagenta}[20] DM ALL  
                                                                                                                    
              {blue}[13] TOKEN LEAVER            {cyan}[17] ID TO TOKEN             
                                                                                                                   
              {blue}[14] TOKEN CHECKER           {cyan}[18] STATUS CHANGER         {cyan}[00] NEXT PAGE -->
                                                                       {cyan}[01] <-- PREV PAGE
           
    ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

"""

bannermenu3 = rf"""
                                        ▄█    █▄       ▄████████  ▄█        ▄█       
                                       ███    ███     ███    ███ ███       ███       
                                       ███    ███     ███    █▀  ███       ███       
                                      ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███       ███       
                                     ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███       ███       
                                       ███    ███     ███    █▄  ███       ███       
                                       ███    ███     ███    ███ ███▌   ▄  ███▌   ▄ 
                                       ███   █▀      ██████████ █████▄▄██ █████▄▄██ 
                                                            ▀        ▀                                                                     

[!] https://discord.gg/QtBftsYhyR
                                                                   
                                                  [ DISCORD / OTHERS ]
[+] https://github.com/Flashy4k/Hell-MultiTool
                                                                                                        Dev: byy
    ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
                                
              [21] ID SCRAPPER        [25]           [29] 
                                                                                                                   
              [22] DM DELETER         [26]           [30]   
                                                                                                                    
              [23] FRIENDS DELETER    [27]            
                                                                                                                   
              [24] ACCOUNT CLEANER    [28]           [00] <-- PREV PAGE 
           
    ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

"""
