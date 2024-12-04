################################################################

            # discord : uhq.s
            # tiktok  : https://tiktok.com/@uhq.s
            # server  : https://discord.gg/wyUuYr9DEN
            # dev     : uhq.s
            # owner   : uhq.s
            # github  : https://github.com/seized0

#################################################################

import requests
from colorama import *
import os

green = Fore.GREEN
red = Fore.RED
magenta = Fore.MAGENTA
blue = Fore.BLUE
r = Fore.WHITE
lmagenta = Fore.LIGHTMAGENTA_EX
lred = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
cyan = Fore.CYAN

async def usernamesearcher():
    os.system('cls')
    print(blue + """


.▄▄ · ▄▄▄ . ▄▄▄· ▄▄▄   ▄▄·  ▄ .▄▄▄▄ .▄▄▄  
▐█ ▀. ▀▄.▀·▐█ ▀█ ▀▄ █·▐█ ▌▪██▪▐█▀▄.▀·▀▄ █·
▄▀▀▀█▄▐▀▀▪▄▄█▀▀█ ▐▀▀▄ ██ ▄▄██▀▐█▐▀▀▪▄▐▀▀▄ 
▐█▄▪▐█▐█▄▄▌▐█ ▪▐▌▐█•█▌▐███▌██▌▐▀▐█▄▄▌▐█•█▌
 ▀▀▀▀  ▀▀▀  ▀  ▀ .▀  ▀·▀▀▀ ▀▀▀ · ▀▀▀ .▀  ▀


""")
    username = input(cyan +'[$] USERNAME : ')
    print(blue + '\nCHECKING ON instagram , tiktok , twitter, pinterest, github')


    insta = requests.get(url=f'https://www.instagram.com/{username}')
    tiktok = requests.get(url=f'https://tiktok.com/@{username}')
    x = requests.get(url=f'https://x.com/{username}')
    pinterest = requests.get(url=f'https://www.pinterest.fr/{username}')
    github = requests.get(url=f'https://github.com/{username}')
    snap = requests.get(url=f'https://www.snapchat.com/add/{username}')


    if insta.status_code ==200:
        print(green + f'{username} : FIND INSTAGRAM : https://www.instagram.com/{username}')
    else:
        print(red + 'INSTAGRAM : NOT FOUND')

    if tiktok.status_code ==200:
        print(green + f'{username} : FIND TIKTOK : https://tiktok.com/@{username}')
    else:
        print(red + 'TIKTOK : NOT FOUND')

    if x.status_code ==200:
        print(green + f'{username} : FIND TWITTER : https://x.com/{username}')

    else:
        print(red + 'TWITTER : NOT FOUND')

    if pinterest.status_code ==200:
        print(green + f'{username} : FIND PINTEREST : https://www.pinterest.fr/{username}')

    else:
        print(red + 'PINTEREST : NOT FOUND')

    if github.status_code ==200:
        print(green + f'{username} : FIND GITHUB : https://github.com/{username}')

    else:
        print(red + 'GITHUB : NOT FOUND')

    if snap.status_code ==200:
        print(green + f'{username} : FIND SNAPCHAT : https://www.snapchat.com/add/{username}')
    else:
        print(red + 'SNAPCHAT : NOT FOUND')

    input(blue + '\n\n[!] PRESS ENTER TO RETURN TO MENU')