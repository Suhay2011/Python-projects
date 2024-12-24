import random #importing module
import time


def getRandomDate(startDate , endDate ) : #definning function
    print("Printing random date between", startDate ,"and", endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%y'

    startTime = time.mktime(time.strptime(startDate , dateFormat))
    endTime = time.mktime(time.strptime(endDate , dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat,time.localtime(randomTime))
    return randomDate
#display resultprint("Random Date =",getRandomDate("1/1/2016") , ("12/12/2018"))