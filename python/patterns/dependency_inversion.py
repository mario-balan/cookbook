# check: https://www.youtube.com/watch?v=Kv5jhbSkqLE

from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")


class Microwave(Switchable):
    def turn_on(self):
        print("Microwave: turned on...")

    def turn_off(self):
        print("Microwave: turned off...")


class ElectricPowerSwitch:
    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


l = LightBulb()
l_switch = ElectricPowerSwitch(l)
l_switch.press()
l_switch.press()

m = Microwave()
m_switch = ElectricPowerSwitch(m)
m_switch.press()
m_switch.press()