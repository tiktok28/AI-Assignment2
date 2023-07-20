import controller as c

initialState = [0,0]
try:
    case = int(input("Default case or generated? (0 or 1)\n"))
    if(case != 0 and case != 1):
        print("Non-acceptable values sent, executing default case...")
        case = 0
except:
    print("Non-acceptable values sent, executing default case...")
    case = 0

if case == 1:
    try:
        numOfRubbish = int(input("Number of rooms with rubbish? (Max 12)\n"))
        numOfDisposalRoom = int(input("Number of disposal rooms? (Max 14)\n"))
        if(numOfDisposalRoom > c.Controller.sizeOfLegalRooms or numOfDisposalRoom <= 0 or numOfRubbish > 12 or numOfRubbish <= 0):
            print("Non-acceptable values sent, executing default case...")
            case = 0
    except:
        print("Non-acceptable value sent, executing default case...")
        case = 0
    controller = c.Controller(numOfRubbish, numOfDisposalRoom, initialState, case)
else:
    controller = c.Controller(0, 0, initialState, case)

controller.start()