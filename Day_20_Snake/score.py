from turtle import Turtle
HIGH_SCORES = "Day_20_Snake/Snake_High_Score.txt"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open(HIGH_SCORES) as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 340)
        self.write("Score: 0", align="center", font=("Arial", 24, "normal"))
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.current_score} High Score: {self.high_score}",
                   align="center",
                   font=("Arial", 24, "normal"))

    def increase_score(self):
        self.current_score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open(HIGH_SCORES, mode="w") as file:
                file.write(str(self.high_score))
        self.current_score = 0
        self.update_scoreboard()