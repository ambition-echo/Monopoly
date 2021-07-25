from pygame import font
import dice
import player
import citys

massage = font.Font(
    'font/HGY4_CNKI.TTF', 20)
massages = [massage.render('', True, (0, 0, 0)),
            massage.render('', True, (0, 0, 0))]


def go(player: player.player):
    global massage, massages
    temp = dice.dice()
    print(temp[0], temp[1], temp[2])
    player.position += temp[2]
    if player.position > 32:
        player.position = player.position % 32
    massages[1] = massage.render(
        f'{player.name}向前行走{temp[2]}格', True, (0, 0, 0))
    player.update()


def check(player: player.player):
    global massage, massages
    if citys.maps[player.position].__class__.__name__ == 'city':
        if citys.maps[player.position].owner == None:
            player.buy(citys.maps[player.position])
            massages[0] = massage.render(
                player.name+'购买了'+citys.maps[player.position].name, True, (0, 0, 0))
        else:
            if citys.maps[player.position].owner != player:
                player.pay(citys.maps[player.position])
                massages[0] = massage.render(
                    player.name+'在'+citys.maps[player.position].name+'向'+citys.maps[player.position].owner.name+'交了过路费', True, (0, 0, 0))
            else:
                citys.maps[player.position].leval += 1
                if citys.maps[player.position].leval > 3:
                    citys.maps[player.position].leval = 3
                else:
                    citys.maps[player.position].update()
                    massages[0] = massage.render(
                        citys.maps[player.position].name+'城市等级+1', True, (0, 0, 0))


print('success')
