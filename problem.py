class Node:
    def __init__(self, state=None, parent=None, depth=0):
        self.state = state
        self.parent = parent
        self.depth = depth

class Rubbish:
    def __init__(self, weight=0, volume=0, pos=[]):
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
        self.pos = pos
class DisposalRoom:
    def __init__(self, pos=[]):
        self.pos = pos

class RubbishBin:
    def __init__(self, weight=0, volume=0):
        self.weight = weight
        self.volume = volume

    #def take(self, Rubbish):