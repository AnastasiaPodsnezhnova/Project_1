from pprint import pprint  # импорт модуля pprint для красивого вывода


class RoadTrafficSimulation:

    def __init__(self, road, n):
        self.road = road
        self.n = n
        self.lights_time = {"G": 5, "O": 1, "R": 5}
        self.lights = {}
        self.prev_char = ""

    def next_color(self, color):
        if color == "G":
            return "O"
        elif color == "O":
            return "R"
        elif color == "R":
            return "G"

    def get_lights(self):
        for i in range(len(self.road)):
            char = self.road[i]

            if char != "." and char != "C":
                self.lights[i] = (char, self.lights_time[char])

    def update_lights(self, result):
        road = list(result)  # Преобразуем строку в список символов
        for key in self.lights:
            color, n = self.lights[key]
            n -= 1

            if key != road.index("C"):
                road[key] = color

            if n < 1:
                color = self.next_color(color)
                self.lights[key] = color, self.lights_time[color]
            else:
                self.lights[key] = color, n

        return "".join(road)
