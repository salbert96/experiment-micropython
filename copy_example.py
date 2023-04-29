from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

def create_file():
    # The content should be copied from somewhere, for example, here
    # https://raw.githubusercontent.com/salbert96/experiment-micropython/master/example.py
    content = """
class MyClass:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def mysum(self):
        return self.a + self.b

    """
    filename = "example.py"

    with open(filename, "w") as file:
        file.write(content)

def read_file():
    filename = "example.py"

    with open(filename, "r") as file:
        content = file.read()

    return content

create_file() # Should be created only once     

import os
from example import MyClass

print('------------')
A = MyClass(1, 2)
print(A.mysum())
print('###')
print(os.listdir())
print('###')
print(read_file())
