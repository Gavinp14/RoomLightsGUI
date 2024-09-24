import tkinter as tk

class GUI(tk.Tk):
    def __init__(self, lampLight, fanLight):
        super().__init__()
        self.lampLight = lampLight
        self.fanLight = fanLight
        self.title("Room Lights Control Panel")
        self.geometry("570x400")
        self.resizable(False, False)

        # Place widgets in window
        self.create_frames()
        self.place_labels()
        self.place_buttons()

    def turnOnBoth(self):
        self.lampLight.turnOn()
        self.fanLight.turnOn()

    def turnOffBoth(self):
        self.lampLight.turnOff()
        self.fanLight.turnOff()

    def changeBothToRed(self):
        self.lampLight.changeToRed()
        self.fanLight.changeToRed()

    def changeBothToWhite(self):
        self.lampLight.changeToWhite()
        self.fanLight.changeToWhite()

    def changeBothToBlue(self):
        self.lampLight.changeToBlue()
        self.fanLight.changeToBlue()

    def create_frames(self):
        # Create frames for lamp, both, and fan lights
        self.lamp_frame = tk.Frame(self)
        self.both_frame = tk.Frame(self)
        self.fan_frame = tk.Frame(self)

        # Grid layout for frames
        self.lamp_frame.grid(row=0, column=0, padx=20, pady=10)  # Left column
        self.both_frame.grid(row=0, column=1, padx=20, pady=10)  # Middle column
        self.fan_frame.grid(row=0, column=2, padx=20, pady=10)  # Right column

    def place_labels(self):
        # Labels for each frame
        self.label_lamp = tk.Label(self.lamp_frame, text="Lamp Light", font=("Arial", 16))
        self.label_lamp.pack(pady=(0, 5))

        self.label_both = tk.Label(self.both_frame, text="All Lights", font=("Arial", 16))
        self.label_both.pack(pady=(0, 5))

        self.label_fan = tk.Label(self.fan_frame, text="Fan Light", font=("Arial", 16))
        self.label_fan.pack(pady=(0, 5))

    def place_buttons(self):
        # Fan Light Buttons
        self.button_fan_on = tk.Button(self.fan_frame, text="Fan Light On", command=self.fanLight.turnOn, width=20, height=2)
        self.button_fan_on.pack(pady=2)

        self.button_fan_off = tk.Button(self.fan_frame, text="Fan Light Off", command=self.fanLight.turnOff, width=20, height=2)
        self.button_fan_off.pack(pady=2)

        self.button_changeFanToRed = tk.Button(self.fan_frame, text="Night", bg="red", fg="white", command=self.fanLight.changeToRed, width=20, height=2)
        self.button_changeFanToRed.pack(pady=2)

        self.button_changeFanToWhite = tk.Button(self.fan_frame, text="Morning", bg="grey", fg="white", command=self.fanLight.changeToWhite, width=20, height=2)
        self.button_changeFanToWhite.pack(pady=2)

        self.button_changeFanToBlue = tk.Button(self.fan_frame, text="Study", bg="blue", fg="white", command=self.fanLight.changeToBlue, width=20, height=2)
        self.button_changeFanToBlue.pack(pady=2)

        # Lamp Light Buttons
        self.button_lamp_on = tk.Button(self.lamp_frame, text="Lamp Light On", command=self.lampLight.turnOn, width=20, height=2)
        self.button_lamp_on.pack(pady=2)

        self.button_lamp_off = tk.Button(self.lamp_frame, text="Lamp Light Off", command=self.lampLight.turnOff, width=20, height=2)
        self.button_lamp_off.pack(pady=2)

        self.button_changeLampToRed = tk.Button(self.lamp_frame, text="Red", bg="red", fg="white", command=self.lampLight.changeToRed, width=20, height=2)
        self.button_changeLampToRed.pack(pady=2)

        self.button_changeLampToWhite = tk.Button(self.lamp_frame, text="Morning", bg="grey", fg="white", command=self.lampLight.changeToWhite, width=20, height=2)
        self.button_changeLampToWhite.pack(pady=2)

        self.button_changeLampToBlue = tk.Button(self.lamp_frame, text="Study", bg="blue", fg="white", command=self.lampLight.changeToBlue, width=20, height=2)
        self.button_changeLampToBlue.pack(pady=2)

        # Both Lights Buttons
        self.button_both_on = tk.Button(self.both_frame, text="All Lights On", command=self.turnOnBoth, width=20, height=2)
        self.button_both_on.pack(pady=2)

        self.button_both_off = tk.Button(self.both_frame, text="All Lights Off", command=self.turnOffBoth, width=20, height=2)
        self.button_both_off.pack(pady=2)

        self.button_both_red = tk.Button(self.both_frame, text="Night", bg="red", fg="white", command=self.changeBothToRed, width=20, height=2)
        self.button_both_red.pack(pady=2)

        self.button_both_white = tk.Button(self.both_frame, text="Morning", bg="grey", fg="white", command=self.changeBothToWhite, width=20, height=2)
        self.button_both_white.pack(pady=2)

        self.button_both_blue = tk.Button(self.both_frame, text="Study", bg="blue", fg="white", command=self.changeBothToBlue, width=20, height=2)
        self.button_both_blue.pack(pady=2)
