import sys
import os
import time

def Loading():
        for _ in range(2):
            os.system ("clear")
            print(" |")
            time.sleep(0.1)
            os.system ("clear")
            print(" /")
            time.sleep(0.1)
            os.system ("clear")
            print(" -")
            time.sleep(0.1)
            os.system ("clear")
            print(" \ ")
            time.sleep(0.1)
            os.system ("clear")
            print(" |")
            time.sleep(0.1)
            os.system ("clear")
            print(" /")
            time.sleep(0.1)
            os.system ("clear")
            print(" -")
            time.sleep(0.1)
            os.system ("clear")
            print(" \ ")

def Header():
    os.system ("clear")
    print("+――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――+")
    time.sleep(0.3)
    print("|                                                    Pyki - The offline wiki                                                     |")
    time.sleep(0.3)
    print("+――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――+")
    time.sleep(0.3)
def Footer():
    print("+――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――+")
    time.sleep(0.3)
    print("|                                                         Pyki - Lepidus                                                         |")
    time.sleep(0.3)
    print("+――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――+")
    time.sleep(0.3)

    sys.stdout.flush()
def SearchBar():
    print("")
    command = input("Search: ")
    return command
def Logo():
    print(" ")
    print('ooooooooo.               oooo    oooo  o8o   THE VERY')
    print('`888   `Y88.             `888   .8P´   `"´   PYTHON')
    print(' 888   .d88´ oooo    ooo  888  d8´    oooo   OFFLINE')
    print(' 888ooo88P´   `88.  .8´   88888[      `888   WIKIPEDIA')
    print(' 888           `88..8´    888`88b.     888   FOR YOUR LINUX')
    print(' 888            `888´     888  `88b.   888   DISTRO!')
    print('o888o            .8´     o888o  o888o o888o  ')
    print('             .o..P´                          ')
    print('             `Y8P´                           made by lepidus')
    print(" ")
def SetSearch():
    command = SearchBar()
    if command == "hi":
        print("you said hi!")
    else:
        print("      .o     .oooo.         .o                      ooooo      ooo               .             oooooooooooo                                         .o8  ")
        print("    .d88    d8P'`Y8b      .d88                      `888b.     `8'             .o8             `888'     `8                                        .888  ")
        print("  .d'888   888    888   .d'888                       8 `88b.    8   .ooooo.  .o888oo            888          .ooooo.  oooo  oooo  ooo. .oo.    .oooo888  ")
        print(".d'  888   888    888 .d'  888                       8   `88b.  8  d88' `88b   888              888oooo8    d88' `88b `888  `888  `888P'Y88b  d88' `888  ")
        print("88ooo888oo 888    888 88ooo888oo      o8o            8     `88b.8  888   888   888              888         888   888  888   888   888   888  888   888  ")
        print("     888   `88b  d88'      888        `*'            8       `888  888   888   888 .            888         888   888  888   888   888   888  888   888  ")
        print("    o888o   `Y8bd8P'      o888o       o8o           o8o        `8  `Y8bod8P'   `888*           o888o        `Y8bod8P'  `V88VV8P' o888o o888o `Y8bod88P´  ")
        print(" ")
              
def Main():
    Loading()
    Header()
    Logo()
    SetSearch()
    SearchBar()
    SetSearch()
    Footer()

Main()