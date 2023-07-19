import controller as c

numOfRubbish = 3 #int(input("Number of rooms with rubbish?\n"))
numOfDisposalRoom = 3 #int(input("Number of disposal rooms?\n"))
initialState = [0,0]

controller = c.Controller(numOfRubbish, numOfDisposalRoom, initialState)
# for room in controller.initialDisposalRooms:
#     print(room.pos)
# for room in controller.initialRubbishRooms:
#     print(room.pos)
controller.start()