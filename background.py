import player
from pygame import font
import event

isover = False
state = False
round = 0
rounds = font.SysFont("consolas",
                      28).render(str(round) + '/∞', True, (0, 0, 0))


def main():
    global round, isover, rounds
    while True:
        for player_ in player.aliveplayers:
            while True:
                if state:
                    quit()
                if isover:
                    isover = False
                    event.go(player_)
                    event.check(player_)
                    break
        round += 1
        rounds = font.SysFont("consolas",
                              28).render(str(round) + '/∞', True, (0, 0, 0))


if __name__ == '__main__':
    main()
