import search as s
import problem as p
import math
import random
class Controller:
    initialRubbishRooms = []
    initialDisposalRooms = []
    currentRubbishRooms = []
    currentDisposalRooms = []
    initialState = []
    currentState = []
    frontier = []
    explored = []
    depthLimit = 10
    rubbishBin = p.RubbishBin()
    def __init__(self, numOfRubbish, numOfDisposal, initialState=[]):
        for i in range(numOfRubbish):
            self.initialRubbishRooms.append(p.Trash(random.randrange(0, 4), random.randrange(0, 3), [random.randrange(0, 9), random.randrange(-4, 3)]))
            print("Rubbish " + str(i + 1) + " at " + str(self.initialRubbishRooms[i].pos) + ", weight=" + str(self.initialRubbishRooms[i].weight) + ", volume=" + str(self.initialRubbishRooms[i].volume))

        for i in range(numOfDisposal):
            self.initialDisposalRooms.append(p.DisposalRoom([random.randrange(0, 9, 2), random.randrange(-4, 4)]))
            print("Disposal Room " + str(i + 1) + " at " + str(self.initialDisposalRooms[i].pos))

        self.currentRubbishRooms = self.initialRubbishRooms
        self.currentDisposalRooms = self.initialDisposalRooms
        self.initialState = initialState
        self.currentState = initialState

    def restart(self):
        self.currentRubbishRooms = self.initialRubbishRooms
        self.currentDisposalRooms = self.initialDisposalRooms
        self.currentState = self.initialState

    def expandAndReturnChildren(self, node, depthLimit):
        children = []
        limitShift = math.floor(node.state[0] / 2)

        yUpLimit, yDownLimit = 5, 0
        xUpLimit, xDownLimit = 8, 0

        yUpLimit -= limitShift
        yDownLimit -= limitShift
        yNewRightUpLimit = yUpLimit
        yNewLeftUpLimit = yUpLimit
        yNewRightDownLimit = yDownLimit
        yNewLeftDownLimit = yDownLimit

        rightFlag = False
        leftFlag = False

        if (node.state[0] > 0 and node.state[0] < 8):
            if (node.state[0] % 2 != 0):
                yNewRightUpLimit = yUpLimit - 1
                yNewRightDownLimit = yDownLimit - 1
                rightFlag = True
            if (node.state[0] % 2 == 0):
                yNewLeftUpLimit = yUpLimit + 1
                yNewLeftDownLimit = yDownLimit + 1
                leftFlag = True

                # print("Y new up limit: ",yNewUpLimit)
                # print("Y new down limit: ",yNewDownLimit)

        if (node.depth < depthLimit):

            # down
            if (node.state[1] > yDownLimit):
                children.append(p.Node([node.state[0], node.state[1] - 1], node, node.depth + 1))

            if (rightFlag == True):
                # up-right
                if (node.state[0] < xUpLimit and node.state[1] <= yNewRightUpLimit):
                    children.append(p.Node([node.state[0] + 1, node.state[1]], node, node.depth + 1))
                # down-right
                if (node.state[0] < xUpLimit and node.state[1] >= yNewRightDownLimit):
                    children.append(p.Node([node.state[0] + 1, node.state[1] - 1], node, node.depth + 1))

            else:
                # up-right
                if (node.state[0] < xUpLimit):
                    children.append(p.Node([node.state[0] + 1, node.state[1]], node, node.depth + 1))
                # down-right
                if (node.state[0] < xUpLimit and node.state[1] > yDownLimit):
                    children.append(p.Node([node.state[0] + 1, node.state[1] - 1], node, node.depth + 1))

            # up
            if (node.state[1] < yUpLimit):
                children.append(p.Node([node.state[0], node.state[1] + 1], node, node.depth + 1))

            if (leftFlag == True):
                # up-left
                if (node.state[0] > xDownLimit and node.state[1] <= yNewLeftUpLimit):
                    children.append(p.Node([node.state[0] - 1, node.state[1] + 1], node, node.depth + 1))
                # down-left
                if (node.state[0] > xDownLimit and node.state[1] >= yNewLeftDownLimit):
                    children.append(p.Node([node.state[0] - 1, node.state[1]], node, node.depth + 1))
            else:
                # up-left
                if (node.state[0] > xDownLimit and node.state[1] < yUpLimit):
                    children.append(p.Node([node.state[0] - 1, node.state[1] + 1], node, node.depth + 1))
                # down-left
                if (node.state[0] > xDownLimit):
                    children.append(p.Node([node.state[0] - 1, node.state[1]], node, node.depth + 1))

        else:
            None

        return children

    def goalTest(self, found_goal, goalie):
        for rubbish in self.currentRubbishRooms:
            if (self.frontier[0].state == rubbish.trashPos):
                if (
                        self.rubbishBin.weight < 40 and self.rubbishBin.volume < 5):
                    if (self.rubbishBin.append(rubbish)):
                        print("found")
                        found_goal = True
                        self.trashList.remove(trash)
                        self.frontier[0].state.append("take")
                        goalie = self.frontier[0]
                        return found_goal, goalie
                    else:
                        self.explored.append(self.frontier[0])
                        self.frontier[0] = self.frontier[0].parent
                        return found_goal, goalie

        for disposalRoom in self.currentDisposalRooms:
            if (self.frontier[0].state == disposalRoom.pos):
                if (self.rubbishBin.capacity != 0):
                    print("disposing")
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

        found_goal = False
        goalie = None
        steps = 0

        while (not found_goal):
            # print("iterating")

            if (self.frontier == []):
                # print("breaking")
                return None, steps

            found_goal, goalie = self.goalTest(found_goal, goalie)
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

        solution = [goalie.state]

        while goalie.parent is not None:
            solution.insert(0, goalie.parent.state)
            goalie = goalie.parent
            steps = steps + 1

        return solution, steps

    def start(self):

        currentDepth = 1
        currentState = p.Node(self.initialState, None, 0)

        while (self.currentRubbishRooms != [] or self.rubbishBin.weight != 0):
            # print("iterating")
            while (currentDepth <= self.depthLimit):
                print("trying limit: ", currentDepth)
                self.explored = []
                # self.frontier = [v.Node(self.currentState,None,0)]
                self.frontier = [currentState]

                # print("current depth: ", currentDepth)
                solution, steps = self.DLS(currentDepth)
                if (solution != None):
                    # self.currentState = self.frontier[0].state
                    # self.frontier[0].parent = None
                    self.frontier[0].layer = 0
                    currentState = self.frontier[0]

                    print("Weight: ", self.rubbishBin.weight, "Volume: ", self.rubbishBin.volume)
                    break
                else:
                    currentDepth = currentDepth + 1

            currentDepth = 1

        return solution, steps