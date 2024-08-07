#텔레비전을 클래스로 정의한다.
class Tv:
    def __init__(self, channel=24, volume=10, on=False):  # Corrected __int__ to __init__
        self.channel = channel
        self.volume = volume
        self.on = on
    def setOn(self):
        self.on = True

    def show(self):
        print(self.channel, self.volume, self.on)

    def setChannel(self, channel):
        self.channel = channel
        
    def getChannel(self):
        return self.channel
    def volumeUp(self):
        self.volume += 1
    def volumeDown(self):
        self.volume -= 1
    def setSilentMode(t):
        t.volume = 2

tv1 = Tv()
tv1.show()
tv1.setChannel(21)
tv1.show()