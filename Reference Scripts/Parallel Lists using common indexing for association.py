#!~/.pyenv/versions/3.11.6/bin/python

# Copyright (c) 2024 Cutieguwu | Olivia Brooks
#
# -*- coding:utf-8 -*-
# @Title: Story Translator.
# @Author: Cutieguwu | Olivia Brooks
# @Email: owen.brooks77@gmail.com | obroo2@ocdsb.ca
# @Description: A simple story translator.
#
# @Script: main_school.py, forked from main.py
# @Date Created: 23 Mar, 2024
# @Last Modified: 11 April, 2024
# @Last Modified by: Cutieguwu | Olivia Brooks

with open("story.txt", "r") as f:                                     # Load story from file.
    story = f.read()

def dictionaryLoad(directory):
    with open(directory, "r") as f:
        dictionary = f.readlines()
    
    return dictionary

dictionaryEnglish = dictionaryLoad("English.txt")
dictionaryFrench = dictionaryLoad("French.txt")

def dictionaryClean(dictionary):
    for i in range(0, len(dictionary)):
        dictionary[i] = "".join(c for c in dictionary[i] if c != "\n")

    return dictionary

dictionaryEnglish = dictionaryClean(dictionaryEnglish)
dictionaryFrench = dictionaryClean(dictionaryFrench)

def translate(string):
    """
    Transates a given string.
    Returns a rough translation.
    """

    # Begin translation.
    word = ""
    wordNew = ""
    storyTranslated = ""

    for c in story:
        if c != " " and c != "." and c != "," and c != "\n":                                # Not end of word.
            word = word + c
        else:
            print("- Found special character")

            if word.lower() in dictionaryFrench:                                            # `word` is not empty or has a known translation;
                                                                                            # additionally fixes ". " and "  " events.

                for i in range(0, len(dictionaryFrench)):                                   # Parse the dictionary for the word's index.

                    if word.lower() == dictionaryFrench[i]:                                 # If the word is found, fetch its english translation.

                        wordNew = dictionaryEnglish[i].lower()                              # Fetch the index for the corresponding word in English.
                    
                        if word[0].isupper():                                               # Adjust capitalization if needed.
                            wordReconstructed = wordNew[0].upper()

                            for character in wordNew:
                                if wordNew.index(character) != 0:
                                    wordReconstructed = wordReconstructed + character
                                else:
                                    pass
                            
                            wordNew = wordReconstructed

                storyTranslated = storyTranslated + wordNew + c                             # Place the word and its proceeding special character in the story.

            else:                                   # Finish building the search string and place it in the story since it's complete and cannot be translated.
                word = word + c
                storyTranslated = storyTranslated + word
            
            word = ""
    
    return storyTranslated

print(translate(story))