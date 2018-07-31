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

        if self.__hour >= 12:
            am_or_pm = 'PM'
            formatted_hour = self.__hour - 12

            if formatted_hour == 0:
                formatted_hour = 12
        elif self.__hour < 12:
            am_or_pm = 'AM'
            formatted_hour = self.__hour

            if formatted_hour == 0:
                formatted_hour = 12

        return '%s:%s:%s %s' % (
            formatted_hour, self.__minute, self.__second, am_or_pm)

    def setHour(self, hour):
        if type(hour) is int and 24 > hour >= 0:
            self.__hour = hour
        else:
            self.__hour = 0

    def getHour(self):
        return self.__hour

    def setMinute(self, minute):
        if type(minute) is int and 60 > minute >= 0:
            self.__minute = minute
        else:
            self.__minute = 0

    def getMinute(self):
        return self.__minute

    def setSecond(self, second):
        if type(second) is int and 60 > second >= 0:
            self.__second = second
        else:
            self.__second = 0

    def getSecond(self):
        return self.__second

# Test cases then output from test cases:
# wrongType = Clock('a', 'b', 'c')
# print('wrongType =', wrongType)
# shouldWork = Clock(2, 30, 50)
# print('shouldWork =', shouldWork)
# mixedTypes = Clock(12, 0, 'c')
# print('mixedTypes =', mixedTypes)
# missingArgs = Clock(12)
# print('missingArgs =', missingArgs)
# lowerAM = Clock(0, 0, 0)
# print('lowerAM =', lowerAM)
# upperAM = Clock(11, 59, 59)
# print('upperAM =', upperAM)
# lowerPM = Clock(12, 0, 0)
# print('lowerPM =', lowerPM)
# upperPM = Clock(23, 59, 59)
# print('upperPM =', upperPM)
# Output:
# wrongType = 12:0:0 AM
# shouldWork = 2:30:50 AM
# mixedTypes = 12:0:0 PM
# missingArgs = 12:0:0 PM
# lowerAM = 12:0:0 AM
# upperAM = 11:59:59 AM
# lowerPM = 12:0:0 PM
# upperPM = 11:59:59 PM
