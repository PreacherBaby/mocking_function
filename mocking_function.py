#!/usr/bin/env python3
import random

message = input()
stop = ''

def mocking(message):
    result = ''
    for word in message:
        for letter in word:
                word = random.choice(random.choice(letter.upper()) + random.choice(letter.lower()))
                result += word
    return result



while stop != 'n':
    print(mocking(message))
    stop = input("Wanna more? y/n ").lower()
    if stop == 'n':
        break
    else:
        message = input()
