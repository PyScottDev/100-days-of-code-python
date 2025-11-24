class Counter:
    def __init__(self):
        self.score = 0

    def increase_score(self):
        self.score += 1
        return self.score

    def decrease_score(self):
        self.score -= 1
        return self.score

    def reset(self):
        self.score = 0
        return self.score

    def show(self):
        print(f"Current score: {self.score}")

current_score = Counter()
print(current_score.increase_score())
print(current_score.increase_score())
print(current_score.increase_score())


print(current_score.reset())
print(current_score.show())



