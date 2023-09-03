"""Написать объектно-ориентированную реализацию.
В программе должны быть реализованы минимум один класс, три атрибута, два метода.

№12 Сгенерировать все возможные одномерные массивы из чисел 0, 1, 2 и 3"""


class Minimizer:
    def __init__(self, n):
        self.K = []
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    for l in range(n):
                        self.K.append([i, j, k, l])
        self.min_sum = float('inf')
        self.min_combination = None

    def check_constraints(self, combination):
        if all(x % 2 == 1 for x in combination[::2]) and all(x % 2 == 0 for x in combination[1::2]):
            return True
        else:
            return False

    def evaluate_function(self, combination):
        sum_mod = sum(abs(x) for x in combination) % 6
        return sum_mod

    def minimize(self):
        for combination in self.K:
            if self.check_constraints(combination):
                sum_mod = self.evaluate_function(combination)
                if sum_mod < self.min_sum:
                    self.min_sum = sum_mod
                    self.min_combination = combination
        print("Количество допустимых комбинаций:", sum_mod)
        print("Набор переменных, при котором достигается минимум:", self.min_combination)

minimizer = Minimizer(4)
minimizer.minimize()