from gameplay import Gameplay

def main():
    x = input()
    try:
        x = int(x)
        ginstance = Gameplay(x)
        ginstance.setup()
        ginstance.interactionPhase()
        ginstance.currentBias()
        ginstance.interactionPhase()
        ginstance.currentBias()

    except ValueError:
        print('number must be an int')



if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
