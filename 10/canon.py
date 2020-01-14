#klasa canon, wykonanie działa, oznacza strzał,
import math

class canon:
    def __init__(self, max_energy, *angle_range):
        self._range_env= angle_range
        self._max_energy=max_energy
        #self.angle=angle

    def __call__(self, weight):
        print(math.sqrt(2*5230000/weight)*math.sqrt(2*5230000/weight)*math.sin(math.radians(2*self.GetAngle))/9.81)

    def SetAngle(self, elev):
        if elev>self._range_env[0] or elev<self._range_env[1]:
            raise print("xx")

    def GetAngle(self):
        return self._curr_elev*math.pi/180
    
