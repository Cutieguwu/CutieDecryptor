#!~/.pyenv/versions/3.11.6/bin/python
#
# Copyright (c) 2024 Cutieguwu | Olivia Brooks
#
# -*- coding:utf-8 -*-
# @Title: CutieDecryptor
# @Author: Cutieguwu | Olivia Brooks
# @Collaborator: JellieJayde | Jayde Paquette
# @Email: owen.brooks77@gmail.com | obroo2@ocdsb.ca
# @Description: All-in-one script to decrypt substitution cyphers.
#
# @Script: main.py
# @Date Created: 10 Apr, 2024
# @Last Modified: 15 Apr, 2024
# @Last Modified by: Cutieguwu | Olivia Brooks
# ----------------------------------------------------------

import CutieDecrypt, CutieParser

with open(input("Enter path of encrypted file relative to script execution point: "), "r") as f:
    dataEncoded = "".join(c for c in f.read() if c != "\n")

with open("key.txt", "r") as f:
    dataReference = "".join(c for c in f.read() if c != "\n")

keys = CutieParser.parse(dataReference, dataEncoded)

print(CutieDecrypt.decrypt(dataEncoded, keys[0], keys[1]))