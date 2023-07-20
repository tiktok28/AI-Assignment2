import problem as p
import math
import random

class Controller:
    legalDisposalRooms = [[0, 5], [2, 6], [4, 7], [6, 8], [8, 9], [8, 8], [8, 7], [8, 6], [8, 5], [8, 4], [7, 3],[5, 2], [3, 1], [1, 0]]
    sizeOfLegalRooms = len(legalDisposalRooms)
    def __init__(self, numOfRubbish=0, numOfDisposal=0, initialState=[], case=0):
        # Initialize instance variables
        self.numOfRubbish = numOfRubbish
        self.numOfDisposal = numOfDisposal
        self.initialState = initialState
        self.currentRubbishRooms = []
        self.currentDisposalRooms = []
        self.frontier = []
        self.explored = []
        self.depthLimit = 10
        self.rubbishBin = p.RubbishBin()
        self.generatedCoords = []

        # Generate initial state
        if case == 1:
            self.generateRubbishRooms(numOfRubbish)
            self.generateDisposalRooms(numOfDisposal)
            # rubbish room generation
        else:
            # Default Case
            self.currentRubbishRooms = [
            p.Rubbish(10, 1, [0, 5]),
            p.Rubbish(30, 3, [1, 3]),
            p.Rubbish(5, 1, [2, 3]),
            p.Rubbish(5, 1, [3, 2]),
            p.Rubbish(5, 3, [3, 5]),
            p.Rubbish(10, 2, [4, 4]),
            p.Rubbish(20, 1, [4, 6]),
            p.Rubbish(10, 2, [6, 4]),
            p.Rubbish(5, 2, [6, 7]),
            p.Rubbish(30, 1, [7, 3]),
            p.Rubbish(20, 2, [7, 6]),
            p.Rubbish(10, 3, [8, 5])]

            self.currentDisposalRooms = [
                p.DisposalRoom([2,6]),
                p.DisposalRoom([5,2]),
                p.DisposalRoom([8,9])
            ]
    def generateRubbishRooms(self, numOfRubbish):
        while len(self.currentRubbishRooms) != numOfRubbish:
            yUpLimit, yDownLimit = 0, 5
            xCoor, yCoor = self.initialState[0], self.initialState[1]
            while [xCoor, yCoor] == self.initialState:
                weight = random.randrange(0, 4)
                volume = random.randrange(1, 4)
                xCoor = random.randrange(0, 9)
                limitShift = math.floor(xCoor / 2)
                yUpLimit, yDownLimit = yUpLimit + limitShift, yDownLimit + limitShift
                yCoor = random.randrange(yUpLimit + 1, yDownLimit)

                rubbish = p.Rubbish(weight, volume, [xCoor, yCoor])

            # check if the position has been generated previously or not
            if rubbish.pos not in self.generatedCoords:
                self.generatedCoords.append(rubbish.pos)
                self.currentRubbishRooms.append(rubbish)
                print("Generated rubbish at " + rubbish.getStats())

    def generateDisposalRooms(self, numOfDisposal):
        # disposal room generation
        while len(self.currentDisposalRooms) != numOfDisposal:
            legalDisposalRoom = p.DisposalRoom(self.legalDisposalRooms[random.randrange(0, len(self.legalDisposalRooms))])
            if legalDisposalRoom.pos not in self.generatedCoords:
                self.generatedCoords.append(legalDisposalRoom.pos)
                self.currentDisposalRooms.append(legalDisposalRoom)
                print("Generated disposal room at " + str(legalDisposalRoom.pos))

    def expandAndReturnChildren(self, node, depthLimit):
        children = []
        limitShift = math.floor(node.state[0]/2)

        yUpLimit, yDownLimit = 0, 5
        xUpLimit, xDownLimit = 8, 0

        yUpLimit += limitShift
        yDownLimit += limitShift

        raisedColumnFlag = False
        normalColumnFlag = False

        if (node.state[0] >= 0 and node.state[0] <= 8):
            if (node.state[0] % 2 != 0):
                yNewRightUpLimit = yUpLimit + 1
                yNewRightDownLimit = yDownLimit + 1
                raisedColumnFlag = True
            if (node.state[0] % 2 == 0):
                yNewLeftUpLimit = yUpLimit - 1
                yNewLeftDownLimit = yDownLimit - 1
                normalColumnFlag = True

        if (node.depth < depthLimit):
            # down
            if (node.state[1] < yDownLimit):
                children.append(p.Node([node.state[0], node.state[1] + 1], node, node.depth + 1))
                # print("Going down to " + str(children[len(children)-1].state))

            if (raisedColumnFlag == True):
                # down-right
                if (node.state[0] < xUpLimit and node.state[1] + 1 <= yNewRightDownLimit):
                    children.append(p.Node([node.state[0] + 1, node.state[1] + 1], node, node.depth + 1))
                    # print("Going down-right to " + str(children[len(children) - 1].state))
                # up-right
                if (node.state[0] < xUpLimit and node.state[1] >= yNewRightUpLimit):
                    children.append(p.Node([node.state[0] + 1, node.state[1]], node, node.depth + 1))
                    # print("Going up-right to " + str(children[len(children) - 1].state))

            else:
                # down-right
                if (node.state[0] < xUpLimit and node.state[1] < yDownLimit):
                    children.append(p.Node([node.state[0] + 1, node.state[1] + 1], node, node.depth + 1))
                    # print("Going down-right to " + str(children[len(children) - 1].state))
                # up-right
                if (node.state[0] < xUpLimit):
                    children.append(p.Node([node.state[0] + 1, node.state[1]], node, node.depth + 1))
                    #  print("Going up-right to " + str(children[len(children) - 1].state))

            # up
            if (node.state[1] > yUpLimit):
                children.append(p.Node([node.state[0], node.state[1] - 1], node, node.depth + 1))
                # print("Going up to " + str(children[len(children) - 1].state))

            if (normalColumnFlag == True):
                # up-left
                if (node.state[0] > xDownLimit and node.state[1] - 1 >= yNewLeftUpLimit):
                    children.append(p.Node([node.state[0] - 1, node.state[1] - 1], node, node.depth + 1))
                    #  print("Going up-left to " + str(children[len(children) - 1].state))
                # down-left
                if (node.state[0] > xDownLimit and node.state[1] <= yNewLeftDownLimit):
                    children.append(p.Node([node.state[0] - 1, node.state[1]], node, node.depth + 1))
                    #  print("Going down-left to " + str(children[len(children) - 1].state))

            else:
                # up-left
                if (node.state[0] > xDownLimit and node.state[1] > yUpLimit):
                    children.append(p.Node([node.state[0] - 1, node.state[1] - 1], node, node.depth + 1))
                    #  print("Going up-left to " + str(children[len(children) - 1].state))
                # down-left
                if (node.state[0] > xDownLimit):
                    children.append(p.Node([node.state[0] - 1, node.state[1]], node, node.depth + 1))
                    #  print("Going down-left to " + str(children[len(children) - 1].state))
        return children

    def goalTest(self, found_goal, goalie):
            for rubbish in self.currentRubbishRooms:
                if (self.frontier[0].state == rubbish.pos):
                    if (self.rubbishBin.failTest(rubbish.weight, rubbish.volume)):
                        print("found")
                        found_goal = True
                        self.currentRubbishRooms.remove(rubbish)
                        self.frontier[0].state.append("rubbish")
                        goalie = self.frontier[0]
                        return found_goal, goalie
                    else:
                        self.explored.append(self.frontier[0])
                        self.frontier[0] = self.frontier[0].parent
                        return found_goal, goalie

            for disposalRoom in self.currentDisposalRooms:
                if (self.frontier[0].state == disposalRoom.pos):
                    if (self.rubbishBin.weight != 0):
                        print("Disposing rubbish at " + str(disposalRoom.pos))
                        self.rubbishBin.clearRubbish()
                        found_goal = True
                        self.frontier[0].state.append("dispose")
                        goalie = self.frontier[0]
                        return found_goal, goalie
                    else:
                        self.explored.append(self.frontier[0])
                        self.frontier[0] = self.frontier[0].parent
                        return found_goal, goalie

            return found_goal, goalie

    def DLS(self, currentLimit):

        solution = 0
        found_goal = False
        goalie = None
        steps = 0

        while (not found_goal):
            if (self.frontier == []):
                return None, steps

            found_goal, goalie = self.goalTest(found_goal, goalie)
            if(found_goal == None and goalie == None):
                solution, steps = None, None
                break

            if (found_goal == True):
                break

            children = self.expandAndReturnChildren(self.frontier[0], currentLimit)
            self.frontier[0].addChildren(children)
            self.explored.append(self.frontier[0])
            del self.frontier[0]

            for child in children:
                if not (child.state in [e.state for e in self.explored]):
                    self.frontier.append(child)

        if(solution == None and goalie == None):
            return solution, steps
        solution = [goalie.state]

        while goalie.parent is not None:
            solution.insert(0, goalie.parent.state)
            goalie = goalie.parent
            steps = steps + 1

        return solution, steps

    def start(self):
        currentDepth = 1
        currentState = p.Node(self.initialState,None,0)
        while (self.currentRubbishRooms != [] or self.rubbishBin.weight != 0):
            while (currentDepth <= 100):
                print("trying limit: ", currentDepth)
                self.explored = []
                self.frontier = [currentState]

                solution, steps = self.DLS(currentDepth)
                if (solution != None):
                    self.frontier[0].depth = 0
                    currentState = self.frontier[0]
                    print("Weight: ", self.rubbishBin.weight, "Volume: ", self.rubbishBin.volume)
                    break
                else:
                    currentDepth = currentDepth + 1
                if(currentDepth>10):
                    print("fail")
                    exit()
            currentDepth = 1
        print("Final solution" + str(solution))
        print("Number of steps: " + str(steps))