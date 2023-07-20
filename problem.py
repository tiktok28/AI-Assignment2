class Node:
    def __init__(self, state=None, parent=None, depth=0):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.children = []

    def addChildren(self, children):
        self.children.extend(children)

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
        self.weight = weight
        self.volume = volume
        self.pos = pos
    def getStats(self):
        return (str(self.pos)+"Weight:"+str(self.weight)+"kg"+",Volume:"+str(self.volume)+"m3")
class DisposalRoom:
    def __init__(self, pos=[]):
        self.pos = pos

class RubbishBin:
    storage = []
    def __init__(self, weight=0, volume=0):
        self.weight = weight
        self.volume = volume

    def takeRubbish(self, rubbish):
        self.storage.append(rubbish)
        self.weight += rubbish.weight
        self.volume += rubbish.volume

    def clearRubbish(self):
        self.storage = []
        self.weight = 0
        self.volume = 0

    def failTest(self, weight, volume):
        if (self.weight+weight > 40 or self.volume+volume > 5):
            return False
        else:
            self.weight = self.weight + weight
            self.volume = self.volume + volume
            return True