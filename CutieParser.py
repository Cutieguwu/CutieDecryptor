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
# @Last Modified: 23 Apr, 2024
# @Last Modified by: Cutieguwu | Olivia Brooks

# ----------------------------------------------------------
#
# Note: Script cannot be called "parser" as that clashes with stdlib module parser.
#
# ----------------------------------------------------------

from os import path

execDir = path.dirname(__file__)


def parse(dataReference, dataEncoded):
    return order(dataReference), order(dataEncoded)

def order(file):

    dataLanguage = []
    amount = []
    index = 0

    with open(execDir + file, "r") as f:
        while True:
            fileChar = f.read(1).strip()

            if fileChar.isalpha():
                if fileChar.lower() not in dataLanguage:
                    dataLanguage.append(fileChar.lower())
                    amount.append(1)

                else:
                    index = 0
                    while True:
                        if dataLanguage[index] == fileChar.lower():
                            amount[index] = amount[index] + 1
                            break

                        else:
                            index = index + 1

            if fileChar == "~":
                index = 0
                Finished = False

                while not Finished:
                    Finished = True

                    for index in range(0, len(amount) - 1):
                        temp = amount[index]
                        tempLetter = dataLanguage[index]

                        if temp < amount[index + 1]:
                            amount[index] = amount[index + 1]
                            amount[index + 1] = temp

                            dataLanguage[index] = dataLanguage[index + 1]
                            dataLanguage[index + 1] = tempLetter

                            Finished = False

                        if index == len(amount):
                            index = 0

                return dataLanguage, amount

print (order("\\dataReference.txt"), "\n")
print (order("\\dataEncoded19.ENC"), "\n")