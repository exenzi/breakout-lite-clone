import time
from game.objects import *

class Game():
    def __init__(self, tk, canvas, settings):
        self.tk = tk
        self.canvas = canvas
        self.end_text_size = settings['end_text_size']
        self.end_text_color = settings['end_text_color']
        self.score = Score(canvas, settings['score_size'], settings['score_color'])
        self.paddle = Paddle(
            canvas, settings['puddle_color'], settings['puddle_width'], settings['puddle_height'], self.score)
        self.ball = Ball(settings['ball_size'], canvas, self.paddle, self.score, settings['ball_color'])

        self.game_started = False

        # Биндим клавиши
        self.canvas.bind_all('<KeyPress-Right>', self.paddle.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.paddle.turn_left)
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)

    def start_game(self, event):
        """Запуск игры"""
        self.game_started = True

    def run(self):
        """Основной цикл игры и конец игры, если ball коснулся дна"""
        while not self.ball.hit_bottom:
            if self.game_started:
                self.ball.draw()
                self.paddle.draw()
            self.__update_ui()

        canvas_width = self.canvas.winfo_width()
        self.canvas.create_text(
            canvas_width / 2, 120, text="Game over :(", font=('Ubuntu', self.end_text_size), fill=self.end_text_color)
        self.__update_ui()
        time.sleep(3)

    def __update_ui(self):
        """Обновляем интерфейс"""
        self.tk.update_idletasks()
        self.tk.update()
        time.sleep(0.01)
