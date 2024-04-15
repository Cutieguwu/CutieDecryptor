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
# @Last Modified: 11 Apr, 2024
# @Last Modified by: Cutieguwu | Olivia Brooks

# ----------------------------------------------------------
#
# Note: Script cannot be called "parser" as that clashes with stdlib module parser.
#
# ----------------------------------------------------------

def parse(dataReference, dataEncoded):
    return order(dataReference), order(dataEncoded)

def order(text:str):
    
    for character in text:

        if character.isalpha():

            pass

with open("dataReference.txt", "r") as f:
    dataLanguage = f.read()

with open("dataEncoded19.ENC", "r") as f:
    dataEncoded = f.read()

parse(dataLanguage, dataEncoded)