"""
This is the Battery class
"""
class Battery:

    def __init__(self, cells, connector) -> None:
        self. cells = cells
        self. connector = connector   #self. makes it an attribute  

    def powersupplyon(self):
        print("powersupplyon")

        """
        Method of supplying power
        """

    def Powersupplyoff(self):
        print("Powersupplyoff")