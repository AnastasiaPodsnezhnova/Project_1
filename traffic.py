# Вариант 1.
# Создайте класс, который имитирует дорожное движение.

# Правила:
# 1. Класс принимает дорогу road и время n.
# 2. Дорога является строкой типа ""C...R.....G....G.."
# 3. Время является числом.
# 4. На каждой итерации автомобиль "C" движется по дороге на 1 единицу вперед согласно сигналам светофора.
# 5. Сигнал светофора меняется следующим образом: G - 5 единиц времени --> O - 1 единица --> R - 5 единиц. Цикл повторяется.
# 6. Класс возвращает список строк каждой итерации

# Пример
road = ""C...R...R.R..G....G"
n = 15

# Результат:
# [   
#   "C...R...R.R..G....G", // 0   Стартовая позиция
#   ".C..R...R.R..G....G", // 1
#   "..C.R...R.R..G....G", // 2
#   "...CR...R.R..G....G", // 3
#   "...CR...R.R..G....G", // 4
#   "....C...G.G..O....O", // 5   C вместо G
#   "....GC..G.G..R....R", // 6
#   "....G.C.G.G..R....R", // 7
#   "....G..CG.G..R....R", // 8
#   "....G...C.G..R....R",  // 9
#   "....O...OCO..G....G",  // 10
#   "....R...RCR..G....G",  // 11
#   "....R...RCR..G....G",  // 12
#   "....R...RCR..G....G",  // 13
#   "....R...RCR..G....G",  // 14
#   "....R...RCR..G....G",  // 15