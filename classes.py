class Ball:
    def __init__(self, number, ischosen):
        self.number = (number,)
        self.ischosen = ischosen

    def __str__(self):
        return f'A bola de número {self.number} está {self.ischosen}'
    
    def change_status(self, status):
        self.ischosen = status