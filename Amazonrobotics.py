"""
This is the Amazon Robotics class
"""
class AmazonRobotics:

    def __init__(self, number, structure) -> None:
        self._number =number
        self._structure =structure
        print("AmazonRobotics constructor")

    def transporting(self):
        print("transport pods")