from GoveeAPI import GoveeAPI

class Light:
    def __init__(self, api, lightID, lightModel):
        self.api = api
        self.lightID = lightID
        self.lightModel = lightModel

    def turnOff(self):
        return self.api.turnOff(self.lightModel, self.lightID)

    def turnOn(self):
        return self.api.turnOn(self.lightModel, self.lightID)
