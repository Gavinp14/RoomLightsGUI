from GUI import GUI
from Light import Light
from GoveeAPI import GoveeAPI

# Govee API init
API_KEY = '3c0f07ac-3b53-486f-9b93-da125606f1d3'
API = GoveeAPI(API_KEY)

#lights
lampLight = Light(API, 'A5:D4:60:74:F4:FF:F8:84', 'H6004')
fanLight = Light(API, '27:D4:60:74:F4:FB:86:C8', 'H6004')

#initialize GUI
gui = GUI(lampLight, fanLight)

if __name__ == "__main__":
    gui.mainloop()
