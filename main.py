from gameplay import Gameplay
from blueNode import BlueNode
import math


def main():
    x = input("Please enter the size for the game: ")
    greyagentsforBlue = math.ceil(float(x)*0.05)
    startingMaxUncertainty = input("input MAX uncertainty green can have: ")
    startingMinUncertainty = input(
        "input MIN Uncertainty green can have (enter a positive number and it will be converted to negative): ")
    playerPlayingBlue = False
    playerPlayingRed = False

    players = input("Players playing: ")
    if(int(players) == 1):
        team = input("Do you want to play as blue? (y/n)")
        if(team == 'y'):
            playerPlayingBlue = True
        else:
            playerPlayingRed = True
    if(int(players) == 2):
        playerPlayingBlue = True
        playerPlayingRed = True

    # Need checks for valid inputs here - for testing play as both players for now
    # Starting uncertainties seems very high (all close to/if not at 1) - nvm I think this just break when min - uncertainty is -1

    print("WARNING: This is currently an endless while-loop for testing.")

    try:
        startingMaxUncertainty = float(startingMaxUncertainty)
        startingMinUncertainty = float(startingMinUncertainty)
        x = int(x)
        ginstance = Gameplay(x, startingMaxUncertainty,
                             startingMinUncertainty, playerPlayingBlue, playerPlayingRed, greyagentsforBlue)
        ginstance.setup()
        GameRunning = True
        while GameRunning:
            print("This red teams turn!")
            ginstance.redTeamTurn()
            ginstance.interactionPhase()

            print("This is the blue teams turn")
            ginstance.blueTeamTurn()
            print("Blue energy remaining: ",
                  ginstance.aiplayers.blueAI.energy)
            ginstance.interactionPhase()

            if ginstance.bluePlayer.energy <= 0 or ginstance.aiplayers.blueAI.energy <= 0:
                break
        print(
            "The game has ended!")
        if ginstance.getVoting() > 50:
            print("Blue has won the game and convinced the majority of Green to vote!")
            print(ginstance.getVoting(),
                  "% of the population decided to vote.")
        elif ginstance.getVoting() < 50:
            print("Red has won the game and convinced the majority of Green to vote!")
            print((100 - ginstance.getVoting()),
                  "% of the population decided to not vote")
        else:
            print(
                "The game was a tie! Half of the population decided to vote and half decided not to.")
        ginstance.displayWindows()
    except ValueError:
        print('Error! The number entered must be an int. ')


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/10
