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
# @Last Modified: 15 Apr, 2024
# @Last Modified by: Cutieguwu | Olivia Brooks
# ----------------------------------------------------------

def decrypt(dataEncoded: str, keyDecrypt: str, keyLanguage: str="etaoinshrdlcumwfgypbvkjxqz".upper()):
    """
    Decrypts a string encoded using a substitution cypher based on the provided key.\n
    Characters closer to index 0 in `key` are more common in the English language.
    Falls back on Lewand's order of English characters, most to least common, if no `keyLanguage` provided.
    """

    dataDecrypted = ""

    for c in dataEncoded:                                                               # Decrypt each character.
        is_found = False

        if c in keyDecrypt:                                                             # Attempt to decrypt each character.
            while not is_found:
                for k in keyDecrypt:
                    if c == k:                                                          # Character found in decryption key.
                        dataDecrypted = dataDecrypted + keyLanguage[keyDecrypt.index(k)]
                        is_found = True
        else:                                                                           # Failed to decrypt a character, passing and leaving character as is.
            dataDecrypted = dataDecrypted + c

    return dataDecrypted


# Code hereon is for testing purposes only. Please use main.py for general use.

with open("dataEncoded19.ENC", "r") as f:
    data = "".join(c for c in f.read() if c != "\n")

"""
with open("keyEnglish.txt", "r") as f:
    key = "".join(c for c in f.read() if c != "\n")
"""
 
key = "qwertyuiopasdfghjklzxcvbnm"                                                      # Temporary - Faux testing key.

print(decrypt(data, key))