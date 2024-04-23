#!~/.pyenv/versions/3.11.6/bin/python
#
# Copyright (c) 2024 Cutieguwu | Olivia Brooks
#
# -*- coding:utf-8 -*-
# @Title: CutieDecryptor
# @Author: JellieJayde | Jayde Paquette
# @Collaborator: Cutieguwu | Olivia Brooks
# @Email: owen.brooks77@gmail.com | obroo2@ocdsb.ca
# @Description: Parses an encrypted file for patterns and characteristics.
#
# @Script: CutieParser.py
# @Date Created: 10 Apr, 2024
# @Last Modified: 15 Apr, 2024
# @Last Modified by: Cutieguwu | Olivia Brooks

# ----------------------------------------------------------
#
# Note: Script cannot be called "parser" as that clashes with stdlib module parser.
#
# ----------------------------------------------------------

<<<<<<< Updated upstream
from os import path

execDir = path.dirname(__file__)

dataLanguage = []
dataEncoded = []

print ("Start")

=======
<<<<<<< HEAD
>>>>>>> Stashed changes
def parse(dataReference, dataEncoded):
    return order(dataReference), order(dataEncoded)

def order(text:str):
    
    for character in text:

        if character.isalpha():

            pass

with open(execDir + "\\dataReference.txt", "r") as f:
    while True:
        dataLanguageChar = f.read(1).strip()

        if dataLanguageChar.isalpha():
            if dataLanguageChar.lower() not in dataLanguage:
                dataLanguage.append(dataLanguageChar.lower())

<<<<<<< Updated upstream
        if dataLanguageChar == "~":
            print (dataLanguage)
            break

with open(execDir + "\\dataEncoded19.ENC", "r") as f:
    while True:
        dataEncodedChar = f.read(1).strip()

        if dataEncodedChar.isalpha():
            if dataEncodedChar.lower() not in dataEncoded:
                dataEncoded.append(dataEncodedChar.lower())

        if dataEncodedChar == "~":
            print (dataEncoded)
            break

parse(dataLanguageChar, dataEncodedChar)
=======
parse(dataLanguage, dataEncoded)
=======
with open("dataReference.txt", "r") as f:
    data = f.read()
>>>>>>> origin/Decryption-script
>>>>>>> Stashed changes
