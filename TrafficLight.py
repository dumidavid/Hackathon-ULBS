import random
import time


class TrafficLight:
    def __init__(self, lanes):
        self.green_lane = None
        self.lanes = {lane: [] for lane in lanes}
        self.green_lane_index = 0

    def measure_traffic(self):
        for lane in self.lanes:
            cars_detected = random.randint(1, 10)
            distances = [random.randint(1, 200) for _ in range(cars_detected)]
            self.lanes[lane].extend(distances)
        return self.lanes

    def prioritisation(self):
        temppriority = [[], []]
        for lane, distances in self.measure_traffic().items():
            temppriority[0].append(lane)
            temppriority[1].append(len(distances))

        priority1, priority2 = zip(*sorted(zip(temppriority[1], temppriority[0])))
        return list(priority2)

    def traffic_lights_on_prioritisation(self):
        prioritized_lanes = self.prioritisation()

        if self.green_lane_index < len(prioritized_lanes):
            if self.green_lane_index >= 0:
                print(f"Green light for {prioritized_lanes[self.green_lane_index]} lane.")
                time.sleep(5)
                self.green_lane = prioritized_lanes[self.green_lane_index]
                print(f"Red light for {prioritized_lanes[self.green_lane_index]} lane.")
                time.sleep(2)
                self.green_lane_index += 1
            else:
                self.green_lane_index = 0

    def run_traffic_lights(self, duration):
        start_time = time.time()
        while time.time() - start_time < duration:
            self.traffic_lights_on_prioritisation()

