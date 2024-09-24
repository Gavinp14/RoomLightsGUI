import requests
import uuid

class GoveeAPI:
    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.baseURL = 'https://openapi.api.govee.com/router/api/v1/'
        self.headers = {
            'Govee-API-Key': apiKey,
            'Content-Type': 'application/json'
        }

    #retrieve all device data from account
    def getDevices(self):
        endpoint = "user/devices"
        response = requests.get(f"{self.baseURL}{endpoint}", headers=self.headers)
        print(response.json())

    #enpoints for device control
    def turnOff(self, model, device):
        endpoint = "device/control"
        data = {
            "requestId": str(uuid.uuid4()),
            "payload": {
                "sku": model,
                "device": device,
                "capability": {
                    "type": "devices.capabilities.on_off",
                    "instance": "powerSwitch",
                    "value": 0  # 0 to turn off, 1 to turn on
                }
            }
        }
        return requests.post(f"{self.baseURL}{endpoint}", headers=self.headers, json=data)

    def turnOn(self, model, device):
        endpoint = "device/control"
        data = {
            "requestId": str(uuid.uuid4()),
            "payload": {
                "sku": model,
                "device": device,
                "capability": {
                    "type": "devices.capabilities.on_off",
                    "instance": "powerSwitch",
                    "value": 1  # 0 to turn off, 1 to turn on
                }
            }
        }
        return requests.post(f"{self.baseURL}{endpoint}", headers=self.headers, json=data)

    def changeColor(self, model, device, setting):
        endpoint = "device/control"
        data = {
            "requestId": str(uuid.uuid4()),
            "payload": {
                "sku": model,
                "device": device,
                "capability": {
                    "type": "devices.capabilities.color_setting",
                    "instance": "colorRgb",
                    "value": setting
                }
            }
        }

        return requests.post(f"{self.baseURL}{endpoint}", headers=self.headers, json=data)




