import controller as c

numOfRubbish = 10 #int(input("Number of rooms with rubbish?\n"))
numOfDisposalRoom = 10 #int(input("Number of disposal rooms?\n"))
initialState = [0,0]

controller = c.Controller(numOfRubbish, numOfDisposalRoom, initialState)
print(controller.initialRubbishRooms)
print(controller.initialDisposalRooms)
print(controller.currentRubbishRooms)
print(controller.currentDisposalRooms)
print(controller.currentState)
print(controller.initialState)
# rubbishBin = p.RubbishBin()
# print(rubbishBin.weight)
# print(rubbishBin.volume)