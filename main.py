from graph import Graph_Imp

"""
Coding Challenge 1: Typing game.

Create a function that takes in two arrays: the array of user-typed words, and the array of correctly-typed words and outputs an array containing 1s (correctly-typed words) and -1s (incorrectly-typed words).

Inputs:
User-typed Array: ["cat", "blue", "skt", "umbrells", "paddy"]
Correct Array: ["cat", "blue", "sky", "umbrella", "paddy"]

Output: [1, 1, -1, -1, 1]
Examples
correctStream(
["it", "is", "find"],
["it", "is", "fine"]
) ➞ [1, 1, -1]

correctStream(
["april", "showrs", "bring", "may", "flowers"],
["april", "showers", "bring", "may", "flowers"]
) ➞ [1, -1, 1, 1, 1]
Notes
The input array lengths will always be the same.

"""
def correctStream(user_words, correct_words):
  word_check = []

  user_words = list(map(lambda x: x.lower(), user_words))
  correct_words = list(map(lambda x: x.lower(), correct_words))

  i = 0
  for word in user_words:
#    print(word)
#    print(correct_words[i])
    if word in correct_words:
      word_check.append(1)
    else:
      word_check.append(-1)
    i += 1

  return word_check

"""
Coding Challenge 2: BFS Chess
You will be given the location of a knight and an end location. The knight can move in a "L" shape. "L" shape movement means that the knight can change it's x coordinate by 2 and it's y coordinate by 1 or it can change it's y coordinate by 2 and it's x coordinate by 1 (you can add and subtract from the x/y).

For example, if the knight is at the position (0, 0), it can move to:

(1,2), (1,-2), (2,1), (2,-1), (-1,2), (-1,-2), (-2,1), (-2, -1)
Your job is to return the least amount of steps needed to go from the position K (knight's start position) to E (end). You will only be given the knight starter coordinates (x1, y1) and the end coordinates (x2, y2).

Constraints: 1 <= x1,y1,x2,y2 <= 8

Examples
knightBFS(1, 1, 8, 8) ➞ 6
knightBFS(1, 1, 3, 2) ➞ 1
knightBFS(8, 8, 3, 3) ➞ 4

Notes
This is a simplified version of this problem.
This travel will always be possible.
The chessboard is 8x8. 

"""
def knightBFS(knightX, knightY, endX, endY):

  knightX -= 1
  knightY -= 1
  endX -= 1
  endY -= 1

  chess_board = Graph_Imp()
  
  for j in range(0, 8):
    for i in range(0, 8):
      movement = []
      if i+2 < 8 and j+1 < 8:
        movement.append("%d %d" % (i+2, j+1))
      if i+1 < 8 and j+2 < 8:
        movement.append("%d %d" % (i+1, j+2))
      if i-2 > 0 and j+1 < 8:
        movement.append("%d %d" % (i-2, j+1))
      if i-1 > 0 and j+2 < 8:
        movement.append("%d %d" % (i-1, j+2))
      if i+2 < 8 and j-1 > 0:
        movement.append("%d %d" % (i+2, j-1))
      if i+1 < 8 and j-2 > 0:
        movement.append("%d %d" % (i+1, j-2))
      if i-2 > 0 and j-1 > 0:
        movement.append("%d %d" % (i-2, j-1))
      if i-1 > 0 and j-2 > 0:
        movement.append("%d %d" % (i-1, j-2))

      current_node = "%d %d" % (i, j)
      chess_board.addNode(current_node, movement)

  # chess_board.listAllNodesAndConnections()
  val = chess_board.bfsShortestPath("%d %d" % (knightX, knightY), "%d %d" % (endX, endY))
  print(len(val) - 1)

# knightBFS(1, 1, 8, 8)
# knightBFS(1, 1, 3, 2)
# knightBFS(8, 8, 3, 3)

# print(correctStream(["it", "is", "find"],
# ["it", "is", "fine"] ))

# print(correctStream(["april", "showrs", "bring", "may", "flowers"],
# ["april", "showers", "bring", "may", "flowers"]))

"""
Logical Interview Question: Torch and Bridge

Puzzle: There are 4 persons (A, B, C, and D) who want to cross a bridge at night.

A takes 1 minute to cross the bridge.
B takes 2 minutes to cross the bridge.
C takes 5 minutes to cross the bridge.
D takes 8 minutes to cross the bridge.

There is only one torch with them and the bridge cannot be crossed without the torch. There cannot be more than two persons on the bridge at any time, and when two people cross the bridge together, they must move at the slower person’s pace.

Can they all cross the bridge in 15 mins? 
"""

