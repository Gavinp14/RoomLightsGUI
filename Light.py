
class Light:
    def __init__(self, api, lightID, lightModel):
        self.api = api
        self.lightID = lightID
        self.lightModel = lightModel

    def turnOff(self):
        return self.api.turnOff(self.lightModel, self.lightID)

    def turnOn(self):
        return self.api.turnOn(self.lightModel, self.lightID)

    def changeToRed(self):
        return self.api.changeColor(self.lightModel, self.lightID, 9109504) #integer values of red

    def changeToWhite(self):
        return self.api.changeColor(self.lightModel, self.lightID, 16772805) #integer values of white

    def changeToBlue(self):
        return self.api.changeColor(self.lightModel, self.lightID, 3302550) #integer values of blue

