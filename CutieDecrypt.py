#!~/.pyenv/versions/3.11.6/bin/python
#
# Copyright (c) 2024 Cutieguwu | Olivia Brooks
#
# -*- coding:utf-8 -*-
# @Title: CutieDecryptor
# @Author: Cutieguwu | Olivia Brooks
# @Collaborator: JellieJayde | Jayde Paquette
# @Email: owen.brooks77@gmail.com | obroo2@ocdsb.ca
# @Description: Decrypts a file.
#
# @Script: CutieDecrypt.py
# @Date Created: 10 Apr, 2024
# @Last Modified: 13 Apr, 2024
# @Last Modified by: Cutieguwu | Olivia Brooks
# ----------------------------------------------------------

def decrypt(dataEncoded: str, keyDecrypt: str, keyEnglish: str):
    """
    Decrypts a string encoded using a substitution cypher based on the provided key.\n
    Characters closer to index 0 in `key` are more common in the English language.
    """

    dataDecrypted = ""

    for c in dataEncoded:
        is_found = False

        if c != " ":
            while not is_found:
                for k in keyDecrypt:
                    if c == k:                                                          # Character found in decryption key.
                        dataDecrypted = dataDecrypted + keyEnglish[keyDecrypt.index(k)]
                        is_found = True
        else:
            dataDecrypted = dataDecrypted + c
    return dataDecrypted

with open("dataEncoded.txt", "r") as f:
    data = "".join(c for c in f.read() if c != "\n")

with open("key.txt", "r") as f:
    key = "".join(c for c in f.read() if c != "\n")

key = "qwertyuiopasdfghjklzxcvbnm"                                                      # Temporary - Faux testing key.
english = "etaoinshrdlcumwfgypbvkjxqz"                                                  # Temporary - Lewand's order of english characters; most to least common.

print(decrypt(data, key, english))