class Torch_And_Bridge():
  def __init__(self):
    self.totalTime = 0
    self.torchLocation = "side 1"
    self.people = {
    "A": "side 1",
    "B": "side 1",
    "C": "side 1",
    "D": "side 1"}
    self.time = {
    "A": 1,
    "B": 2,
    "C": 5,
    "D": 8
    }
    # self.personA = "side1"
    # self.personB = "side1"
    # self.personC = "side1"
    # self.personD = "side1"

  def reset(self):
    self.totalTime = 0
    self.torchLocation = "side 1"
    self.people = {
    "A": "side 1",
    "B": "side 1",
    "C": "side 1",
    "D": "side 1"}
    self.time = {
    "A": 1,
    "B": 2,
    "C": 5,
    "D": 8
    }
    # self.personA = "side1"
    # self.personB = "side1"
    # self.personC = "side1"
    # self.personD = "side1"

  def cross(self):

    try:

      person1 = input("Enter 1st person to cross: ")
      person2 = input("Enter 2nd person to cross (enter None if you only want one person to cross): ")

      
      if (self.torchLocation != self.people[person1] and person2 == "None"):
        print("Cannot cross, torch on %s while person1 is on %s" % (self.torchLocation, self.people[person1]))
        return False
      if person2 != "None":
        if self.torchLocation != self.people[person1] and self.torchLocation != self.people[person2]:
          print("Cannot cross, torch on %s while person1 is on %s and person2 is on %s" % (self.torchLocation, self.people[person1], self.people[person2]))
          return False
        if self.people[person1] != self.people[person2]:
          print("Cannot cross, person1 is on %s while person2 is on %s (torch is on %s)" % (self.people[person1], self.people[person2], self.torchLocation))
          return False

      ############################################

      if self.people[person1] == "side 1":
        self.people[person1] = "side 2"
      else:
        self.people[person1] = "side 1"
      
      if person2 != "None":
        if self.people[person2] == "side 1":
          self.people[person2] = "side 2"
        else:
          self.people[person2] = "side 1"

      if self.torchLocation == "side 1":
        self.torchLocation = "side 2"
      else:
        self.torchLocation = "side 1"

      if person2 != "None":
        if self.time[person1] > self.time[person2]:
          self.totalTime += self.time[person1]
        else:
          self.totalTime += self.time[person2]
      else:
        self.totalTime += self.time[person1]

      if self.totalTime > 15:
        print("Overtime, resetting...")
        self.reset()
        return False

      return True

    except:
      print("Unexpected error, returning")
      return False

  def win(self):
    if self.people["A"] == "side 2" and self.people["B"] == "side 2" and self.people["C"] == "side 2" and self.people["D"] == "side 2":
      return True
    return False

  def print(self):
    print("Person A is on %s\nPerson B is on %s\nPerson C is on %s\nPerson D is on %s\nThe torch is on %s\n%d minutes have passed" % (self.people["A"], self.people["B"], self.people["C"], self.people["D"], self.torchLocation, self.totalTime))

  def simulation(self):
    print("Welcome to the torch and the bridge simulation\nTry to get person A, B, C, and D to side 2 of the bridge\nIn order for people to cross the bridge, they need a torch, and there is only one of them\nOnly 2 people can cross the bridge at a time\nIf the torch is on side 2, people on side 1 cannot use it, and vice versa\nPerson A takes 1 min to cross\nPerson B takes 2 min to cross\nPerson C takes 5 min to cross\nPerson D takes 8 min to cross\nTry to cross the bridge in 15 minutes or less!")

    user_input = ""

    self.print()

    while(user_input != "exit" and self.win() != True ):

      user_input = input("Enter a command (type 'help' for a list of commands): ")
      user_input = user_input.lower()

      if user_input == "print":
        self.print()
      elif user_input == "cross":
        self.cross()
      elif user_input == "help":
        print("exit - exit this loop\nprint - print out the current locations of people and torches\ncross - choose one or two people to cross the bridge\nremind - print the problem statement again")
      elif user_input == "remind":
        print("Welcome to the torch and the bridge simulation\nTry to get person A, B, C, and D to side 2 of the bridge\nIn order for people to cross the bridge, they need a torch, and there is only one of them\nOnly 2 people can cross the bridge at a time\nIf the torch is on side 2, people on side 1 cannot use it, and vice versa\nPerson A takes 1 min to cross\nPerson B takes 2 min to cross\nPerson C takes 5 min to cross\nPerson D takes 8 min to cross\nTry to cross the bridge in 15 minutes or less!")
      else:
        print("Unknown command, continuing")

    if self.win() == True:
      print("Congratulations, you solved the riddle!")


sim = Torch_And_Bridge()

sim.simulation()

