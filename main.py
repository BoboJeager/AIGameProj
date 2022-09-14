from gameplay import Gameplay

def main():
    x = input()
    try:
        x = int(x)
        ginstance = Gameplay(x)
        ginstance.setup()
        for i in ginstance.poplist:
            print(i.voting, i.uncertainty)
        ginstance.blueTeamTurn()
        for i in ginstance.poplist:
            print(i.voting, i.uncertainty)

    except ValueError:
        print('number must be an int')



if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
