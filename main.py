import controller as c

initialState = [0,0]
try:
    case = int(input("Default case or generated? (0 or 1)"))
    if(case != 0 and case != 1):
        print("Non-acceptable value sent, executing default case...")
        case = 0
except:
    print("Non-acceptable value sent, executing default case...")
    case = 0

if case == 1:
    numOfRubbish = int(input("Number of rooms with rubbish?\n"))
    numOfDisposalRoom = int(input("Number of disposal rooms?\n"))
    controller = c.Controller(numOfRubbish, numOfDisposalRoom, initialState, case)
else:
    controller = c.Controller(0, 0, initialState, case)

controller.start()