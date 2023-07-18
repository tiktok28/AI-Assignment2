import random
import numpy as np
import math
import problem
import search

numOfRubbish = int(input("Number of rooms with rubbish?\n"))
numOfDisposalRoom = int(input("Number of disposal rooms?\n"))
rubbishRooms = []
disposalRooms = []

for i in range(numOfRubbish):
    rubbishRooms.append(problem.Trash(random.randrange(0,4),random.randrange(0,3),random.randrange(0,9),random.randrange(-4,3)))
    print("Rubbish " + str(i+1) + " at (" + str(rubbishRooms[i].xCoor) + "," + str(rubbishRooms[i].yCoor) + "), weight=" + str(rubbishRooms[i].weight) + ", volume=" + str(rubbishRooms[i].volume))

for i in range(numOfDisposalRoom):
    disposalRooms.append(problem.DisposalRoom(random.randrange(0,9,2),random.randrange(-4,4)))
    print("Disposal Room " + str(i+1) + " at (" + str(disposalRooms[i].xCoor) + "," + str(disposalRooms[i].yCoor) + ")")

rubbishBin = problem.RubbishBin()