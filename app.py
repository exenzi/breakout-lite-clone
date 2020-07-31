from tkinter import Tk, Canvas
from PIL import Image, ImageTk

from game.game import Game
from settings import *

tk = Tk()

# Инициализация окна Tkinter
tk.title(GAME_NAME)
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)

# Инициализация Canvas, на котором мы можем рисовать
canvas = Canvas(tk, width=WIDTH,
                height=HEIGHT, highlightthickness=0)
bg = ImageTk.PhotoImage(Image.open('bg.jpg').resize((WIDTH, HEIGHT)))
canvas.create_image(WIDTH / 2, HEIGHT / 2, image=bg)

canvas.pack()
tk.update()

# Импортируем настройки в словарь, понимаемый классом игры
settings = {
    'ball_size': BALL_SIZE,
    'ball_color': BALL_COLOR,
    'puddle_width': PUDDLE_WIDTH,
    'puddle_height': PUDDLE_HEIGHT,
    'puddle_color': PUDDLE_COLOR,
    'score_size': SCORE_SIZE,
    'score_color': SCORE_COLOR,
    'end_text_size': END_TEXT_SIZE,
    'end_text_color': END_TEXT_COLOR
}

# Инициализация игры
game = Game(tk, canvas, settings)

# Запуск игры
if __name__ == '__main__':
    game.run()
