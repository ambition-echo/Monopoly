import player
from pygame import font
import event
isover = False
state = False
round = 0
rounds = font.SysFont("consolas", 28).render(
    str(round)+'/∞', True, (0, 0, 0))


def main():
    global round, isover, rounds
    while True:
        while True:
            # print(isover)
            if player.player1.life:
                if state:
                    quit()
                if isover:
                    isover = False
                    event.go(player.player1)
                    event.check(player.player1)
                    break
            else:
                break
        while True:
            # print(isover)
            if player.player2.life:
                if state:
                    quit()
                if isover:
                    isover = False
                    event.go(player.player2)
                    event.check(player.player2)
                    break
            else:
                break
        while True:
            # print(isover)
            if player.player3.life:
                if state:
                    quit()
                if isover:
                    isover = False
                    event.go(player.player3)
                    event.check(player.player3)
                    break
            else:
                break
        round += 1
        rounds = font.SysFont("consolas", 28).render(
            str(round)+'/∞', True, (0, 0, 0))


if __name__ == '__main__':
    main()
