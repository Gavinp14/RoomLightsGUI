import schedule
import time
from Light import Light
from GoveeAPI import GoveeAPI
from dotenv import load_dotenv
import os

#load .env variables
load_dotenv()

# Govee API init
API_KEY = os.getenv("API_KEY")
LAMP_ID = os.getenv("LAMP_LIGHT_ID")
FAN_ID = os.getenv("FAN_LIGHT_ID")
LIGHT_MODEL = os.getenv("LIGHT_MODEL")
API = GoveeAPI(API_KEY)

#lights
lampLight = Light(API, LAMP_ID, LIGHT_MODEL)
fanLight = Light(API, FAN_ID, LIGHT_MODEL)

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

#loop to check processes and see if they match current time
while True:
    print(schedule.get_jobs())
    schedule.run_pending()
    time.sleep(10)