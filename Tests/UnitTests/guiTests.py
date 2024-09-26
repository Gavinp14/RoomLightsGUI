from unittest.mock import MagicMock
import unittest
from GUI import GUI

class TestGUI(unittest.TestCase):
    def setUp(self):
        # Create mock objects for lampLight and fanLight
        self.lampLight = MagicMock()
        self.fanLight = MagicMock()

        # Create the GUI application
        self.app = GUI(self.lampLight, self.fanLight)

        # Add the GUI's main loop to avoid blocking
        self.app.update_idletasks()
        self.app.update()

    def test_lamp_light_on_button_calls_turn_on(self):
        # Simulate clicking the "Lamp Light On" button
        self.app.button_lamp_on.invoke()  # Simulates button click

        # Assert that the turnOn method was called on lampLight
        self.lampLight.turnOn.assert_called_once()


if __name__ == "__main__":
    unittest.main()