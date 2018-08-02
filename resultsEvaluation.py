# points given to each house as per position
posPoints = {
    1: 5,
    2: 3,
    3: 2,
    4: 1
}

# index of each house in the final results array
houses = {
    "red": 0,
    "blue": 1,
    "green": 2,
    "yellow": 3
}

# compiling positions of each event, and adding scores to houses
def addResults(hr, hf):
    for i in range(0, 4):
        hf[houses[hr[i]]] += posPoints[i+1]
        pass
    return hf # returns a list of additional points to be added to each
