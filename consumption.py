import math
import random

def consumptionCal():
    consumption = input(f"Consumption (units)? ")
    unitPrice = input(f"Unit price (currency units)? ")
    if (float(consumption) < 500):
        unitPrice = float(unitPrice) + 4.32
    else:
        unitPrice = float(unitPrice) + 7.75
    print(f"Total price is {float(consumption) * unitPrice * 1.17} currency units.")

def pseudo(min, max):
    pseudoArr = list()
    index = 0
    while (index < 50):
        pseudoArr.append(random.random() + float(random.randrange(min, max)))
        index += 1
    mean, median, small = 0.0, 0.0, 0.0
    for x in pseudoArr:
        print(x)
        mean += x
    mean /= 50
    pseudoArr.sort()
    median = (pseudoArr[24] + pseudoArr[25]) / 2
    small = pseudoArr[0]
    print(f"Mean: {mean}\n")
    print(f"Median: {median}\n")
    print(f"Small: {small}\n")

def ciphertext():
    cipherList = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789".rsplit()
    plaintext = input(f"Input plaintext: ")
    plaintext.upper()
    indent = input(f"Input an integer for encoding: ")
    indent = int(indent)

# consumptionCal()
pseudo(4,7)