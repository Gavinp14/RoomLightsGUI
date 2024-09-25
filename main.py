from GUI import GUI
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

#initialize GUI
gui = GUI(lampLight, fanLight)

if __name__ == "__main__":
    gui.mainloop()
