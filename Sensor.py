"""
This is the sensor class
"""
class sensor:

    def __init__(self, light) -> None:
        self._light=light
        print("Sensor constructor")

    def fetch(self):
        print("fetch pods")

    def identify(self):
        print("identify obstacles")

"""
Ultrasonic sensor is a subclass of sensor
"""
class Ultrasonicsensor:
    def __init__(self, light):
        super().__init__(light)
        print("Sensor constructor")
    def signalon(self):
        print("signal on to stop")

    def signaloff(self):
        print("signal off to move")
 """
Level Measuring Sensor is a subclass of sensor
"""
class Levelmeasuringsensor:
    def __init__(self, light):
        super().__init__(light)
        print("Sensor constructor")
    def signalon(self):
        print("signal on to instruct for charging")

    def signaloff(self):
        print("signal off to stop charging")
