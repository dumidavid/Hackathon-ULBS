import random


class TrafficLight:
    def __innit__(self, lanes):
        self.lanes = {lane: [] for lane in lanes}


def measure_traffic(self):
    for lane in self.lanes:
        cars_detected = random.randint(0, 10)
        distance = [random.randint(1, 200) for _ in range(cars_detected)]
        self.lanes[lane] = distance
