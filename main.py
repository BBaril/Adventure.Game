# Bethany Baril
# 08/2024
#
# Choose your own adventure game. Python

from flask import Flask

app = Flask(__name__)

@app.route("/")
def adventure_game():
    return 
while True:
    answer = input("Would you like to play an adventure game? (yes/no) ")

    if answer.lower().strip() == "yes":

        print("You are in the woods, traveling along an old path, heading towards a castle. You continue for a")
        print("little bit when you hear something approaching. You realize it is a group of goblins.")
        answer = input("Would you like to hide or run to the castle? (hide/run) ").lower().strip()

        if answer == "run":
            print("You dart off towards the castle and stumble to the ground. The goblins have noticed and are close.")
            answer = input("Do you fight or keep going? (fight/go) ")

            if answer == "fight":
                print("The goblins attack and quickly end your life.... game over")
            else:
                print("As you approach the castle, the archers stop the goblins. The guard asks what your business is.")
                answer = input("Joining the war against The Trolls or a traveling salesman? (war/salesman) ")
                if answer == "salesman":
                    print("The guards send you on your way. Bandits attack and leave you with nothing.... game over")
                else:
                    print("The guards open the gate and tell you to report to training first thing in the morning.")
                    print("You find a bed for the night above the tavern.")
                    answer = input(" Do you go to bed early or have a drink? "
                                   "(bed/drink) ")
                    if answer == "bed":
                        print("You decide to get a good nights sleep.")
                        answer = input("During training, the instructor asks if you prefer to use a sword or a bow? "
                                       "(sword/bow) ")
                        if answer == "sword":
                            print("You practice all day. Then you are given a meal and told to be ready at dawn.")
                            print("The ground shaking wakes you up. You look out to see a troll's foot over your "
                                  "tent.... game over")
                        else:
                            print("You practice all day. Then you are given a meal and told to be ready at dawn.")
                            print("The ground shaking wakes you up. There is a troll in camp. ")
                            print("You are greatly injured by a flying tree.... game over")
                    else:
                        print("You decide to relax with a drink and get to talking with a group of people. ")
                        print("Another recruit named Bram reminds you of your younger brother.")
                        answer = input("During training, the instructor asks if you prefer to use a sword or a bow? "
                                       "(sword/bow) ")
                        if answer == "sword":
                            print("Bram also works with a sword and you are assigned a tent next to him after practice")
                            print("In the middle of the night he jerks you out bed and tells you a troll is near. ")
                            print("You manage to exit just as the tent gets crushed by a foot. ")
                            print("Everyone fights. The troll is defeated. You live to see anther day.... Great Game!!")
                        else:
                            print("You practice all day, given a meal, and a tent on the other side of camp as "
                                  "your friends. ")
                            print("The ground shaking wakes you up. You grab your bow and arrows. ")
                            print("As you raise your bow to shoot you see a horse flying towards you.... game over")

        elif answer == "hide":
            print("As you duck down you notice an open to a cave.")
            print("You slip down and notice its mostly open with two paths leading back.")
            answer = input("Which way do you go? (left/right) ")

            if answer == "left":
                print("You slip and fall. You are stuck at the bottom of a dark cave with a broken leg.... game over")
            else:
                print("You go down the path as far can while still seeing light.")
                print("Shorty after you are attack by a giant spider.... game over")
    else:
        print("Thanks for your time.")
        break
