from phonenumbers import geocoder,timezone
import phonenumbers,datetime
import pytz
from datetime import datetime

def getAreaName(number):
    cx_number = phonenumbers.parse("+1"+str(number))
    return geocoder.description_for_number(cx_number,'en')


def getTimeZone(number):
    cx_number = phonenumbers.parse("+1"+str(number))
    cx_timezone = timezone.time_zones_for_number(cx_number)
    return cx_timezone

def getLocalTime(TimeZone):
    return datetime.now(pytz.timezone(TimeZone[0]))

print(getAreaName(9078909242))
print(getTimeZone(9078909343))
print(getLocalTime(getTimeZone(9078909242)))
