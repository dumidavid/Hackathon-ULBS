import random
import time

class TrafficLight:
    def __init__(self, lanes):
        self.lanes = {lane: [] for lane in lanes}
        self.green_lane = None

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

    def traffic_lights_on_prioritisation(self):
        prioritized_lanes = self.prioritisation()
        if self.green_lane:
            print(f"Red light for {self.green_lane} lane.")
            time.sleep(2)
        self.green_lane = prioritized_lanes[0]
        print(f"Green light for {self.green_lane} lane.")
        time.sleep(5)

    def run_traffic_lights(self, duration):
        start_time = time.time()
        while time.time() - start_time < duration:
            self.traffic_lights_on_prioritisation()



if __name__ == '__main__':
    lanes = ["Lane1", "Lane2", "Lane3", "Lane4"]
    traffic_light = TrafficLight(lanes)
    traffic_light.run_traffic_lights(30)
