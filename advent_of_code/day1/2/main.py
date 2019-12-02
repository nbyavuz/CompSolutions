FILE_NAME = 'fuels.txt'


def calculateRecursively(fuel: int) -> int:
    newFuel = int(fuel / 3) - 2
    if newFuel <= 0:
        return 0
    return newFuel + calculateRecursively(newFuel)


def calculateFuel() -> int:
    maxFuel = 0
    with open(FILE_NAME, "r") as fuels:
        data = fuels.readlines()
        for line in data:
            maxFuel += calculateRecursively(int(line))
    return maxFuel


if __name__ == "__main__":
    print(calculateFuel())
