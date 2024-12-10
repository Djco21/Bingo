class Ball:
    def __init__(self, number, ischoosen):
        self.number = number
        self.ischoosen = ischoosen

    def __str__(self):
        return f'A bola de número {self.number} está {self.ischoosen}'