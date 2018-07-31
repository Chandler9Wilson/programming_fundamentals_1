# Name: Chandler Wilson
# Date: 07/31/2018
# COSC1336, Lab 10, 2 parts:
#   part 1: Create the Clock class
#   part 2: Enhance Clock class


class Clock():

    def __init__(self, hour, minute, second):

        self.setHour(hour)
        self.setMinute(minute)
        self.setSecond(second)

    def __str__(self):
        if self.__hour == 0:
            return '11:59 AM'
        elif self.__hour >= 12:
            return 'PM'
        elif self.__hour <= 12:
            return 'AM'

    def setHour(self, hour):
        if 24 > hour > 0:
            self.__hour = hour

    def getHour(self):
        return self.__hour

    def setMinute(self, minute):
        if 59 > minute > 0:
            self.__minute = minute

    def getMinute(self):
        return self.__minute

    def setSecond(self, second):
        if 59 > second > 0:
            self.__second = second

    def getSecond(self):
        return self.__second
