class Node:
    def __init__(self, state=None, parent=None):
        self.state = state
        self.parent = parent

class Trash:
    def __init__(self, weight=0, volume=0, xCoor=0, yCoor=0):
        if(weight==0):
            self.weight = 5
        if(weight==1):
            self.weight = 10
        if(weight==2):
            self.weight = 20
        if(weight==3):
            self.weight = 30
        if(volume==0):
            self.volume = 1
        if(volume==1):
            self.volume = 2
        if(volume==2):
            self.volume = 3
        self.xCoor = xCoor
        self.yCoor = yCoor
class DisposalRoom:
    def __init__(self, xCoor=0, yCoor=0):
        self.xCoor = xCoor
        self.yCoor = yCoor

class RubbishBin:
    def __init__(self, weight=0, volume=0):
        self.weight = weight
        self.volume = volume