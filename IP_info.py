import ipinfo
import time

#Apple IP 57.116.146.168

access_token = ('') #Put IPinfo API key here

handler = ipinfo.getHandler(access_token)

local_time = time.asctime(time.localtime(time.time()))
print ('Local current time is : ', local_time)


ip_address = input('Enter a IP address: ') #Get user input for IP address
details = handler.getDetails(ip_address) #Handler to fetch details from ipinfo

def returnInfo():
    print ('IP address: ' , details.ip)
    print ('City: ' , details.city)
    print ('Region: ' , details.region)
    print ('Country Code:  ' , details.country,  ' Country Name:  ' , details.country_name)
    print ('Organization: ' , details.org)
    print ('Postal Code: ' , details.postal)
    print ('Timezone: ' , details.timezone)
    print ('Latitude: ' , details.latitude)
    print ('Longitude: ' , details.longitude)


returnInfo()


'''
---------------------------------------------------------
Arguments for shell:                                    |
                                                        |
details.ip -returns IP Address                          |
details.hostname -returns hostname (doesn't always work)|
details.city -returns city                              |
details.region -returns region                          |
details.country -returns country                        |
details.loc -returns location coordinates               |
details.org -returns organization name                  |
details.postal -returns postal code                     |
details.timezone returns timezone                       |
---------------------------------------------------------
'''
