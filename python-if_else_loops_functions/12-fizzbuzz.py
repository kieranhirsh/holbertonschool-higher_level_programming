#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        word = 1
        if i % 3 == 0:
            print("Fizz", end="")
            word = 0
        if i % 5 == 0:
            print("Buzz", end="")
            word = 0
        if word:
            print(i, end="")
        print(" ", end="")
