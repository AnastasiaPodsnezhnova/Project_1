from pprint import pprint  # импорт модуля pprint для красивого вывода


class RoadTrafficSimulation:

  def __init__(self, road, n):
    self.road = road
    self.n = n
    self.signals = ["G", "O", "R"]
    self.signal_cycle = [5, 1, 5]


def change_light(self):
  pass


def simulate(self):
  result = [self.road]

  for i in range(self.n):
    new_road = list(result[i])
    j = -1  # переменная цикла для while
    c_ind = new_road.index("C")  # текущий индекс машины
