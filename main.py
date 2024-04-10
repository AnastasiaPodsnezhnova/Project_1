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

      # поменяли for на while и добавили отдельный индекс для машины
      # т.к. если использовать for, то он каждый раз стирает следующую машину
      self.change_light()
      while j < len(new_road) - 1:
        j += 1
        if c_ind == len(new_road) - 1:
          break

        # если следующий индекс после C = .
        if new_road[c_ind + 1] == ".":
          new_road[c_ind] = "."
          new_road[c_ind + 1] = "C"

        # если следующий индекс после C = R
        elif new_road[c_ind + 1] == "R":
          pass
