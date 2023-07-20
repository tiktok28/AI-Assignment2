import search as s
import problem as p
import math
import random
class Controller:
    legalDisposalRooms = [[0,5],[2,6],[4,7],[6,8],[8,9],[8,8],[8,7],[8,6],[8,5],[8,4],[7,3],[5,2],[3,1],[1,0]]
    currentRubbishRooms = []
    currentDisposalRooms = []
    frontier = []
    explored = []
    depthLimit = 10
    rubbishBin = p.RubbishBin()
    generatedCoords = []
    def __init__(self, numOfRubbish=0, numOfDisposal=0, initialState=[], case=0):
        self.numOfRubbish = numOfRubbish
        self.numOfDisposal = numOfDisposal
        self.initialState = initialState
        numOfLegalLeft = len(self.legalDisposalRooms)
        if (case == 1):
            # rubbish room generation
            while len(self.currentRubbishRooms) != numOfRubbish:
                yUpLimit, yDownLimit = 0, 5
                xCoor, yCoor = initialState[0], initialState[1]

                # ensure that no room is on starting position
                while [xCoor, yCoor] == initialState:
                    weight = random.randrange(0, 4)
                    volume = random.randrange(1, 4)
                    xCoor = random.randrange(0, 9)
                    limitShift = math.floor(xCoor / 2)
                    yUpLimit, yDownLimit = yUpLimit + limitShift, yDownLimit + limitShift
                    yCoor = random.randrange(yUpLimit + 1, yDownLimit)

                    rubbish = p.Rubbish(weight, volume, [xCoor, yCoor])

                # check if the coordinate has been used or not
                if rubbish.pos not in self.generatedCoords:
                    self.generatedCoords.append(rubbish.pos)
                    self.currentRubbishRooms.append(rubbish)
                    print("Generated rubbish at " + rubbish.getStats())

            # disposal room generation
            while len(self.currentDisposalRooms) != numOfDisposal:
                # yUpLimit, yDownLimit = 0, 5
                # xCoor, yCoor = initialState[0], initialState[1]
                #
                # # ensure that no room is on starting position
                # while [xCoor, yCoor] == initialState:
                #     xCoor = random.randrange(0, 9)
                #     limitShift = math.floor(xCoor / 2)
                #     yUpLimit, yDownLimit = yUpLimit + limitShift, yDownLimit + limitShift
                #     yCoor = random.randrange(yUpLimit + 1, yDownLimit)
                #
                #     disposalRoom = p.DisposalRoom([xCoor, yCoor])
                # check if the coordinate has been used or not
                legalDisposalRoom = p.DisposalRoom(self.legalDisposalRooms[random.randrange(0,len(self.legalDisposalRooms))])
                if legalDisposalRoom.pos not in self.generatedCoords:
                    self.generatedCoords.append(legalDisposalRoom.pos)
                    self.currentDisposalRooms.append(legalDisposalRoom)
                    print("Generated disposal room at " + str(legalDisposalRoom.pos))

        else:
            rubbish1 = p.Rubbish(10, 1, [0, 5])
            rubbish2 = p.Rubbish(30, 3, [1, 3])
            rubbish3 = p.Rubbish(5, 1, [2, 3])
            rubbish4 = p.Rubbish(5, 1, [3, 2])
            rubbish5 = p.Rubbish(5, 3, [3, 5])
            rubbish6 = p.Rubbish(10, 2, [4, 4])
            rubbish7 = p.Rubbish(20, 1, [4, 6])
            rubbish8 = p.Rubbish(10, 2, [6, 4])
            rubbish9 = p.Rubbish(5, 2, [6, 7])
            rubbish10 = p.Rubbish(30, 1, [7, 3])
            rubbish11 = p.Rubbish(20, 2, [7, 6])
            rubbish12 = p.Rubbish(10, 3, [8, 5])
      
            self.currentRubbishRooms = [rubbish1, rubbish2, rubbish3, rubbish4, rubbish5, rubbish6, rubbish7, rubbish8, rubbish9, rubbish10, rubbish11,rubbish12]
    
            disposal1 = p.DisposalRoom([2,6])
            disposal2 = p.DisposalRoom([5,2])
            disposal3 = p.DisposalRoom([8,9])
            self.currentDisposalRooms = [disposal1,disposal2,disposal3]

    def expandAndReturnChildren(self, node, depthLimit):
        children = []
        limitShift = math.floor(node.state[0] / 2)

        yUpLimit, yDownLimit = 0, 5
        xUpLimit, xDownLimit = 8, 0

        yUpLimit += limitShift
        yDownLimit += limitShift

        rightFlag = False
        leftFlag = False

        if (node.state[0] >= 0 and node.state[0] <= 8):
            if (node.state[0] % 2 != 0):
                yNewRightUpLimit = yUpLimit + 1
                yNewRightDownLimit = yDownLimit + 1
                rightFlag = True
            if (node.state[0] % 2 == 0):
                yNewLeftUpLimit = yUpLimit - 1
                yNewLeftDownLimit = yDownLimit - 1
                leftFlag = True

                # print("Y new up limit: ",yNewUpLimit)
                # print("Y new down limit: ",yNewDownLimit)

        if (node.depth < depthLimit):
            # down
            if (node.state[1] < yDownLimit):
                children.append(p.Node([node.state[0], node.state[1] + 1], node, node.depth + 1))
                # print("Going down to " + str(children[len(children)-1].state))

            if (rightFlag == True):
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

            if (leftFlag == True):
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
                        self.frontier[0].state.append("take")
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
                        # self.frontier[0] = self.frontier[0].parent
                        return found_goal, goalie
                    else:
                        self.explored.append(self.frontier[0])
                        self.frontier[0] = self.frontier[0].parent
                        return found_goal, goalie

            return found_goal, goalie

    def DLS(self, currentLimit):
        # up = y+1
        # up-right = x+1
        # up-left = x-1, y+1
        # down = y-1
        # down-right = x+1, y-1
        # down-left = x-1

        solution = 0
        found_goal = False
        goalie = None
        steps = 0

        while (not found_goal):
            # print("iterating")

            if (self.frontier == []):
                # print("breaking")
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
                    # and not (child.state in [f.state for f in self.frontier])

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
            # print("iterating")
            while (currentDepth <= 10):
                print("trying limit: ", currentDepth)
                self.explored = []
                # self.frontier = [v.Node(self.currentState,None,0)]
                self.frontier = [currentState]

                # print("current depth: ", currentDepth)

                solution, steps = self.DLS(currentDepth)
                if (solution != None):
                    # self.currentState = self.frontier[0].state
                    # self.frontier[0].parent = None
                    self.frontier[0].depth = 0
                    currentState = self.frontier[0]
                    print("Weight: ", self.rubbishBin.weight, "Volume: ", self.rubbishBin.volume)
                    break
                else:
                    currentDepth = currentDepth + 1
            currentDepth = 1
        print("Final solution" + str(solution))
        print("Number of steps: " + str(steps))