from pygame import font
import dice
import player
import citys

massage = font.Font('font/HGY4_CNKI.TTF', 20)
massages = [
    massage.render('', True, (0, 0, 0)),
    massage.render('', True, (0, 0, 0)),
    massage.render('玩家已破产！', True, (0, 0, 0))
]


def go(player: player.player):
    global massage, massages
    temp = dice.dice()
    print(temp[0], temp[1], temp[2])
    player.position += temp[2]
    if player.position > 32:
        player.position = player.position % 32
    massages[1] = massage.render(f'{player.name}向前行走{temp[2]}格', True,
                                 (0, 0, 0))
    player.update()


def check(player_: player.player):
    global massage, massages
    if citys.maps[player_.position].__class__.__name__ == 'city':
        if citys.maps[player_.position].owner == None:
            if player_.buy(citys.maps[player_.position]):
                massages[0] = massage.render(
                    player_.name + '购买了' + citys.maps[player_.position].name,
                    True, (0, 0, 0))
        else:
            if citys.maps[player_.position].owner != player_:
                player_.pay(citys.maps[player_.position])
                massages[0] = massage.render(
                    player_.name + '在' + citys.maps[player_.position].name +
                    '向' + citys.maps[player_.position].owner.name + '交了过路费',
                    True, (0, 0, 0))
            else:
                citys.maps[player_.position].leval += 1
                if citys.maps[player_.position].leval > 3:
                    citys.maps[player_.position].leval = 3
                else:
                    citys.maps[player_.position].update()
                    massages[0] = massage.render(
                        citys.maps[player_.position].name + '城市等级+1', True,
                        (0, 0, 0))
    else:
        if citys.maps[player_.position].name == 'start':
            temp = ''
            for i in player_.owned_citys:
                i.update()
                temp += i.name + ' '
            massages[0] = massage.render(temp + '城市等级+1', True, (0, 0, 0))


print('success')
