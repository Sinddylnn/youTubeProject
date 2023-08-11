import os
import re
from rich import print


def printHeader(header):
    for index, lines in enumerate(header):
        print(lines)

def printItemsList(ItemsList):
    for index, lines in enumerate(ItemsList):
        print(f"[{index+1}] -", lines)

def pathAlreadyExists(path): 
    return os.path.exists(path)

specialCharacters = """[ , (, ), @, #, $, %, &, *, _, [, !, ?, ", ", “, |, -,]"""  # quebram o comando de legendar
def clearName(name):
    clearedName = re.sub(specialCharacters, "_", name)
    clearedName = re.sub("]", "_", clearedName)
    return clearedName