from gameplay import Gameplay
from blueNode import BlueNode


def main():
    x = input("Please enter the size for the game: ")
    GameRunning = True

    try:
        x = int(x)
        ginstance = Gameplay(x)
        ginstance.setup()
        ginstance.displayNetwork()
        while GameRunning:
            # If red team has no followers, end game - needs red team follower functionality first
            print("This is the red team's turn")
            ginstance.redTeamTurn()

            if ginstance.bluePlayer.energy == 0:
                GameRunning = False
                print(
                    "The game has ended! Please see the network displayed for the final results of the game!")
            else:
                print("This is the blue teams turn")
                ginstance.blueTeamTurn()

        ginstance.displayNetwork()

    except ValueError:
        print('Error! The number entered must be an int. ')


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
