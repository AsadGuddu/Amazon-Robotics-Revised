"""
This is the Wheels class
"""
class Wheels:

    def __init__(self, brake):
        self._brake=brake
        print("Wheels constructor")

    def brake(self):
        print("brake to stop movement")

    def unbrake(self):
        print("unbrake to continue movement")