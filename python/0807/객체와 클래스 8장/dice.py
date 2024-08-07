from random import randint     #주사위 굴리기
class Dice:
    def __init__(self,x,y):
        self._x=x
        self._y=y
        self._size=30
        self._value=1
    def getDiceValue(self):
        return self._value
    def printDice(self):
        print('주사위의 값 = ',self.__value)
    def rollDice(self):
        self.__value = randint(1,6)
dice1 = Dice(100,100)
dice1.rollDice()
dice1.printDice()