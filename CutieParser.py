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
# @Last Modified: 29 Apr, 2024
# @Last Modified by: JellieJayde | Jayde Paquette

# ----------------------------------------------------------
#
# Note: Script cannot be called "parser" as that clashes with stdlib module parser.
#
# ----------------------------------------------------------

from os import path

execDir = path.dirname(__file__)

def order(file):                                                            # This is the main function that we will use to decrypt the code

    dataLanguage = []                                                       # Variables:
    amount = []                                                             # -
    index = 0                                                               # -
    sortedString = ""                                                       # -

    with open(execDir + file, "r") as f:                                    # With the readable file:
# -------------------------------------------------------------------------------------------------------
        while True:                                                         # Will loop from this line ^ to the next one, until told otherwise
            fileChar = f.read(1).strip()                                    # Reads the first character in the file

            if fileChar.isalpha():                                          # If the character is in the alphabet (aka. a, b, c, etc...):
                if fileChar.upper() not in dataLanguage:                    # If the character is not in the (currently) empty list:
                    dataLanguage.append(fileChar.upper())                   # Put the character in the empty list
                    amount.append(1)                                        # Gives that letter an amount of 1, with the same index

                else:                                                       # If the charatcer is in the alphabet, but is already in the list, then:
                    index = 0                                               # Set the "index" variable to 0
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
                    while True:                                             # Loop from this ^ line to the next until told otherwise
                        if dataLanguage[index] == fileChar.upper():         # If the letter with the index (which is currently zero) is the same as the current character:
                            amount[index] = amount[index] + 1               # Add one to the amount of that charcater
                            break                                           # Break the loop

                        else:                                               # If the letter isn't the same as the current character:
                            index = index + 1                               # Add one to the index variable, then continue the loop
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
            if fileChar == "~":                                             # If the character is a tilde (I put a tilde at the end of the file so the program knows when the file is finished)
                index = 0                                                   # The index variable is now 0
                Finished = False                                            # Add a "Finished" variable
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
                while not Finished:                                         # If the "Finished" variable is false, it will loop from this line ^ to the next, until told other wise
                    Finished = True                                         # Set's finished to true, but wont stop the loop because it just started the first cycle
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
                    for index in range(0, len(amount) - 1):                 # Will loop from this line ^ to the next for how many items are in the "amount" list
                        temp = amount[index]                                # Make a new variable, "temp" into a number in the amount list
                        tempLetter = dataLanguage[index]                    # Do the same thing, but with "tempLetter", and instead of a number, it's a ltter

                        if temp < amount[index + 1]:                        # If the temperaroy number is less than the amount declared:
                            amount[index] = amount[index + 1]               # it will the replace the number declared in the "amount" list with the number ahead of it
                            amount[index + 1] = temp                        # Will replace the number ahead of the amount declared, with the temperaroy number

                            dataLanguage[index] = dataLanguage[index + 1]   # Replace the letter associated with the same index with the one ahead of it
                            dataLanguage[index + 1] = tempLetter            # Replace the letter ahead with the temperary letter

                            Finished = False                                # Make the "Finsihed" variable false, therefore resarting the loop
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                        if index == len(amount):                            # If the index is equal to the amount of numbers in the "amount" string
                            index = 0                                       # Reset the index
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
                for i in dataLanguage:                                      # Will loop this next line for how many letters are in the "dataLanguage" list
                    sortedString = sortedString + i                         # Add the letter it reads into a string


                return sortedString                                         # Returns the string
# ------------------------------------------------------------------------------------------------------------

# Then shows the data, proving it works
print (order("\\dataReference.txt"), "\n")
print (order("\\dataEncoded19.ENC"), "\n")