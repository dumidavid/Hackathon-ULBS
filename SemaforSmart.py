import random


class TrafficLight:
    def __init__(self, lanes):
        self.lanes = {lane: [] for lane in lanes}

    def measure_traffic(self):
        for lane in self.lanes:
            cars_detected = random.randint(1, 10)
            distances = [random.randint(1, 200) for _ in range(cars_detected)]
            self.lanes[lane].extend(distances)
        return self.lanes

    def prioritisation(self):
        temppriority = [[], []]
        for lane, distances in self.measure_traffic().items():
            sum_dist = sum(distances)
            temppriority[0].append(lane)
            temppriority[1].append(sum_dist / len(distances))

        priority1, priority2 = zip(*sorted(zip(temppriority[1], temppriority[0])))
        return list(priority2)


if __name__ == '__main__':
    lanes = ["Lane1", "Lane2", "Lane3", "Lane4"]
    traffic_light = TrafficLight(lanes)
    a = traffic_light.prioritisation()

    print(a)