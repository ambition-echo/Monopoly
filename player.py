from random import randint
from pygame.image import load
from pygame import font
import citys

font.init()


class player(object):
    def __init__(self, name: str, id: int, img, car, name__font):
        self.name = name
        self.id = id
        self.img = img  # 所有城市贴图
        self.car = car
        self.assets = 50000  # 资产
        while True:
            temp = randint(0, 23)
            if citys.citys[temp].owner == None:
                self.owned_citys = [citys.citys[temp]]  # 所有城市
                citys.citys[temp].owner = self
                break
        while True:
            temp = randint(0, 23)
            if citys.citys[temp].owner == None:
                self.owned_citys.append(citys.citys[temp])  # 所有城市
                citys.citys[temp].owner = self
                break
        self.life = True  # 是否破产
        self.position = 1  # 位置
        self.name__font = name__font
        self.name_font = font.SysFont("consolas", 28).render(
            self.name + '       ' + str(len(self.owned_citys)), True,
            self.name__font)
        self.assets_font = font.SysFont("consolas", 28).render(
            'Assets:' + str(self.assets), True, (255, 0, 0))

    def update(self):
        self.assets_font = font.SysFont("consolas", 28).render(
            'Assets:' + str(self.assets), True, (255, 0, 0))
        self.name_font = font.SysFont("consolas", 28).render(
            self.name + '       ' + str(len(self.owned_citys)), True,
            self.name__font)

    # 购买城市

    def buy(self, target: citys.city):
        if self.assets >= target.price:
            self.assets -= target.price
            self.owned_citys.append(target)
            target.owner = self
            self.update()
            return True
        else:
            return False

    # 出售城市

    def sell(self, target: citys.city):
        if target in self.owned_citys:
            self.owned_citys.remove(target)
            self.assets += target.price

    # 交过路费

    def pay(self, target: citys.city):
        if self.assets > target.income:
            self.assets -= target.income
            target.owner.charge(target)
            self.update()
        else:
            target.owner.charge(target)
            self.bankruptcy()
            self.update()

    # 收过路费(不需要单独调用，路过者交路费时自动调用)

    def charge(self, target: citys.city):
        self.assets += target.income
        self.update()

    # 破产

    def bankruptcy(self):
        self.assets = 0
        global aliveplayers
        aliveplayers.remove(self)


player1 = player('hgy', 1, load('img/player1.png'), load('img/car1.png'),
                 (148, 20, 252))
player2 = player('hgj', 2, load('img/player2.png'), load('img/car2.png'),
                 (252, 28, 100))
player3 = player('g k', 3, load('img/player3.png'), load('img/car3.png'),
                 (43, 240, 15))

players = [player1, player2, player3]
aliveplayers = [player1, player2, player3]
if __name__ == '__main__':
    for i in player3.owned_citys:
        print(i.name, i.position)
