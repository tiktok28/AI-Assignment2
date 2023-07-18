import search as s
import problem as p
import random
class Controller:
    initialRubbishRooms=[]
    initialDisposalRooms=[]
    currentRubbishRooms=[]
    currentDisposalRooms=[]
    initialState=[]
    currentState=[]
    def __init__(self, numOfRubbish, numOfDisposal, initialState=[]):
        for i in range(numOfRubbish):
            self.initialRubbishRooms.append(p.Trash(random.randrange(0, 4), random.randrange(0, 3), random.randrange(0, 9), random.randrange(-4, 3)))
            print("Rubbish " + str(i + 1) + " at (" + str(self.initialRubbishRooms[i].xCoor) + "," + str(self.initialRubbishRooms[i].yCoor) + "), weight=" + str(self.initialRubbishRooms[i].weight) + ", volume=" + str(self.initialRubbishRooms[i].volume))

        for i in range(numOfDisposal):
            self.initialDisposalRooms.append(p.DisposalRoom(random.randrange(0, 9, 2), random.randrange(-4, 4)))
            print("Disposal Room " + str(i + 1) + " at (" + str(self.initialDisposalRooms[i].xCoor) + "," + str(self.initialDisposalRooms[i].yCoor) + ")")

        self.currentRubbishRooms = self.initialRubbishRooms
        self.currentDisposalRooms = self.initialDisposalRooms
        self.initialState = initialState
        self.currentState = initialState

    def restart(self):
        self.currentRubbishRooms = self.initialRubbishRooms
        self.currentDisposalRooms = self.initialDisposalRooms
        self.current_state = self.initial_state