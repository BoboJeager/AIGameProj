from gameplay import Gameplay
import math
import matplotlib.pyplot as plt

# runs game


def main():
    x = input("Please enter the size for the game: ")
    redLearningGraph = []
    greyagentsforBlue = math.ceil(float(x)*0.05)
    startingMaxUncertainty = input("Input MAX uncertainty green can have: ")
    startingMinUncertainty = input(
        "Input MIN Uncertainty green can have (enter a positive number and it will be converted to negative): ")
    playerPlayingBlue = False
    playerPlayingRed = False

    players = input("Number of players: ")
    if (int(players) == 1):
        team = input("Do you want to play as blue? (y/n) ")
        if (team == 'y'):
            playerPlayingBlue = True
        else:
            playerPlayingRed = True
    if (int(players) == 2):
        playerPlayingBlue = True
        playerPlayingRed = True

    numGames = input("How many games do you wish to run? ")
    displayGraphAfter = input(
        "Do you want to be asked to display the graph after each game? (y/n): ")

    winners = []
    winpercentage = []
    try:
        for i in range(int(numGames)):
            startingMaxUncertainty = float(startingMaxUncertainty)
            startingMinUncertainty = float(startingMinUncertainty)
            x = int(x)
            ginstance = Gameplay(x, startingMaxUncertainty,
                                 startingMinUncertainty, playerPlayingBlue, playerPlayingRed, greyagentsforBlue)
            ginstance.aiplayers.redAILearningGraph = redLearningGraph
            ginstance.setup()

            GameRunning = True
            while GameRunning:
                print("\nThis is red teams turn!")
                ginstance.redTeamTurn()
                ginstance.interactionPhase()
                if int(players) != 0:
                    showGraph = input(
                        "Do you want to view the graph of the current state of the game? (y/n): ")
                    if showGraph == 'y':
                        ginstance.displayWindows()
                print("\nThis is the blue teams turn!")
                ginstance.blueTeamTurn()
                # print("\tBlue energy remaining: ",
                #       ginstance.bluePlayer.energy)
                ginstance.interactionPhase()
                ginstance.aiplayers.turn += 1
                if int(players) != 0:
                    showGraph = input(
                        "Do you want to view the graph of the current state of the game? (y/n): ")
                    if showGraph == 'y':
                        ginstance.displayWindows()
                if ginstance.bluePlayer.energy <= 0 or ginstance.aiplayers.blueAI.energy <= 0:
                    break
            print(
                "The game has ended!")
            ginstance.aiplayers.turn = 0
            if ginstance.getVoting() > 50:
                print(
                    "Blue has won the game and convinced the majority of Green to vote!")
                print(ginstance.getVoting(),
                      "% of the population decided to vote.")
                winners.append("Blue")
            elif ginstance.getVoting() < 50:
                print(
                    "Red has won the game and convinced the majority of Green to vote!")
                winningpercentage = 100 - ginstance.getVoting()
                print(winningpercentage,
                      "% of the population decided to not vote")
                winners.append("Red")
                winningpercentage -= ginstance.getVoting()
                ginstance.aiplayers.saveRedWinningState(
                    ginstance.aiplayers.initialState, winningpercentage, ginstance.aiplayers.redFirstFiveMoves)
                redLearningGraph = ginstance.aiplayers.redAILearningGraph.copy()
            else:
                print(
                    "The game was a tie! Half of the population decided to vote and half decided not to.")
                winners.append("Tie")
            if displayGraphAfter == 'y':

                showGraph = input(
                    "Do you want to view the graph of the current state of the game? (y/n) \n")
                if showGraph == 'y':
                    ginstance.displayWindows()
                else:
                    continue
            winpercentage.append(ginstance.getVoting())

    except ValueError:
        print('Error! The number entered must be an int. ')
    if int(numGames) > 1:
        print(winners)
        print(winpercentage)
        BlueWin = 0
        RedWin = 0
        NoWin = 0
        for item in winners:
            if item == 'Blue':
                BlueWin += 1
            elif item == 'Red':
                RedWin += 1
            else:
                NoWin += 1
        print("Number of blue wins: ", BlueWin)
        print("Number of red wins: ", RedWin)
        print("Number of tied games: ", NoWin)
        print("Red learning graph is", ginstance.aiplayers.redAILearningGraph)

        fig1, ax1 = plt.subplots()
        sizes = [BlueWin, RedWin, NoWin]
        chartLabels = "BlueWins", "RedWins", "Tie"
        chartColors = ["blue", "red", "grey"]
        ax1.pie(sizes, labels=chartLabels,  autopct='%1.1f%%',
                shadow=True, colors=chartColors)
        ax1.axis('equal')
        fig = plt.gcf()
        fig.set_size_inches(6, 6)
        plt.show()


if __name__ == '__main__':
    main()
