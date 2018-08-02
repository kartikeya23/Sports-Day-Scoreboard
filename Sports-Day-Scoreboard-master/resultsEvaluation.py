import sqlite3

# points given to each house as per position
posPoints = {
    1: 5,
    2: 3,
    3: 2,
    4: 1
}

# index of each house in the final results array
houses = {
    "Red": 0,
    "Blue": 1,
    "Green": 2,
    "Yellow": 3
}

# compiling positions of each event, and adding scores to houses
def addResults(hr, hf):
    for i in range(0, 4):
        hf[houses[hr[i]]] += posPoints[i+1]
        pass
    return hf # returns a list of additional points to be added to each


def update(oppo):
    real = sqlite3.connect('Samyak.db')
    real.execute('''UPDATE house SET Red = {x}, Blue = {y}, Green = {z}, Yellow = {a}
     WHERE True = "True" '''.format(x=oppo[0],y=oppo[1],z=oppo[2],a=oppo[3]))
    real.commit()
