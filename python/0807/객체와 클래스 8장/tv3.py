class Tele3:
    objectCnt = 0
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
        Tele3.objectCnt += 1

    def show(self):
        print(self.channel, self.volume, self.on, self.objectCnt)

myTv = Tele3(24, 10, True)
myTv.show()
yourTv = Tele3(21, 20, False)
yourTv.show()

