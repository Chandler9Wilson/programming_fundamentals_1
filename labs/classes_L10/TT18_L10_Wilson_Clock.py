# Name: Chandler Wilson
# Date: 07/31/2018
# COSC1336, Lab 10, 2 parts:
#   part 1: Create the Clock class
#   part 2: Enhance Clock class


class Clock():

    def __init__(self, hour=0, minute=0, second=0):

        self.setHour(hour)
        self.setMinute(minute)
        self.setSecond(second)

    def __str__(self):
        return 'hour: %s, minute: %s, second: %s' % (
            self.__hour, self.__minute, self.__second)

        if self.__hour == 0:
            return '11:59 AM'
        elif self.__hour >= 12:
            return 'PM'
        elif self.__hour <= 12:
            return 'AM'

    def setHour(self, hour):
        if type(hour) is int and 24 > hour > 0:
            self.__hour = hour
        else:
            self.__hour = 0

    def getHour(self):
        return self.__hour

    def setMinute(self, minute):
        if type(minute) is int and 59 > minute > 0:
            self.__minute = minute
        else:
            self.__minute = 0

    def getMinute(self):
        return self.__minute

    def setSecond(self, second):
        if type(second) is int and 59 > second > 0:
            self.__second = second
        else:
            self.__second = 0

    def getSecond(self):
        return self.__second


wrongType = Clock('a', 'b', 'c')
print(wrongType)
shouldWork = Clock(2, 30, 50)
print(shouldWork)
mixedTypes = Clock(12, 0, 'c')
print(mixedTypes)
missingArgs = Clock(12)
print(missingArgs)
