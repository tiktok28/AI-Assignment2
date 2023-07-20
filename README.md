# AI-Assignment2
This is a program that allow the algorithm (Rony) to find and grab the rubbish with a limited weight of 40kg to carry and limited size of 5m^3 to carry, and then dispose them into the disposal room.
The base rules are stated as Rony can only execute actions below:
1. Move
2. Move from node to another node without teleporting by skipping node.
3. Pick up rubbish.
4. Dispose of rubbish.
The algorithm will be terminated after all of the rubbish has been picked up and disposed.
The whole program is coded with Iterative Depth First Search (IDDFS) to accomplish the objecitves and not violate the rules.

##Usage
Before executing the program, user have to download the entire folder.

##Files
This project contains 3 python files:
1. main.py
2. controller.py
3. problem.py

##Execution
After downloading the whole document, executing the main file will 
User will have to input the default case or the case they wanted to.
For customized cases, user will required to input the number of rubbish and number of disposal room. The maximum number of the rubbish is 12 and maximum number of disposal room 14.
If the user provides invalid inputs (such as -1 or 0 for both rubbish and disposal room, non-integer inputs), the program will execute in default way.

##Requirement
Latest version of Python

##Member 
Naveen Ramarao
Lim Ee Hui
Navinder Singh
