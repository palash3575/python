from suntime import Sun, SunTimeException
import geocoder


def mySuntime(query):
    
    '''
    #uncomment this section when online
    geo = geocoder.ip('me') 
    latitude = geo.latlng[0]
    longitude= geo.latlng[1]
    '''
    #this section for my own location
    latitude = 22.5837655
    longitude = 90.2677207

    '''

    # get ipinfo from ipinfo.io
    #geo = geocoder.ip('me')
    if geocoder.ip('me').ok == False:
        latitude = 22.5837655
        longitude = 90.2677207
        
    else:
        geo = geocoder.ip('me')
        latitude = geo.latlng[0]
        longitude= geo.latlng[1]
    '''
    sun = Sun(latitude, longitude)

    todaySr = sun.get_local_sunrise_time()
    todaySs = sun.get_local_sunset_time()

    sunRiseHour = int(todaySr.strftime('%H'))
    sunRiseMinute = int(todaySr.strftime('%M'))
    sunRiseAmPm= "AM"
    if sunRiseHour >= 12:
        sunRiseHour = sunRiseHour-12
        sunRiseAmPm = "PM"


    sunSetHour = int(todaySs.strftime('%H'))
    sunSetMinute = int(todaySs.strftime('%M'))

    sunSetAmPm= "AM"
    if sunSetHour >= 12:
        sunSetHour = sunSetHour-12
        sunSetAmPm = "PM"
    #return only sunrise time
    if query =='sunrise':
        return f"todays sunrise time is {sunRiseHour} : {sunRiseMinute} : {sunRiseAmPm}"
    #return only sunset time
    elif query == 'sunset':
        return f"todays sunset  time is {sunSetHour} : {sunSetMinute} : {sunSetAmPm}"
    #return both sunrise and sunset time
    elif query == 'sunrise and sunset' or query == 'sunset and sunrise':
        return f"todays sunrise time is {sunRiseHour} : {sunRiseMinute} : {sunRiseAmPm} and todays sunset  time is {sunSetHour} : {sunSetMinute} : {sunSetAmPm}"
    #error message 
    else:
        return 'opps the perfect query will be "sunris"/"sunset"/"sunrise and sunset"/"sunset and sunrise"'

# all out puts 
print(mySuntime('sunrise'))
print(mySuntime('sunset'))
print(mySuntime('sunrise and sunset'))
print(mySuntime('sunset and sunrise'))
print(mySuntime('any text '))
