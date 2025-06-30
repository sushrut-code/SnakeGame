from turtle import Turtle

class ScoreBoard(Turtle):
     def __init__(self):
         super().__init__()
         self.score=0
         self.color("white")
         self.penup()
         self.goto(0, 280)
         self.update_score_board()
         self.hideturtle()


     def update_score_board(self):
         self.write(arg=f"score: {self.score}", align="center", font=("Arial", 8, "normal"))


     def score_increase(self):
         self.score = self.score + 1
         self.clear()
         self.update_score_board()

     def game_over(self):
         self.goto(0,0)
         self.write(f"Game Over",align="center",font=("Arial",20,"bold"))







