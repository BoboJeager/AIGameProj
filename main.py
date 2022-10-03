from gameplay import Gameplay


def main():
    x = input("build your grid")
    try:
        x = int(x)
        ginstance = Gameplay(x)
        ginstance.setup()
        ginstance.redTeamTurn()
        ginstance.blueTeamTurn()
        ginstance.displayNetwork()

    except ValueError:
        print('number must be an int')


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
