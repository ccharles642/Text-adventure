print ("A girl named Garnet, is at the arcade and is going to play Mortal Kombat.")

path = str(input("Do you want to go against Sub- Zero? [Yes/No]: "))
a = "Yes"
b = "No"
#Yes Sub-Zero
if path ==a:
    print("You are now fighting Sub-Zero. Ready. Fight")
    firstsubmove = str(input("Sub-Zero is going to freeze you, What is your next move? Dodge Right, Dodge Left"))
    a = "Dodge Right"
    b = "Dodge Left"

#Sub-Move first move "a"
    if firstsubmove ==a:
        print("Sub-Zero misses, you hit him and his health decreases by half")
        print("You throw a smoke bomb and go in with your sword and swing, Sub - Zero gets cut badly and now is bleeding. His health is going down.")
        submove = str(input("You go in for an attack. What is your move? Pull out your sword, Punch him"))
        a = "Attack again with sword"
        b = "Punch him"

#Sub move a
        if submove ==a:
            print("Your last sword swing finishes him and cut him in half. The announcer says Fatality and YOU WIN")

#Sub move b
    if submove ==b:
        print("You try to punch him but he catches your fist and freezes your whole body. When he freezes you, he comes in with one last blow and shatters your whole body and YOU LOSE")
#Sub-Zero first move "b"
    if firstsubmove ==b:
        print("Sub-Zero moves and you still get hit. So your health decreases by half.")
        nextsubmove = str(input("You go in for an attack. What is your move? Pull out your sword, Punch him"))
        a = "Pull out your sword"
        b = "Punch him"

# Pull out the sword on Sub-Zero
        if nextsubmove ==a:
            print("He is able to catch the sword, freeze it and shatter the sword and your health is critical. To finish you off, he comes in with the biggest upper cut of all time.")
            print("The uppercut takes your head off and the announcer says Fatality")

#Punch Sub-Zero
        if nextsubmove ==b:
            print(" You punch him so hard, that create a hole in his chest and grab his heart and pull it out")
            print("The announcer says Fatality and YOU WIN")

#No Sub-Zero
if path ==b:
    print("Choose a new Player")
    newplayer = str(input("Scorpion")
    a = "Scorpion"

# If Scorpion is chosen and his first move
    if newplayer ==a:
        print("You are now fighting Scorpion. Ready. Fight")
        print("Scorpion throws a punch first")
        firstscorpionmove = str(input("Dodge Right or Dodge Left"))
        a = "Dodge Right"
        b = "Dodge Left"

# Dodge Right of Scorpion
        if firstscorpionmove ==a:
            print("You grab him arm and break his arm in half")
            nextscorpionmove = str(input("You go in for another move. What will you do? Choke him out, Move back"))
            a = "Choke him out"
            b = "Move back"

 #Choke him out
  if nextscorpionmove ==a:
      print("The move didn't work and ended up not reaching his neck")



#
