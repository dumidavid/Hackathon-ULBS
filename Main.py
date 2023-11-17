from TrafficLight import TrafficLight


class Main:
    lanes = ["Lane1", "Lane2", "Lane3", "Lane4"]
    traffic_light = TrafficLight(lanes)
    a = traffic_light.prioritisation()
    b = traffic_light.measure_traffic()
    print(b)
    print(a)
    traffic_light.run_traffic_lights(60)


Main()