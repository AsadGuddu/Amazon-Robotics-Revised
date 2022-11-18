"""
This is the Corkscrew class
"""
class Corkscrew:

    def __init__(self, screw, holdingplates) -> None:
        self. screw = screw
        self. holdingplates = holdingplates   #self. makes it an attribute  

    def lifting(self):
        print("turns righ to lift pods")

    def holding(self):
        print("holds pods to carry")

    def unload(self):
        print("turns left to unload pods")

        """
        Method of lifting, holding and unloading pods.
        """