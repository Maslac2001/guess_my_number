# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 11:59:41 2020

@author: Aleksa
"""


import random

from guess_my_number import MIN, MAX, GuessMachine

if __name__ == "__main__":
    min = MIN
    max = MAX
    guess_machine = GuessMachine()
    while True:
        attempt = random.randint(min,max)
        result = guess_machine.guess(attempt)
        print("tried %d : %s" % (attempt,result))
        if result == "found":
            print("Finished in %d attempts." % guess_machine.number_of_attempt)
            break
        elif result == "too low":
            min = attempt + 1
        else:
            max = attempt - 1
        
