class Analyzer:

    def __init__(self):
        self.numbers = []

    def add_number(self, x: int):
        self.numbers.append(x)

    def even_count(self) -> int:
        count = 0
        for num in self.numbers:
            if num % 2 == 0:
                count += 1
        return count

    def odd_count(self) -> int:
        count = 0
        for num in self.numbers:
            if num % 2 == 1:
                count += 1
        return count

    def highest_number(self):
        return max(self.numbers) if self.numbers else None

    def increasing_pairs(self) -> int:
        count = 0
        for i in range(1, len(self.numbers)):
            if self.numbers[i] > self.numbers[i - 1]:
                count += 1
        return count

    def average(self):
        return (sum(self.numbers) / len(self.numbers)) if self.numbers else None

    def range_diff(self):
        return (max(self.numbers) - min(self.numbers)) if self.numbers else None
