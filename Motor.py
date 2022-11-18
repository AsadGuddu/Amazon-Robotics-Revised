"""
This is the Motor class
"""
class Motor:

    def __init__(self, accelerator, decelerator):
        self._accelerator=accelerator
        self._decelerator=decelerator
        print("Motor constructor")

    def accelerate(self):
        print("accelerate to move forward")

    def decelerate(self):
        print("decelerate to move backward")