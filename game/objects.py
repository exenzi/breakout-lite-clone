import random

class Ball:
    def __init__(self, size, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        
        self.id = canvas.create_oval(0, 0, size, size, fill=color)
        self.canvas.move(self.id, 250, 100)

        starts = [-2, -1, 1, 2]
        random.shuffle(starts)

        self.x = starts[0]
        self.y = -2

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        self.hit_bottom = False

    def hit_paddle(self, pos):
        """Возвращает, докоснулся ли объект платформы"""
        paddle_pos = self.canvas.coords(self.paddle.id)

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True

        return False

    def draw(self):
        """Перемещение ball и повышение скорости"""
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        speed = self.score.get_difficulty_multiplier() * 2

        if pos[1] <= 0:
            self.y = speed

        if pos[3] >= self.canvas_height:
            self.hit_bottom = True

        if self.hit_paddle(pos):
            self.score.add_point()
            self.y = self.score.get_difficulty_multiplier() * -2


        if pos[0] <= 0:
            self.x = speed

        if pos[2] >= self.canvas_width:
            self.x = 0 - speed

class Paddle():
    def __init__(self, canvas, color, width, height, score):
        self.canvas = canvas
        self.score = score
        self.id = canvas.create_rectangle(0, 0, width, height, fill=color)

        start_1 = [40, 60, 120, 150, 180, 200]
        random.shuffle(start_1)
        self.start_pos_x = start_1[0]
        self.canvas.move(self.id, self.start_pos_x, 480)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        
    def turn_right(self, event):
        if self.canvas.coords(self.id)[2] < self.canvas_width: 
            self.x = self.score.get_difficulty_multiplier() * 2

    def turn_left(self, event):
        if self.canvas.coords(self.id)[0] > 0:
            self.x = self.score.get_difficulty_multiplier() * -2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)

        if self.canvas.coords(self.id)[0] <= 0:
            self.x = 0
        elif self.canvas.coords(self.id)[2] >= self.canvas_width:
            self.x = 0
        

class Score():
    def __init__(self, canvas, size, color):
        self.canvas = canvas
        self.score = 0 
        canvas_width = self.canvas.winfo_width()
        self.id = canvas.create_text(
            canvas_width - 50, size, text=self.score, font=('Ubuntu', size), fill=color)

    def add_point(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)

    def get_difficulty_multiplier(self):
        if self.score < 2:
            return 1
        elif self.score < 4:
            return 2
        else:
            return 4
