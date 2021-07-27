from pygame.locals import *
import background
import pygame
import player
import event
import citys


def init():
    global screen
    pygame.init()
    pygame.font.init()
    pygame.display.init()
    pygame.display.set_caption('Monopoly')
    screen = pygame.display.set_mode((729, 729))


def put_pic():
    global screen
    screen.fill((0, 0, 0))
    # 地块citys
    for i in citys.citys:
        screen.blit(i.img.convert(), i.position)
        screen.blit(i.name_font, i.position)
    # 特殊地块stations
    for i in citys.stations:
        screen.blit(i.img.convert(), i.position)
    # 玩家所有城市贴图
    for i in player.players:
        for j in i.owned_citys:
            screen.blit(i.img.convert_alpha(), j.position)
    # 玩家位置贴图car
    for i in player.players:
        screen.blit(i.car.convert_alpha(), citys.maps[i.position].position)
    # 中央贴图

    screen.blit(citys.center.convert(), (81, 81))  # center


def put_font():
    global screen
    screen.blit(player.player1.name_font, (81 * 5, 81 * 6))
    screen.blit(player.player2.name_font, (81 * 5, 81))
    screen.blit(player.player3.name_font, (81, 81))
    screen.blit(player.player1.assets_font, (81 * 5, 81 * 6 + 40))
    if player.player1 not in player.aliveplayers:
        screen.blit(event.massages[2], (81 * 5, 81 * 6 + 70))
    screen.blit(player.player2.assets_font, (81 * 5, 81 + 40))
    if player.player2 not in player.aliveplayers:
        screen.blit(event.massages[2], (81 * 5, 81 + 70))
    screen.blit(player.player3.assets_font, (81, 81 + 40))
    if player.player3 not in player.aliveplayers:
        screen.blit(event.massages[2], (81, 81 + 70))
    screen.blit(background.rounds, (81 * 4 + 5, 81 * 4 + 30))
    screen.blit(event.massages[0], (81, 81 * 6 + 30))
    screen.blit(event.massages[1], (81, 81 * 6))
    pygame.display.update()


def main():
    global state
    init()
    while True:
        for i in pygame.event.get():
            if i.type == QUIT:
                background.state = True
                quit()
            if i.type == KEYDOWN:
                if i.key == K_SPACE:
                    print('success')
                    background.isover = True
        #background.isover = True
        put_pic()
        put_font()


if __name__ == '__main__':
    main()
