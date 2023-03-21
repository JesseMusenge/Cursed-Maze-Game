print('''
88888888888888888888888888888888888888888888888888888888888888888888888
88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
88   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|.'j   |_..!-'|     |     88
88   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     88
88___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____88
88      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  88
88      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |  88
88      |    _!.-j'  | _!,"|_|M<>MMMMoMMM|_||!._|  `i-!.._ |      |  88
88     _!.-'|    | _."|  !;|1|MbdMMoMMMMM|l|`.| `-._|    |``-.._  |  88
88..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..88
88   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `".    |     88
88   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     88
88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  88
88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
88      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  88
88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
88888888888888888888888888888888888888888888888888888888888888888888888
''')
print("Welcome to the Cursed Maze.")
print("Your mission is to escape before the creatures of the ight find you.") 

crossroad_choice = input("You're at a crossroad. Where will you go? Left or right? \n").lower()

if crossroad_choice == "left":
  print("There is a dark shadow portal at the end of the path.")
  enter_portal = input("Type 'Enter' to enter. Type 'Go back' to try the previous choice: \n").lower() 
  if enter_portal == "enter":
    print("The portal has teleported you to a snowy location in the maze. It is cold and you may not survive the night.")
    fire_or_run = input("Type 'Fire' to stop and build a fire. Type 'Run' to keep navigating through the maze and stay warm: \n").lower()
    if fire_or_run == "run":
      print("You have turned into a straight long path with 3 doors at the end. One is red, one is blue and one is purple.")
      blue_red_purple = input("Which door will you enter? Type 'Blue' or 'Red' or 'Purple': \n").lower()
      if blue_red_purple == "blue":
        print("You have chosen the door to freedom. You run and never look back. You are free!")
      elif blue_red_purple == "red":
        print("You have walked into an endless void with no beginning and no end. You are stuck forver. \nGame Over.")             
      elif blue_red_purple == "purple":
        print("You walk onto an unstable path. The ground beneath you cracks and you fall into an endless pit. Game Over.")
      else:
        print("You chose a door that doesn't exist. \nGame Over.")
    else:
      print("A swarm of deformed crows have attacked you and feasted on your flesh. The fire was the perfect distraction. Game over")
  else:
    print("The cursed walls of the maze have started shifting. You don't remember your path and are stuck forever. Game Over.")
else:
  print("A vicious wolf jumped out of the shadows and ripped your throat out. Game over. ")
