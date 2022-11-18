"""
This is the camera class
"""
class camera:

    def __init__(self, display) -> None:
        self._display=display
        print("Camera constructor")

    def readingbarcode(self):
        print("read bar codes on floor and pods")


"""
Upper camera is a subclass of camera
"""
class Uppercamera:
    def __init__(self, display):
        super().__init__(display)
        
    def readbarcodes(self):
        print("read bar codes of pods")

    
 """
Lower camera is a subclass of camera
"""
class Lowercamera:
    def __init__(self, display):
        super().__init__(display)
       
    def readbarcodes(self):
        print("read bar codes on the floor")
