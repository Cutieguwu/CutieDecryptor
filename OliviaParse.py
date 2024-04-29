#!~/.pyenv/versions/3.11.6/bin/python
#
# Copyright (c) 2024 Cutieguwu | Olivia Brooks
#
# -*- coding:utf-8 -*-
# @Title: OliviaParser
# @Author: Cutieguwu | Olivia Brooks
# @Collaborator: JellieJayde | Jayde Paquette
# @Email: owen.brooks77@gmail.com | obroo2@ocdsb.ca
# @Description: Parses an encrypted and unencrypted file to discern a decryption key.
#
# @Script: CutieDecrypt.py
# @Date Created: 22 Apr, 2024
# @Last Modified: 28 Apr, 2024
# @Last Modified by: Cutieguwu | Olivia Brooks
# ----------------------------------------------------------

# Fetch English language reference text and encoded text.
with open("/mnt/EnderChest/beartech/Workspace/CutieDecryptor/dataReference.txt", "r") as f:
    dataReference = f.read()

with open("/mnt/EnderChest/beartech/Workspace/CutieDecryptor/dataEncoded19.ENC", "r") as f:
    dataEncoded = f.read()

def parse(data):
    """
    Parses a string and orders the characters present within from most to least frequent.
    """

    characters = {}

    for character in data:
        character = character.upper()
        if character.isalpha():
            try:
                characters[character] = characters[character] + 1                       # Increment the character frequency.
            except KeyError:
                characters[character] = 1                                               # Make character position.

    # Get all the frequncies present to speed up the reorganisation.
    frequencies = []

    for character, frequency in characters.items():
            if frequency in frequencies:
                pass
            else:
                frequencies.append(frequency)

    keyInverse = ""
    charactersWritten = 0
    index = 0

    while charactersWritten < len(characters):                                          # Align each character from least to greatest.
        for frequency in frequencies:
            for character, characterFreq in characters.items():
                if characterFreq == frequency:
                    keyInverse = keyInverse + character                                 # Not nessecarily the most efficient alignment as the final key
                    charactersWritten = charactersWritten + 1                           # could be made straight away instead of the inversion following.

    # Invert List
    key = ""

    for index in range(0, len(keyInverse)):
        indexInvert = len(keyInverse) - 1 - index
        print(index)
        key = key + keyInverse[indexInvert]

    return key

print(parse(dataReference))
print(parse(dataEncoded))