import schedule
import time
import threading
from Light import Light
from GoveeAPI import GoveeAPI

# Govee API init
API_KEY = '3c0f07ac-3b53-486f-9b93-da125606f1d3'
API = GoveeAPI(API_KEY)

#lights
lampLight = Light(API, 'A5:D4:60:74:F4:FF:F8:84', 'H6004')
fanLight = Light(API, '27:D4:60:74:F4:FB:86:C8', 'H6004')

def turnOnNightLights():
    lampLight.changeToRed()
    fanLight.changeToRed()
    lampLight.turnOn()
    fanLight.turnOn()

def turnOnMorningLights():
    lampLight.changeToWhite()
    fanLight.changeToWhite()
    lampLight.turnOn()
    fanLight.turnOn()

def turnOff():
    lampLight.turnOff()
    fanLight.turnOff()

# Monday Schedule
schedule.every().monday.at("07:30").do(turnOnMorningLights)
schedule.every().monday.at("21:00").do(turnOnNightLights)
schedule.every().monday.at("22:00").do(turnOff)

# Tuesday Schedule
schedule.every().tuesday.at("09:30").do(turnOnMorningLights)
schedule.every().tuesday.at("21:00").do(turnOnNightLights)
schedule.every().tuesday.at("22:00").do(turnOff)

# Wednesday Schedule
schedule.every().wednesday.at("07:30").do(turnOnMorningLights)
schedule.every().wednesday.at("21:00").do(turnOnNightLights)
schedule.every().wednesday.at("22:00").do(turnOff)

# Thursday Schedule
schedule.every().thursday.at("09:30").do(turnOnMorningLights)
schedule.every().thursday.at("21:00").do(turnOnNightLights)
schedule.every().thursday.at("22:00").do(turnOff)

schedule.every().day.at("19:46").do(turnOff)

while True:
    print(schedule.get_jobs())
    schedule.run_pending()
    time.sleep(1)