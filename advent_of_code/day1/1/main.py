FILE_NAME = 'fuels.txt'


def calculateFuel() -> int:
    maxFuel = 0
    with open(FILE_NAME, "r") as fuels:
        data = fuels.readlines()
        for line in data:
            maxFuel += int(int(line) / 3) - 2
    return maxFuel


if __name__ == "__main__":
    print(calculateFuel())
