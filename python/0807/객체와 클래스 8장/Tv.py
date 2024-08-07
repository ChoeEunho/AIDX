class Tv:
    def __init__(self, channel, volume, on):  # Corrected __int__ to __init__
        self.channel = channel
        self.volume = volume
        self.on = on

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

tv1 = Tv(24, 10, True)
tv1.show()

tv1.setChannel(21)
tv1.show()

