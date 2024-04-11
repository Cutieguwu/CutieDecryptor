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
# @Last Modified: 11 Apr, 2024
# @Last Modified by: Cutieguwu | Olivia Brooks
# ----------------------------------------------------------

def decrypt(dataEncoded: str, key: str):
    """
    Decrypts a string encoded using a substitution cypher based on the provided key.\n
    Characters closer to index 0 in `key` are more common in the English language.
    """

    dataDecrypted = ""

    # Convert key to a list.
    keyDecrypt = [].append(k for k in key)
    keyEnglish = [].append(k for k in "etaoinshrdlcumwfgypbvkjxqz")                         # Lewand's order of english characters; most to least common.

    for c in dataEncoded:
        is_found = False

        while not is_found:
            for k in keyDecrypt:
                if c == k:                                                                  # Character found in decryption key.
                    dataDecrypted = dataDecrypted + keyEnglish[keyDecrypt.index(k)]
                    is_found = True
    
    return dataDecrypted

