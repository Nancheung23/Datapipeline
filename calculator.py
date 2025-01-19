def calculate(x, y, fthreshold):
    sums = x + y
    subs = x - y
    multis = x * y
    print(f"{x} + {y} = {sums} {classifier(fthreshold, sums)}")
    print(f"{x} - {y} = {subs} {classifier(fthreshold, subs)}")
    print(f"{x} x {y} = {multis} {classifier(fthreshold, multis)}")
    if y == 0:
        print(f"Divisor 0 is illegal!")
    else:
        div = x / y
        print(f"{x} / {y} = {div} {classifier(fthreshold, div)}")

def classifier(fthreshold, fresult):
    if fthreshold > fresult:
        smallList.append(fresult)
        return f"is lower than {fthreshold}"
    elif fthreshold == fresult:
        return f"equals {fthreshold}"
    else:
        bigList.append(fresult)
        return f"is higher than {fthreshold}"

smallList = []
bigList = []

while True:
    print("Start script:\n")
    x = input(f"Input first parameter:")
    if x == "exit":
        exit()
    y = input(f"Input second parameter:")
    if y == "exit":
        exit()
    threshhold = input(f"Input threshold:")
    calculate(float(x), float(y), float(threshhold))
    print("Small numbers:")
    for num in smallList:
        print(f"{num}")
    print("Big numbers:")
    for num in bigList:
        print(f"{num}")
    exit()
