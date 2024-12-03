
class PixelRange:
    def __init__(self, start, end):
        if(start > end):
            start, end = end, start
        if(start < 0):
            start = 0
        if(end <= start):
            end+=1
        self.start = start
        self.end = end


class Color:
    __color: tuple[int,int,int]
    def __init__(self, r, g, b, brightness=1.):
        
        self.r = r
        self.g = g
        self.b = b
        self.__color = (r, g, b)
        self.brightness = brightness

    def set_brightness(self, brightness):
        self.brightness = brightness
        self.__color = (int(self.r * self.brightness), int(self.g * self.brightness), int(self.b * self.brightness))
        return self

    def lower_brightness(self, brightness=0.1):
        if(self.brightness <= 0 ):
            return self
        if(brightness > self.brightness):
            self.brightness= 0.
        else :
            self.brightness -= brightness
        
        self.__color = (int(self.r * self.brightness), int(self.g * self.brightness), int(self.b * self.brightness))
        return self
    
    def raise_brightness(self, brightness=0.1):
        if(self.brightness >= 1):
            return self
        self.brightness += brightness
        self.__color= (int(self.r * self.brightness), int(self.g * self.brightness), int(self.b * self.brightness))
        return self
    def set_color(self, r, g, b):
        self.__color = (r, g, b)

    def get_color(self):

        return (int(self.r * self.brightness), int(self.g * self.brightness), int(self.b * self.brightness))
    

class PodororoArgs:
    def __init__(self, work_duration:int, break_duration:int, work_color:Color, break_color:Color):
        self.work_duration = work_duration
        self.break_duration = break_duration
        self.work_color = work_color
        self.break_color = break_color