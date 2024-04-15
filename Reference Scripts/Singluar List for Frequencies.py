#!~/.pyenv/versions/3.11.6/bin/python

# Copyright (c) 2024 Cutieguwu | Olivia Brooks
#
# -*- coding:utf-8 -*-
# @Title: Coin Flipper.
# @Author: Cutieguwu | Olivia Brooks
# @Email: owen.brooks77@gmail.com | obroo2@ocdsb.ca
# @Description: Runs a given number of trials of 5 coin flips and reports the total groupings of tails.
#
# @Script: 8.py
# @Date Created: 06 March, 2024
# @Last Modified: 07 March, 2024
# @Last Modified by: Cutieguwu | Olivia Brooks

from random import randint

trials = ""
while trials.isnumeric() == False:                      # Ensure that user enters a number value to iterate.
    trials = input("Enter a number of trials to run: ")

trials = int(trials)

tails = 0                                               # Tails in 5 throws
tailsGroups = [0, 0, 0, 0, 0, 0]                        # Index indicates number of tails present, value indicates frequency of the group.


def make_plural(x=int(), msg=str()):
    """
    Appends "s" to msg if the value given isn't 1.
    Returns the modified msg.
    """

    if x != 1:
        msg = msg + "s"
    
    return msg

for x in range(trials):                                 # Main run loop, runs for number of trials given.
    msgTrial = ""
    tails = 0

    for i in range(5):                                  # Run a trial; flip a "coin" five times.
        flip = randint(1, 2)
        msg = ", "

        if i == 0:
            msg = ""
        
        if flip == 1:
            msg = msg + "Heads"
        else:
            msg = msg + "Tails"
            tails = tails + 1                           # Record the number of tails for the trial.

        msgTrial = msgTrial + msg

    print(f"{msgTrial} You got {tails} tails.", end="")        # Print all results of the trial at once.
    tailsGroups[tails] = tailsGroups[tails] + 1         # Increment the appropriate tails.

for i in range(len(tailsGroups)):                                                                                   # Produce results with proper grammar.
    print(make_plural(tailsGroups[i], make_plural(i, f"Rolled {i} tail") + f" in {tailsGroups[i]} trial") + ".")    # Produce and print the final report, making "tail" plural if needed.