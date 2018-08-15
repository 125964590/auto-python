import requests
import datetime

saveTime = 7
newDay = datetime.datetime.now().strftime('%d')  # define new day
newTime = datetime.datetime.now().strftime('%Y.%m.')
maxDay = str(int(newDay) - saveTime)
request = "http://192.168.100.110:9400/"


def deleteOne(day):
    delete = requests.delete(url=request + '*' + day + '*')


if __name__ == "__main__":
    if len(maxDay) < 2:
        maxDay = '0' + maxDay
deleteOne(day=newTime + maxDay)
