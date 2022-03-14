IP Info custom based on the IPinfo Python Client Library https://github.com/ipinfo/python


|Getting Started - Quick Method|
----------------------------------------------------------------------------------------------------------
Quick Start: 

requirements: 

⚫Python 3.5 or greater - NO EOL Python versions >;)

⚫PIP

Installation:

pip install ipinfo

Then create an account for IPinfo in order to get your API access token and input it at access_token in IP_info.py

Usage: python IP_info.py


-----------------------------------------------------------------------------------------------------------

|Getting Started - Developer/Advanced|
-----------------------------------------------------------------------------------------------------------
requirements: 

⚫Python 3.5 or greater - NO EOL Python versions >;)

⚫PIP

pip -r requirements.txt (Not all are used in the current form of the script, such as asyncio)

Usage: python IP_info.py

-----------------------------Details Data-----------------------------------

The `Handler.getDetails()` method accepts an IP address as an optional, positional argument. If no IP address is specified, the API will return data for the IP address from which it receives the request.


The `handler.getDetails()` method will return a `Details` object that contains all fields listed in the [IPinfo developer docs](https://ipinfo.io/developers/responses#full-response) with a few minor additions. Properties can be accessed directly.

---------------------------------------------------------
details.ip -returns IP Address                          
details.hostname -returns hostname (doesn't always work)
details.city -returns city                              
details.region -returns region                          
details.country -returns country                        
details.loc -returns location coordinates               
details.org -returns organization name                 
details.postal -returns postal code                    
details.timezone returns timezone                      
---------------------------------------------------------


- [IP geolocation / geoIP data](https://ipinfo.io/ip-geolocation-api) (city, region, country, postal code, latitude and longitude)
- [ASN details](https://ipinfo.io/asn-api) (ISP or network operator, associated domain name, and type, such as business, hosting or company)
- [Firmographics data](https://ipinfo.io/ip-company-api) (the name and domain of the business that uses the IP address)
- [Carrier information](https://ipinfo.io/ip-carrier-api) (the name of the mobile carrier and MNC and MCC for that carrier if the IP is used exclusively for mobile traffic)
