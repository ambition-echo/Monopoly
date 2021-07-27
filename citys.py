from pygame.image import load
from pygame import font

font.init()


class city(object):
    def __init__(self, name: str, price: int, position: int, income: int):
        self.name = name  # 名字
        self.price = price  # 价格
        self.position = position  # 位置
        self.income = income  # 收入
        self.img1 = load('img/1.png')
        self.img2 = load('img/2.png')
        self.img3 = load('img/3.png')
        self.img = self.img1
        self.mult = 1  # 倍数
        self.leval = 1  # 等级
        self.owner = None  # 所有者
        self.name_font = font.Font('font/HGY4_CNKI.TTF', 14).render(
            self.name + '  ' + str(self.mult) + 'x', True, (0, 0, 0))

    def update(self):
        if self.leval == 1:
            self.img = self.img1
        if self.leval == 2:
            self.img = self.img2
        if self.leval == 3:
            self.img = self.img3


class station(object):
    def __init__(self, name, position, img):
        self.name = name
        self.position = position
        self.img = img


beijing = city('北京', 300, (81 * 7, 81 * 8), 5000)
shanghai = city('上海', 300, (81 * 6, 81 * 8), 5000)
guangzhou = city('广州', 300, (81 * 5, 81 * 8), 5000)
shenzhen = city('深圳', 300, (81 * 3, 81 * 8), 5000)
jinan = city('济南', 300, (81 * 2, 81 * 8), 5000)
nanchang = city('南昌', 300, (81 * 1, 81 * 8), 5000)
taibei = city('台北', 30000, (0, 81 * 7), 5000)
fuzhou = city('福州', 300, (0, 81 * 6), 5000)
hangzhou = city('杭州', 300, (0, 81 * 5), 5000)
changsha = city('长沙', 300, (0, 81 * 3), 5000)
xining = city('西宁', 300, (0, 81 * 2), 5000)
xi_an = city('西安', 300, (0, 81), 5000)
taiyuan = city('太原', 300, (81 * 1, 0), 5000)
changchun = city('长春', 300, (81 * 2, 0), 5000)
wuhan = city('武汉', 300, (81 * 3, 0), 5000)
kunming = city('昆明', 300, (81 * 5, 0), 5000)
lanzhou = city('兰州', 300, (81 * 6, 0), 5000)
chengdu = city('成都', 300, (81 * 7, 0), 5000)
haikou = city('海口', 300, (81 * 8, 81 * 1), 5000)
hefei = city('合肥', 300, (81 * 8, 81 * 2), 5000)
shenyang = city('沈阳', 300, (81 * 8, 81 * 3), 5000)
zhengzhou = city('郑州', 300, (81 * 8, 81 * 5), 5000)
chongqing = city('重庆', 300, (81 * 8, 81 * 6), 5000)
guiyang = city('贵阳', 300, (81 * 8, 81 * 7), 5000)

start = station('start', (81 * 8, 81 * 8), load('img/port.png'))
port1 = station('port1', (0, 81 * 8), load('img/port.png'))
port2 = station('port2', (0, 0), load('img/port.png'))
uncertain1 = station('', (81 * 4, 81 * 8), load('img/uncertain.png'))
uncertain2 = station('', (0, 81 * 4), load('img/uncertain.png'))
uncertain3 = station('', (81 * 4, 0), load('img/uncertain.png'))
uncertain4 = station('', (81 * 8, 81 * 4), load('img/uncertain.png'))
prison = station('prison', (81 * 8, 0), load('img/prison.png'))
center = load('img/center.png')
citys = [
    beijing, shanghai, guangzhou, shenzhen, jinan, nanchang, taibei, fuzhou,
    hangzhou, changsha, xining, xi_an, taiyuan, changchun, wuhan, kunming,
    lanzhou, chengdu, haikou, hefei, shenyang, zhengzhou, chongqing, guiyang
]
stations = [
    uncertain1, uncertain2, uncertain3, uncertain4, start, port1, port2, prison
]
maps = {
    1: start,
    2: beijing,
    3: shanghai,
    4: guangzhou,
    5: uncertain1,
    6: shenzhen,
    7: jinan,
    8: nanchang,
    9: port1,
    10: taibei,
    11: fuzhou,
    12: hangzhou,
    13: uncertain2,
    14: changsha,
    15: xining,
    16: xi_an,
    17: port2,
    18: taiyuan,
    19: changchun,
    20: wuhan,
    21: uncertain3,
    22: kunming,
    23: lanzhou,
    24: chengdu,
    25: prison,
    26: haikou,
    27: hefei,
    28: shenyang,
    29: uncertain4,
    30: zhengzhou,
    31: chongqing,
    32: guiyang
}
