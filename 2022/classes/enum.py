from enum import Enum


class TrafficLight(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3


print(TrafficLight.RED.value)
for x in TrafficLight:
    print(x.name)
